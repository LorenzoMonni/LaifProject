# Usa Python 3.13, ma con strumenti di compilazione
FROM python:3.13-slim

# Evita input interattivi e caching apt
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# Installa dipendenze di sistema necessarie a psycopg2 e uvicorn
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia il progetto nel container
COPY . /app

# Aggiorna pip e installa le dipendenze Python (pyproject o requirements)
RUN pip install --upgrade pip setuptools wheel

# Se hai pyproject.toml:
RUN pip install -e .

# oppure, se preferisci requirements.txt, sostituisci con:
# RUN pip install -r requirements.txt

# Espone la porta API
EXPOSE 8000

# Avvia l'app FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
