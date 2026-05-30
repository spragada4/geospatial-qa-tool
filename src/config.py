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

    # PostgreSQL deep docs
    "https://www.postgresql.org/docs/current/queries.html",
    "https://www.postgresql.org/docs/current/queries-overview.html",
    "https://www.postgresql.org/docs/current/queries-table-expressions.html",
    "https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-FROM",
    "https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-WHERE",
    "https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-GROUP",
    "https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-GROUPING-SETS",
    "https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-WINDOW",
    "https://www.postgresql.org/docs/current/queries-select-lists.html",
    "https://www.postgresql.org/docs/current/queries-select-lists.html#QUERIES-COLUMN-LABELS",
    "https://www.postgresql.org/docs/current/queries-select-lists.html#QUERIES-DISTINCT",
    "https://www.postgresql.org/docs/current/queries-union.html",
    "https://www.postgresql.org/docs/current/queries-order.html",
    "https://www.postgresql.org/docs/current/queries-limit.html",
    "https://www.postgresql.org/docs/current/queries-values.html",
    "https://www.postgresql.org/docs/current/queries-with.html",
    "https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-SELECT",
    "https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-RECURSIVE",
    "https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-CTE-MATERIALIZATION",
    "https://www.postgresql.org/docs/current/queries-with.html#QUERIES-WITH-MODIFYING",

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

    # OpenLayers
    "https://openlayers.org/en/latest/apidoc/",

    # ── British National Grid / EPSG:27700 ────────────────
    "https://spatialreference.org/ref/epsg/27700/",
    "https://proj.org/en/stable/operations/projections/tmerc.html",

    # ── PostGIS additional functions ─────────────────────
    "https://postgis.net/docs/ST_Equals.html",
    "https://postgis.net/docs/ST_DWithin.html",
    "https://postgis.net/docs/ST_SnapToGrid.html",
    "https://postgis.net/docs/ST_AsGeoJSON.html",
    "https://postgis.net/docs/ST_GeomFromGeoJSON.html",
    "https://postgis.net/docs/ST_Buffer.html",
    "https://postgis.net/docs/ST_Union.html",
    "https://postgis.net/docs/ST_Intersection.html",
    "https://postgis.net/docs/ST_IsValid.html",

    # ── GDAL programs ────────────────────────────────────
    "https://gdal.org/programs/ogrinfo.html",
    "https://gdal.org/programs/ogr2ogr.html",
    "https://gdal.org/programs/gdalwarp.html",
    "https://gdal.org/programs/gdal_translate.html",

    # ── GeoServer CQL / filtering ───────────────────────
    "https://docs.geoserver.org/stable/en/user/tutorials/cql/cql_tutorial.html",

    # ── Java geospatial ──────────────────────────────────
    "https://docs.geotools.org/latest/userguide/",
    "https://docs.geotools.org/latest/userguide/library/referencing/index.html",
    "https://docs.geotools.org/latest/userguide/library/data/index.html",
    "https://locationtech.github.io/jts/jts-faq.html",

    # ──JavaScript testing ───────────────────────────────
    "https://jestjs.io/docs/getting-started",
    "https://jestjs.io/docs/expect",
    "https://playwright.dev/docs/intro",
    "https://playwright.dev/docs/api/class-page",
    "https://playwright.dev/docs/locators",
    "https://docs.cypress.io/guides/overview/why-cypress",
    "https://docs.cypress.io/api/commands/get",

    # ── Selenium ─────────────────────────────────────────
    "https://www.selenium.dev/documentation/webdriver/",
    "https://www.selenium.dev/documentation/webdriver/elements/",
    "https://www.selenium.dev/documentation/webdriver/interactions/",
    "https://www.selenium.dev/documentation/test_practices/",

    # ── Capybara / Ruby ──────────────────────────────────
    "https://rubydoc.info/github/teamcapybara/capybara/master",
    "https://www.rubydoc.info/gems/capybara",

    # ── OpenLayers examples ──────────────────────────────
    "https://openlayers.org/en/latest/examples/",

    # ── Leaflet examples ─────────────────────────────────
    "https://leafletjs.com/examples/geojson/",

    # ── GeoPandas additional ─────────────────────────────
    "https://geopandas.org/en/stable/docs/user_guide/projections.html",
    "https://geopandas.org/en/stable/docs/user_guide/io.html",

    # ── Proj additional ──────────────────────────────────
    "https://proj.org/en/stable/operations/projections/index.html",

    # ── QGIS ─────────────────────────────────────────────
    "https://docs.qgis.org/3.44/en/docs/user_manual/index.html",
    "https://docs.qgis.org/3.44/en/docs/user_manual/working_with_vector/vector_properties.html",
    "https://docs.qgis.org/3.44/en/docs/user_manual/working_with_vector/expression_field_calculator.html",
    "https://docs.qgis.org/3.44/en/docs/user_manual/working_with_projections/working_with_projections.html",
    "https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/index.html",
    "https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/vectorgeometry.html",
    "https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/vectoranalysis.html",
    "https://docs.qgis.org/3.44/en/docs/user_manual/processing_algs/qgis/vectoroverlay.html",

    # QGIS PyQGIS (Python scripting)
    "https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/index.html",
    "https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/loadlayer.html",
    "https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/vector.html",
    "https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/crs.html",
    "https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/geometry.html",
    "https://docs.qgis.org/3.44/en/docs/pyqgis_developer_cookbook/expressions.html",

    # QGIS Server (WMS/WFS serving)
    "https://docs.qgis.org/3.44/en/docs/server_manual/index.html",
    "https://docs.qgis.org/3.44/en/docs/server_manual/services/wms.html",
    "https://docs.qgis.org/3.44/en/docs/server_manual/services/wfs.html",

    # QGIS gentle introduction (good for non-technical context)
    "https://docs.qgis.org/3.44/en/docs/gentle_gis_introduction/index.html",
    "https://docs.qgis.org/3.44/en/docs/gentle_gis_introduction/coordinate_reference_systems.html",
    "https://docs.qgis.org/3.44/en/docs/gentle_gis_introduction/vector_data.html",
    "https://docs.qgis.org/3.44/en/docs/gentle_gis_introduction/raster_data.html",
]