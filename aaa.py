import streamlit as st
import pandas as pd
 
st.title("Mon Application Streamlit")
st.write("Ceci est une application Streamlit exécutée depuis Jupyter Notebook.")

st.title("charger et utiliser un fichier excel avec pandas")

uploaded_file = st.file_uploader("choisissez un fichier Excel", type=["xlsx"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Données chargées :")
    st.dataframe(df)
    st.write("Statistiques descriptives")
    st.write(df.describe())