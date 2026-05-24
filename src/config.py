# src/config.py

# Model settings
OLLAMA_MODEL = "llama3.1"
EMBEDDING_MODEL = "nomic-embed-text"  # lightweight, fast embeddings

# Paths
CHROMA_DB_PATH = "./data/db"
RAW_DATA_PATH = "./data/raw"

# Chunking settings
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64

# Retrieval settings
TOP_K_RESULTS = 5

# Public docs to index
GEOSPATIAL_URLS = [
    # PostGIS
    "https://postgis.net/docs/reference.html",
    "https://postgis.net/docs/using_postgis_dbmanagement.html",
    "https://postgis.net/docs/performance_tips.html",

    # GDAL
    "https://gdal.org/programs/ogr2ogr.html",
    "https://gdal.org/programs/gdalwarp.html",
    "https://gdal.org/programs/gdal_translate.html",

    # Shapely
    "https://shapely.readthedocs.io/en/stable/manual.html",

    # pyproj
    "https://pyproj4.github.io/pyproj/stable/api/crs/crs.html",

    # GeoJSON spec
    "https://geojson.org/",
]