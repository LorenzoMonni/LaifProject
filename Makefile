# ========================================
# 💊 CareMonitor Makefile
# Per gestione semplice da terminale o PyCharm
# ========================================

# Variabili ambiente (override se serve)
ENV_FILE=backend/.env
PYTHON=python
BACKEND_DIR=backend
FRONTEND_DIR=frontend

# ========================================
# 🔧 Setup ambiente
# ========================================

install:
	@echo "📦 Installazione dipendenze..."
	cd $(BACKEND_DIR) && pip install -e .
	cd $(FRONTEND_DIR) && pip install -r requirements.txt
	@echo "✅ Installazione completata!"

init-db:
	@echo "🧱 Inizializzo il database (PostgreSQL deve essere in esecuzione)..."
	cd $(BACKEND_DIR) && $(PYTHON) -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
	@echo "✅ Database pronto!"

mock-data:
	@echo "🧪 Genero dati fittizi (dal container backend)..."
	docker compose exec backend python mock_data.py
	@echo "✅ Mock data generati!"


# ========================================
# 🚀 Avvio backend (FastAPI)
# ========================================

run-api:
	@echo "🚀 Avvio backend FastAPI su http://localhost:8000 ..."
	cd $(BACKEND_DIR) && uvicorn main:app --reload --env-file $(ENV_FILE)

# ========================================
# 💻 Avvio frontend (Streamlit)
# ========================================

run-ui:
	@echo "🩺 Avvio frontend Streamlit su http://localhost:8501 ..."
	cd $(FRONTEND_DIR) && streamlit run app.py

# ========================================
# 🧰 Utility
# ========================================

lint:
	@echo "🧹 Linting con Black e isort..."
	cd $(BACKEND_DIR) && black . && isort .

clean:
	@echo "🗑️ Pulizia file temporanei..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "✅ Pulizia completata!"

# Esegui test
test:
	cd backend && pytest -v

# Esegui solo unit test
test-unit:
	cd backend && pytest tests/unit -v

# Esegui solo integration test
test-integration:
	cd backend && pytest tests/integration -v


# ========================================
# 🏁 Help
# ========================================

help:
	@echo ""
	@echo "=== CareMonitor Makefile ==="
	@echo "Comandi disponibili:"
	@echo "  make install       -> Installa tutte le dipendenze"
	@echo "  make init-db       -> Crea le tabelle nel DB"
	@echo "  make mock-data     -> Genera dati fittizi"
	@echo "  make run-api       -> Avvia backend FastAPI"
	@echo "  make run-ui        -> Avvia frontend Streamlit"
	@echo "  make lint          -> Formatta il codice"
	@echo "  make clean         -> Rimuove file temporanei"
	@echo ""
