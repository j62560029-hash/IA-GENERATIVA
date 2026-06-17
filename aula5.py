import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Detector de Spam com IA",
    page_icon="✉️",
    layout="centered"
)

# 1. Dados de Treino Base (Exemplos de Spam e Não-Spam)
@st.cache_resource
def treinar_modelo_base():
    # Exemplos práticos exigidos no escopo
    mensagens_ham = [
        "Oi, tudo bem? Vamos almoçar mais tarde?",
        "Segue em anexo o relatório da reunião de ontem.",
        "Você viu a nova tarefa no sistema? Preciso de ajuda.",
        "Gostei muito do projeto, parabéns pelo resultado!",
        "Confirma sua presença no evento de amanhã?"
    ]
    
    mensagens_spam = [
        "GANHE DINHEIRO FÁCIL TRABALHANDO DE CASA! CLIQUE AQUI!",
        "URGENTE: Seu banco informou que sua conta será bloqueada. Atualize agora.",
        "Parabéns! Você foi o sorteado para receber um prêmio de 10 mil reais!",
        "Compre Bitcoin agora com 50% de desconto garantido.",
        "Pílulas milagrosas e ofertas exclusivas só hoje! Aproveite."
    ]
    
    X_texto = mensagens_ham + mensagens_spam
    # 0 para Não-Spam (Ham), 1 para Spam
    y = np.array([0] * len(mensagens_ham) + [1] * len(mensagens_spam))
    
    # Pré-processamento de Texto com Keras
    tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
    tokenizer.fit_on_texts(X_texto)
    
    sequencias = tokenizer.texts_to_sequences(X_texto)
    padded = pad_sequences(sequencias, maxlen=20, padding='post', truncating='post')
    
    # Construção de um modelo simples e leve de NLP com TensorFlow
    model = Sequential([
        Embedding(1000, 16, input_length=20),
        GlobalAveragePooling1D(),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(padded, y, epochs=30, verbose=0)
    
    return model, tokenizer, mensagens_spam, mensagens_ham

# Inicializa o modelo e recupera as listas de exemplos
modelo, tokenizer, lista_spam, lista_ham = treinar_modelo_base()

# 2. Interface do Usuário (UI)
st.title("✉️ Detector de Spam Inteligente")
st.write("Insira o conteúdo do e-mail recebido abaixo para verificar se ele é malicioso.")

# Área de Input do Usuário
input_usuario = st.text_area("Cole a mensagem aqui:", height=150, placeholder="Ex: Olá, segue a fatura do mês...")

if st.button("Analisar Mensagem"):
    if input_usuario.strip() == "":
        st.warning("Por favor, digite ou cole alguma mensagem para analisar.")
    else:
        # Processar o input do usuário
        seq_usuario = tokenizer.texts_to_sequences([input_usuario])
        padded_usuario = pad_sequences(seq_usuario, maxlen=20, padding='post', truncating='post')
        
        # Predição com TensorFlow
        predicao = modelo.predict(padded_usuario)[0][0]
        
        st.subheader("Resultado da Análise:")
        # Limiar de decisão de 0.5
        if predicao >= 0.5:
            st.error(f"🚨 **Esta mensagem foi classificada como SPAM.** (Confiança: {predicao*100:.2f}%)")
        else:
            st.success(f"✅ **Esta mensagem é SEGURA (Não é Spam).** (Confiança: {(1-predicao)*100:.2f}%)")

# 3. Seções de Exemplos (Exigência do Escopo)
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Exemplos de Spam")
    for item in lista_spam:
        st.markdown(f"- *\"{item}\"*")

with col2:
    st.subheader("📌 Exemplos Seguros (Não Spam)")
    for item in lista_ham:
        st.markdown(f"- *\"{item}\"*")