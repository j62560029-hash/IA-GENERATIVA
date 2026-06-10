# calculadora


import streamlit as st





    #verificador de numero par ou impar

st.title('verificador de numeros par ou impar')

par = st.number_input('digite um numero')

impar = st.number_input('digite seu numero')

if st.button('verificar'):
    calculo = par + impar
    st.success('impar') or st.success('par')