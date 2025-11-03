import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app

# DB temporaneo (usiamo SQLite in RAM per i test)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# Per test più isolati: sqlite:///:memory:

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea le tabelle
Base.metadata.create_all(bind=engine)

# Override della dependency FastAPI get_db
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Client FastAPI
@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
