import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys

# Carica .env
load_dotenv()

ENV = os.getenv("ENV", "dev")

if ENV == "test":
    DATABASE_URL = "sqlite:///:memory:"
else:
    DATABASE_URL = os.getenv("DATABASE_URL")

# if "pytest" in sys.modules and "sqlite" not in DATABASE_URL:
#     raise RuntimeError("❌ I test non dovrebbero usare PostgreSQL! Usa SQLite in-memory invece.")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 🔧 Avvia sessione DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()