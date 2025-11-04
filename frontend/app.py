import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import os
from dotenv import load_dotenv

# Carica variabili da .env
load_dotenv()

API_URL = os.getenv("API_URL", "http://backend:8000")

st.set_page_config(page_title="CareMonitor", page_icon="🏥", layout="wide")
st.title("🏥 CareMonitor - Monitoraggio Pazienti")

patients = requests.get(f"{API_URL}/patients/").json()

if not patients:
    st.warning("Nessun paziente trovato. Esegui il generatore di mock data (mock_data.py).")
    st.stop()

selected = st.selectbox("Seleziona paziente", [p["name"] for p in patients])
patient = next(p for p in patients if p["name"] == selected)

st.subheader(f"{patient['name']} ({patient['age']} anni) - Stanza {patient['room']}")

summary = requests.get(f"{API_URL}/patients/{patient['id']}/summary").json()
if "message" in summary:
    st.warning(summary["message"])
else:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("❤️ Battito medio", summary["avg_heart_rate"])
    col2.metric("🌡️ Temperatura media", summary["avg_temperature"])
    col3.metric("💉 Pressione media", summary["avg_blood_pressure"])
    col4.metric("📈 Misurazioni", summary["count"])

# Grafico storico
df = pd.DataFrame(patient["measurements"])
if len(df) > 0:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    tabs = st.tabs(["❤️ Frequenza cardiaca", "🌡️ Temperatura", "💉 Pressione"])
    with tabs[0]:
        st.plotly_chart(px.line(df, x="timestamp", y="heart_rate"))
    with tabs[1]:
        st.plotly_chart(px.line(df, x="timestamp", y="temperature"))
    with tabs[2]:
        st.plotly_chart(px.line(df, x="timestamp", y="blood_pressure"))
