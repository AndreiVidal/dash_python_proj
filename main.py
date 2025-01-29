import pandas as pd
import streamlit as st


file_path = "influenciadores.xlsx"
df = pd.read_excel(file_path, skiprows=1)

df.columns = [
    "Nome do Influencer", "Arroba", "Nota", "Data de Trabalho",
    "Experiência", "Conselho", "Extra"
]

df = df.dropna(subset=["Nome do Influencer"]).reset_index(drop=True)

df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")

st.set_page_config(page_title="Dashboard de Influenciadores", layout="wide")
st.title("📊 Dashboard de Influenciadores")

st.sidebar.header("🔍 Filtros")
search = st.sidebar.text_input("Buscar Influenciador", "")

if search:
    df = df[df["Nome do Influencer"].str.contains(search, case=False, na=False)]

st.subheader("📋 Tabela de Avaliações")
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("📌 **Dica**: Use a barra lateral para pesquisar influenciadores.")
