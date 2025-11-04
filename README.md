# 🏥 CareMonitor

Sistema demo per monitoraggio pazienti in una casa di riposo. La gestione degli entry-point per l'installazione e la gestione
dell'app è stata progettata tramite il Makefile nella root di progetto. Per informazioni dettagliate sul suo funzionamento
eseguire:

```bash
make help
```


## Architettura
- **Backend**: FastAPI + SQLAlchemy + PostgreSQL  
- **Frontend**: Streamlit
- **Database**: PostgreSQL
- **Container**: Docker Compose

## Installazione
Il seguente comando installa tramite servizio di Docker Compose tutti i componenti dockerizzati dell'applicazione:

```bash
make install
```
## Avvio
```bash
make run
```
E visualizzazione app nel browser all'url http://localhost:8501/


## Main APIs
- POST /patients/

- GET /patients/

- POST /measurements/

- GET /patients/{id}/summary