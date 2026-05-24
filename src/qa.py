# src/qa.py

from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from config import (
    OLLAMA_MODEL,
    EMBEDDING_MODEL,
    CHROMA_DB_PATH,
    TOP_K_RESULTS,
)

GEOSPATIAL_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an expert assistant for geospatial test engineers.
Your job is to answer questions about spatial data, PostGIS,
GDAL, coordinate reference systems, OGC standards, and
geospatial testing practices.

Use ONLY the context provided below to answer.
If the answer is not in the context, say:
"I don't have enough documentation to answer this confidently.
Try checking the official docs or adding them to the knowledge base."

Never guess EPSG codes, function names, or standard numbers.
Be concise, technical, and accurate.

Context:
{context}

Question:
{question}

Answer:
"""
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def load_qa_chain():
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings,
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K_RESULTS},
    )

    llm = OllamaLLM(model=OLLAMA_MODEL, temperature=0.1)

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | GEOSPATIAL_PROMPT
        | llm
        | StrOutputParser()
    )

    return chain, retriever

def ask(qa_chain_tuple, question: str) -> dict:
    chain, retriever = qa_chain_tuple

    # Get source documents
    source_docs = retriever.invoke(question)
    sources = list({doc.metadata.get("source", "Unknown") for doc in source_docs})

    # Get answer
    answer = chain.invoke(question)

    return {
        "answer": answer,
        "sources": sources,
    }