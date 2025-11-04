import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from main import app
from database import Base, get_db

# Percorso file test DB
TEST_DB_FILE = "./test.db"

# Se esiste, lo rimuoviamo per iniziare puliti
if os.path.exists(TEST_DB_FILE):
    os.remove(TEST_DB_FILE)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_FILE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # richiesto da SQLite con più thread
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creiamo tutte le tabelle una volta sola
Base.metadata.create_all(bind=engine)

# Override della dipendenza FastAPI
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
