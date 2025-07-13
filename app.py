import streamlit as st
import pandas as pd
from datetime import datetime

# Simuler base de données
if 'inspections' not in st.session_state:
    st.session_state.inspections = []

st.title("Inspection des Équipements")

technicien = st.text_input("Nom du technicien")
equipement_id = st.text_input("ID de l'équipement")
statut = st.selectbox("Statut", ["OK", "Warning", "Danger"])
description = st.text_area("Description")
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if st.button("Enregistrer Inspection"):
    new_entry = {
        "date": date,
        "technicien": technicien,
        "equipement_id": equipement_id,
        "statut": statut,
        "description": description
    }
    st.session_state.inspections.append(new_entry)
    st.success("Inspection enregistrée.")

# Historique (affichage)
if st.checkbox("Afficher l'historique"):
    df = pd.DataFrame(st.session_state.inspections)
    st.dataframe(df)
