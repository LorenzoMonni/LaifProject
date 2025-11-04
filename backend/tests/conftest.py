import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from main import app
import models
import database

# ==========================================================
# ✅ DB di test (in memoria o su file temporaneo)
# ==========================================================

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# Per stare 100% in memoria: "sqlite:///:memory:" (ma non persiste tra test)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ricrea le tabelle pulite prima dei test
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

# ==========================================================
# 🔁 Override vero di get_db
# ==========================================================

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# ⚠️ Qui sovrascriviamo la dipendenza FastAPI
app.dependency_overrides[database.get_db] = override_get_db

# ==========================================================
# 🔧 Fixture client test
# ==========================================================

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
