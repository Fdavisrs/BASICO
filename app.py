import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar o CSV
st.title("Análise de Vendas - Gráfico Personalizado")
uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Detectar colunas numéricas e categóricas
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    # Interface para seleção de eixos
    x_axis = st.selectbox("Escolha o eixo X (agrupamento):", categorical_columns)
    y_axis = st.selectbox("Escolha o eixo Y (valor numérico):", numeric_columns)

    # Escolher tipo de gráfico
    chart_type = st.radio("Tipo de gráfico:", ["Barra", "Linha", "Pizza"])

    # Agrupamento e exibição
    if x_axis and y_axis:
        grouped = df.groupby(x_axis)[y_axis].sum().reset_index()

        if chart_type == "Barra":
            st.plotly_chart(px.bar(grouped, x=x_axis, y=y_axis, title=f"{y_axis} por {x_axis}"))
        elif chart_type == "Linha":
            st.plotly_chart(px.line(grouped, x=x_axis, y=y_axis, title=f"{y_axis} por {x_axis}"))
        elif chart_type == "Pizza":
            st.plotly_chart(px.pie(grouped, names=x_axis, values=y_axis, title=f"{y_axis} por {x_axis}"))
    else:
        st.warning("Por favor, selecione os eixos corretamente.")
