import streamlit as st

st.title("Sumadora de dos numeros de Josemaria Cano Cavazos")

numero1 = st.number_input("ingresa el primer numero", value=0)

numero2 = st.number_input("ingresa el segundo numero", value=0)

suma = numero1 + numero2

st.write(f"la suma de {numero1} + {numero2} es: {suma}")

