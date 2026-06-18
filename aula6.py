# app.py
import streamlit as st
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os

# Configuração visual do Streamlit
st.set_page_config(page_title="Preditor de Aprovação", page_icon="🎓")
st.title("🎓 Preditor de Aprovação do Aluno")
st.write("Esse app treina uma IA e prevê a chance de aprovação com base nas horas de estudo.")

NOME_DO_MODELO = 'modelo_aprovacao.h5'

# --- FUNÇÃO PARA TREINAR E SALVAR O MODELO ---
def treinar_e_salvar_modelo():
    # Dados da professora
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([0, 0, 0, 1, 1])

    # Estrutura do modelo
    model = keras.Sequential([
        layers.Dense(4, activation='relu', input_shape=[1]),
        layers.Dense(1, activation='sigmoid')
    ])

    # Compilação e Treino
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=500, verbose=0)

    # Salva o arquivo .h5
    model.save(NOME_DO_MODELO)
    return model

# --- CARREGAR OU TREINAR ---
@st.cache_resource
def obter_modelo():
    # Se o modelo já existir, carrega ele. Se não, treina do zero!
    if os.path.exists(NOME_DO_MODELO):
        return keras.models.load_model(NOME_DO_MODELO)
    else:
        st.warning("Modelo não encontrado. Treinando a IA pela primeira vez, aguarde...")
        model = treinar_e_salvar_modelo()
        st.success("IA treinada com sucesso!")
        return model

# Executa a função para garantir que o modelo está pronto
model = obter_modelo()

# --- INTERFACE GRÁFICA ---
st.subheader("Faça sua Previsão")
horas = st.slider("Horas de estudo:", min_value=1.0, max_value=10.0, value=3.0, step=0.5)

if st.button("Prever Resultado"):
    entrada = np.array([[horas]])
    predicao = model.predict(entrada)[0][0]
    
    st.subheader(f"Probabilidade de aprovação: {predicao * 100:.2f}%")
    
    if predicao >= 0.5:
        st.success("Resultado: provável APROVAÇÃO! 🎉")
    else:
        st.error("Resultado: provável REPROVAÇÃO. 📚 Precisa estudar mais!")