from sqlalchemy import create_engine
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
CHARTS_DIR = BASE_DIR / "charts"
EXPORTS_DIR = BASE_DIR / "exports"
DATASETS_DIR = BASE_DIR / "datasets"

PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB   = os.getenv("PG_DB")

ENGINE_URL = f"postgresql+psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}"
ENGINE = create_engine(ENGINE_URL, echo=False, future=True)

print(f"Connected to DB: {PG_HOST}:{PG_PORT}/{PG_DB} as {PG_USER}")
