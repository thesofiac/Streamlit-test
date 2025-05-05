# app.py
import streamlit as st
import pandas as pd
import joblib

# Carregar modelo e dados
pipeline = joblib.load('pipeline.pkl')
data = pd.read_csv('data.csv')

st.title("Classificador Binário")

menu = st.sidebar.selectbox("Escolha uma opção", [
    "Prever a partir de features",
    "Buscar por ID",
    "Top 10 maiores e menores probabilidades"
])

if menu == "Prever a partir de features":
    st.subheader("Previsão com valores de entrada")
    f1 = st.number_input("Feature 1", value=0.0)
    f2 = st.number_input("Feature 2", value=0.0)
    f3 = st.number_input("Feature 3", value=0.0)

    if st.button("Prever"):
        input_df = pd.DataFrame([[f1, f2, f3]], columns=['feature1', 'feature2', 'feature3'])
        prediction = pipeline.predict(input_df)[0]
        prob = pipeline.predict_proba(input_df)[0, 1]
        st.write(f"Previsão: {prediction} (Probabilidade de 1: {prob:.2f})")

elif menu == "Buscar por ID":
    st.subheader("Buscar dados por ID")
    id_input = st.text_input("Digite o ID (ex: id_0)")
    
    if st.button("Buscar"):
        result = data[data['ID'] == id_input]
        if not result.empty:
            st.write(result[['feature1', 'feature2', 'feature3', 'label', 'prob_1']])
        else:
            st.write("ID não encontrado.")

elif menu == "Top 10 maiores e menores probabilidades":
    st.subheader("Top 10 maiores e menores probabilidades de 1")
    top_10 = data.nlargest(10, 'prob_1')[['ID', 'prob_1']]
    bottom_10 = data.nsmallest(10, 'prob_1')[['ID', 'prob_1']]

    st.write("## Top 10 maiores probabilidades")
    st.dataframe(top_10.reset_index(drop=True))

    st.write("## Top 10 menores probabilidades")
    st.dataframe(bottom_10.reset_index(drop=True))

