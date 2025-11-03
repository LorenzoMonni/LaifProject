# 🏥 CareMonitor

Sistema demo per monitoraggio pazienti in una casa di riposo.

## Architettura
- **Backend**: FastAPI + SQLAlchemy + PostgreSQL  
- **Frontend**: Streamlit
- **Database**: PostgreSQL
- **Container**: Docker Compose

## Avvio
```bash
docker-compose up --build
```


## Main APIs
- POST /patients/

- GET /patients/

- POST /measurements/

- GET /patients/{id}/summary