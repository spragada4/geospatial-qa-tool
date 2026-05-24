# 🌍 Geospatial QA Assistant

A fully local, AI-powered documentation Q&A tool built for geospatial test engineers. Ask natural language questions about PostGIS, GDAL, CRS, OGC standards, and spatial testing — and get accurate, sourced answers instantly. No cloud. No API keys. Everything runs on your machine.

---

## What It Does

- Answers technical questions about PostGIS, GDAL, Shapely, pyproj, GeoJSON, and OGC standards
- Cites the source document for every answer so engineers can verify
- Runs entirely locally — no data leaves your machine
- Supports adding your own internal project documentation (PDFs)
- Simple browser-based chat interface

---

## How It Works

```
Public Geospatial Docs (PostGIS, GDAL, Shapely, OGC...)
              ↓
     LangChain ingestion + chunking
              ↓
     nomic-embed-text (Ollama) → ChromaDB
              ↓
     llama3.1 via Ollama (local LLM)
              ↓
     Streamlit Chat UI → http://localhost:8501
```

---

## Requirements

| Requirement | Minimum | Recommended |
|---|---|---|
| Python | 3.10+ | 3.11 |
| RAM | 16 GB | 32 GB |
| Disk space | 15 GB free | 20 GB free |
| GPU | Not required | 8GB VRAM (e.g. RTX 3060) |
| OS | macOS / Linux / Windows | macOS / Linux |

> **Note:** Without a GPU the tool still works but responses will take 15–30 seconds. With a GPU responses come in 1–3 seconds.

---

## Installation

### Step 1: Install Ollama

Ollama runs the LLM locally on your machine.

**macOS:**
Download and install from https://ollama.com/download/mac

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Windows:**
Download and install from https://ollama.com/download/windows

Verify the installation:
```bash
ollama --version
```

---

### Step 2: Pull the Required Models

```bash
# The LLM (approx 4.7 GB download)
ollama pull llama3.1

# The embedding model (approx 274 MB download)
ollama pull nomic-embed-text
```

Test the LLM is working:
```bash
ollama run llama3.1 "What is ST_IsValid in PostGIS?"
# Type /bye to exit
```

---

### Step 3: Clone the Repository

```bash
git clone https://github.com/spragada4/geospatial-qa-tool.git
cd geospatial-qa-tool
```

---

### Step 4: Create a Virtual Environment

```bash
python -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

---

### Step 5: Fix SSL Certificates (macOS only)

If you are on macOS and encounter SSL errors during pip install, run this first:

```bash
open /Applications/Python\ 3.11/Install\ Certificates.command
```

Or via terminal:
```bash
/Applications/Python\ 3.11/Install\ Certificates.command
```

---

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 7: Run Document Ingestion

This downloads and indexes all public geospatial documentation into a local vector database. Only needs to be run once (or when you add new documents).

```bash
cd src
python ingest.py
```

Expected output:
```
==================================================
  GEOSPATIAL QA — DOCUMENT INGESTION
==================================================

📥 Loading 12 URLs...
  → https://postgis.net/docs/reference.html
     ✓ Loaded 1 document(s)
  ...

✂️  Chunking 12 documents...
   ✓ Created 3842 chunks

🔢 Embedding and storing in ChromaDB...
   ✓ Vector store saved to ./data/db

✅ Ingestion complete! Ready to query.
```

> This step takes approximately 5–15 minutes depending on your internet connection.

---

### Step 8: Launch the App

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## Project Structure

```
geospatial-qa-tool/
├── src/
│   ├── config.py       # Models, paths, URLs, settings
│   ├── ingest.py       # Document loading, chunking, embedding
│   ├── qa.py           # Retrieval chain and LLM logic
│   └── app.py          # Streamlit chat UI
├── data/
│   ├── raw/            # Drop your own PDFs here
│   └── db/             # ChromaDB vector store (auto-generated)
├── requirements.txt
└── README.md
```

---

## Adding Your Own Project Documentation

You can add internal project docs (test plans, data dictionaries, bug reports, API specs) to extend the knowledge base.

1. Copy your PDFs into `data/raw/`:
```bash
cp your-test-plan.pdf data/raw/
cp your-data-dictionary.pdf data/raw/
```

2. Re-run ingestion:
```bash
cd src
python ingest.py
```

The new documents are merged into the existing knowledge base automatically.

---

## Example Questions

Once the app is running, try these:

**PostGIS**
- `What is ST_IsValid and when should I use it?`
- `How do I find self-intersecting geometries in PostGIS?`
- `What is the difference between ST_Within and ST_Contains?`
- `How do I create a spatial index in PostGIS?`

**CRS & Projections**
- `What EPSG code should I use for WGS84 lat/lng?`
- `How do I reproject geometry from EPSG:4326 to EPSG:3857?`
- `What is the difference between geometry and geography types?`

**GDAL**
- `How do I convert a shapefile to GeoJSON using ogr2ogr?`
- `How do I reproject a raster file with gdalwarp?`

**OGC / GeoJSON**
- `What is the correct structure of a GeoJSON FeatureCollection?`
- `What is the difference between WFS and WMS?`

---

## Configuration

All settings are in `src/config.py`:

```python
# Change the LLM model
OLLAMA_MODEL = "llama3.1"          # or "mistral", "llama3.1:70b"

# Change the embedding model
EMBEDDING_MODEL = "nomic-embed-text"   # or "mxbai-embed-large"

# Adjust chunk size (larger = more context, slower)
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64

# Number of document chunks retrieved per query
TOP_K_RESULTS = 5
```

---

## Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `ollama: command not found` | Ollama not installed or not in PATH | Restart terminal after install |
| SSL certificate error on pip install | macOS Python cert issue | Run `Install Certificates.command` (Step 5) |
| Slow responses (15–30s) | Running on CPU only | Normal without GPU — consider smaller model like `mistral` |
| `ModuleNotFoundError` on any import | Package not installed | Run `pip install -r requirements.txt` again |
| ChromaDB errors on startup | Corrupted vector store | Delete `data/db/` and re-run `python ingest.py` |
| URL fails during ingestion | Site blocking scrapers | Download the page as PDF, place in `data/raw/` |
| Out of memory error | Model too large for RAM | Switch to `mistral` in `config.py` |

---

## Improving the Tool

Once the base tool is working, here are ways to make it better:

- **Add more URLs** to `GEOSPATIAL_URLS` in `config.py` and re-run ingestion
- **Add internal docs** — drop PDFs into `data/raw/` and re-run ingestion
- **Upgrade the embedding model** — switch to `mxbai-embed-large` for better retrieval accuracy
- **Upgrade the LLM** — pull `llama3.1:70b` if you have 16GB+ VRAM
- **Enable hybrid search** — combine semantic + keyword search for exact function name lookups

---

## Tech Stack

| Component | Technology |
|---|---|
| LLM | Llama 3.1 8B via Ollama |
| Embeddings | nomic-embed-text via Ollama |
| Vector Store | ChromaDB (local) |
| RAG Framework | LangChain |
| UI | Streamlit |
| Document Loading | LangChain WebBaseLoader + PyPDFLoader |

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-improvement`
3. Commit your changes: `git commit -m "add: my improvement"`
4. Push the branch: `git push origin feature/my-improvement`
5. Open a Pull Request

---

## License

MIT License — free to use, modify, and distribute.

---

## Author

Built by [@spragada4](https://github.com/spragada4) as an tooling project for geospatial test engineering teams.