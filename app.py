import streamlit as st
import random

st.header('Lanzar una moneda')

# Función para simular el lanzamiento de una moneda
def lanzar_moneda():
    resultado = random.choice(['Cara', 'Cruz'])
    return resultado

# Interfaz de usuario
if st.button('Lanzar Moneda'):
    resultado = lanzar_moneda()
    st.write(f'Resultado: {resultado}')
