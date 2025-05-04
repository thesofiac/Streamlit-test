import streamlit as st

# Título da aplicação
st.title("Calculadora de Quadrado")

# Caixa de entrada numérica
numero = st.number_input("Digite um número", value=1)

# Botão para calcular
if st.button("Calcular quadrado"):
    resultado = numero ** 2
    st.success(f"O quadrado de {numero} é {resultado}")
