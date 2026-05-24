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
    # OGC Standards
    "https://www.ogc.org/standard/wfs/",
    "https://www.ogc.org/standard/wms/",
    "https://www.ogc.org/standard/wcs/",
    "https://www.ogc.org/standard/geopackage/",

    # EPSG / CRS
    "https://epsg.io/about",
    "https://spatialreference.org/",

    # GeoJSON & formats
    "https://www.rfc-editor.org/rfc/rfc7946",
    "https://www.geopackage.org/",

    # PostGIS deep docs
    "https://postgis.net/docs/using_raster_dataman.html",
    "https://postgis.net/docs/using_postgis_query.html",
    "https://postgis.net/docs/ST_IsValidReason.html",
    "https://postgis.net/docs/ST_MakeValid.html",
    "https://postgis.net/docs/ST_Transform.html",

    # GDAL formats
    "https://gdal.org/drivers/vector/index.html",
    "https://gdal.org/drivers/raster/index.html",

    # GeoServer
    "https://docs.geoserver.org/stable/en/user/services/wfs/reference.html",
    "https://docs.geoserver.org/stable/en/user/services/wms/reference.html",
    "https://docs.geoserver.org/stable/en/user/services/wcs/reference.html",

    # MapLibre / Leaflet
    "https://maplibre.org/maplibre-gl-js/docs/",
    "https://leafletjs.com/reference.html",

    # Proj / pyproj
    "https://proj.org/en/stable/operations/index.html",

    # GeoPandas
    "https://geopandas.org/en/stable/docs/user_guide.html",

    # Turf.js (spatial analysis)
    "https://turfjs.org/docs/",

    # OpenLayers (map rendering)
    "https://openlayers.org/en/latest/apidoc/",
]