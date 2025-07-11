import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráfico Rápido com CSV")

# Upload
uploaded_file = st.file_uploader("Envie seu arquivo CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, sep=None, engine='python')
        else:
            df = pd.read_excel(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.write("Prévia dos dados:", df.head())

        # Seleção de eixos
        x_col = st.selectbox("Escolha o eixo X", df.columns)
        y_col = st.selectbox("Escolha o eixo Y", df.select_dtypes(include='number').columns)

        # Plot
        if x_col and y_col:
            fig, ax = plt.subplots()
            df.groupby(x_col)[y_col].sum().plot(kind='bar', ax=ax)
            ax.set_ylabel(y_col)
            ax.set_xlabel(x_col)
            ax.set_title(f"{y_col} por {x_col}")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")
