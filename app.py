import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hypercar Performance Analysis", layout="wide")
st.title("🚀 Hypercar Performance Analysis")

# Cargar dataset
df = pd.read_csv("data/hypercar_specs.csv")

st.subheader("Tabla de especificaciones")
st.dataframe(df)

# Procesar columnas numéricas (extraer valores de strings)
df["power_hp_numeric"] = pd.to_numeric(df["power_hp"].str.extract(r"(\d+)")[0], errors="coerce")
df["top_speed_mph_numeric"] = pd.to_numeric(df["top_speed_mph"].str.extract(r"(\d+)")[0], errors="coerce")

# Gráfico: Potencia vs Velocidad máxima
st.subheader("Potencia vs Velocidad máxima (mph)")
fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(df["power_hp_numeric"], df["top_speed_mph_numeric"], color="royalblue")

for i, txt in enumerate(df["name"]):
    if not pd.isna(df["power_hp_numeric"].iloc[i]) and not pd.isna(df["top_speed_mph_numeric"].iloc[i]):
        ax.annotate(txt, (df["power_hp_numeric"].iloc[i], df["top_speed_mph_numeric"].iloc[i]), fontsize=7)

ax.set_xlabel("Potencia (hp)")
ax.set_ylabel("Velocidad máxima (mph)")
ax.grid(True, linestyle="--", alpha=0.5)
st.pyplot(fig)
