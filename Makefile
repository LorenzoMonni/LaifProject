# ========================================
# 💊 CareMonitor Makefile
# Gestione semplificata progetto Docker (FastAPI + Streamlit + PostgreSQL)
# ========================================

# Variabili ambiente
ENV_FILE=backend/.env
PROJECT_NAME=caremonitor
BACKEND_CONTAINER=backend
DB_CONTAINER=db
FRONTEND_CONTAINER=frontend

# ========================================
# 🔧 Setup & Build
# ========================================

# Builda TUTTE le immagini Docker (senza cache)
install:
	@echo "📦 Buildo tutte le immagini Docker per il progetto $(PROJECT_NAME)..."
	docker compose build --no-cache
	@echo "✅ Build completata!"

# Avvio completo dello stack
run:
	@echo "🚀 Avvio di tutti i servizi Docker..."
	docker compose up -d
	@echo "✅ Tutti i container sono in esecuzione!"

# Stoppa tutto
stop:
	@echo "🛑 Arresto e rimozione dei container..."
	docker compose down
	@echo "✅ Tutti i container sono stati arrestati!"

# Ricostruisci solo il backend
rebuild-backend:
	@echo "🔁 Ricostruzione immagine backend..."
	docker compose build --no-cache backend
	@echo "✅ Backend ricostruito!"

# Mostra i log live
logs:
	@echo "📜 Mostro i log di tutti i container..."
	docker compose logs -f

# ========================================
# 🧱 Database
# ========================================

init-db:
	@echo "🧱 Inizializzo il database (PostgreSQL deve essere in esecuzione)..."
	docker compose exec $(BACKEND_CONTAINER) python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
	@echo "✅ Database pronto!"

mock-data:
	@echo "🧪 Genero dati fittizi nel database..."
	docker compose exec $(BACKEND_CONTAINER) python mock_data.py
	@echo "✅ Mock data generati!"

# ========================================
# 🧰 Utility
# ========================================

lint:
	@echo "🧹 Linting del backend con Black e isort..."
	docker compose exec $(BACKEND_CONTAINER) black .
	docker compose exec $(BACKEND_CONTAINER) isort .
	@echo "✅ Lint completato!"

clean:
	@echo "🗑️ Pulizia file temporanei e container..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	docker system prune -f
	@echo "✅ Pulizia completata!"

# ========================================
# 🧪 Test
# ========================================

test:
	@echo "🧪 Eseguo tutti i test..."
	docker compose exec $(BACKEND_CONTAINER) pytest -v
	@echo "✅ Test completati!"

test-unit:
	@echo "🧩 Eseguo unit test..."
	docker compose exec $(BACKEND_CONTAINER) pytest tests/unit -v

test-integration:
	@echo "🔗 Eseguo integration test..."
	docker compose exec $(BACKEND_CONTAINER) pytest tests/integration -v

# ========================================
# 🏁 Help
# ========================================

help:
	@echo ""
	@echo "=== 💊 CareMonitor Makefile ==="
	@echo "Comandi principali:"
	@echo "  make install           → Builda tutte le immagini Docker"
	@echo "  make up                → Avvia stack (backend + db + frontend)"
	@echo "  make down              → Ferma e rimuove i container"
	@echo "  make rebuild-backend   → Ricostruisce solo il backend"
	@echo "  make logs              → Mostra i log in tempo reale"
	@echo ""
	@echo "Gestione DB:"
	@echo "  make init-db           → Crea le tabelle nel DB"
	@echo "  make mock-data         → Popola il DB con dati fittizi"
	@echo ""
	@echo "Utility:"
	@echo "  make lint              → Linting backend"
	@echo "  make clean             → Pulizia temporanei e cache Docker"
	@echo ""
	@echo "Testing:"
	@echo "  make test              → Tutti i test"
	@echo "  make test-unit         → Solo unit test"
	@echo "  make test-integration  → Solo integration test"
	@echo ""
