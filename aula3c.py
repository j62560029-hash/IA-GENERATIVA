import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


st.header("Previsão de Vendas")


dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})


st.scatter_chart(dados_vendas, x='investimento', y='faturamento')

modelo = LinearRegression()
modelo.fit(dados_vendas[['investimento']], dados_vendas['faturamento'])


opcao_usuario = st.slider('Escolha o valor para investir', 0, 1000, 250)


previsao = modelo.predict([[opcao_usuario]])

st.metric('Faturamento previsto:', previsao[0])