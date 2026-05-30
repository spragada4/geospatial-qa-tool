# src/ingest.py

import os
import sys
os.environ["USER_AGENT"] = "geospatial-qa-tool/1.0"

from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from config import (
    OLLAMA_MODEL,
    EMBEDDING_MODEL,
    CHROMA_DB_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    GEOSPATIAL_URLS,
)

def load_web_docs(urls: list) -> list:
    print(f"\n📥 Loading {len(urls)} URLs...")
    all_docs = []
    failed_urls = []

    for url in urls:
        try:
            print(f"  → {url}")
            loader = WebBaseLoader(url)
            loader.requests_kwargs = {
                "headers": {
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                },
                "timeout": 15
            }
            docs = loader.load()

            # Check if content is meaningful
            content = docs[0].page_content.strip() if docs else ""
            if len(content) < 200:
                print(f"     ⚠️  Too little content ({len(content)} chars) — site may be blocking")
                failed_urls.append(url)
                continue

            all_docs.extend(docs)
            print(f"     ✓ Loaded {len(docs)} doc(s), {len(content)} chars")

        except Exception as e:
            print(f"     ✗ Failed: {e}")
            failed_urls.append(url)

    if failed_urls:
        print(f"\n⚠️  {len(failed_urls)} URLs failed or returned too little content:")
        for url in failed_urls:
            print(f"   - {url}")
        print("   → Download these manually as PDFs and place in data/raw/\n")

    return all_docs

def load_pdf_docs(pdf_folder: str) -> list:
    """Load any PDFs dropped into data/raw/"""
    all_docs = []
    if not os.path.exists(pdf_folder):
        return all_docs
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_folder, filename)
            print(f"  → Loading PDF: {filename}")
            loader = PyPDFLoader(path)
            docs = loader.load()
            all_docs.extend(docs)
            print(f"     ✓ {len(docs)} pages loaded")
    return all_docs

def chunk_documents(docs: list) -> list:
    """Split documents into chunks."""
    print(f"\n✂️  Chunking {len(docs)} documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = splitter.split_documents(docs)
    print(f"   ✓ Created {len(chunks)} chunks")
    return chunks

def build_vectorstore(chunks: list) -> Chroma:
    """Embed chunks and store in ChromaDB."""
    print(f"\n🔢 Embedding and storing in ChromaDB...")
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_PATH,
    )
    print(f"   ✓ Vector store saved to {CHROMA_DB_PATH}")
    return vectorstore

def run_ingestion():
    print("=" * 50)
    print("  GEOSPATIAL QA — DOCUMENT INGESTION")
    print("=" * 50)

    # Load web docs
    web_docs = load_web_docs(GEOSPATIAL_URLS)

    # Load any PDFs in data/raw/
    pdf_docs = load_pdf_docs("./data/raw")

    all_docs = web_docs + pdf_docs

    if not all_docs:
        print("\n❌ No documents loaded. Check URLs or add PDFs to data/raw/")
        sys.exit(1)

    print(f"\n📄 Total documents loaded: {len(all_docs)}")

    # Chunk
    chunks = chunk_documents(all_docs)

    # Embed and store
    build_vectorstore(chunks)

    print("\n✅ Ingestion complete! Ready to query.\n")

if __name__ == "__main__":
    run_ingestion()