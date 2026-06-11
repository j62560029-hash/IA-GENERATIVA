import streamlit as st

# Título da página web
st.title("🔢 Verificador de Par ou Ímpar")
st.write("Digite um número abaixo para saber se ele é par ou ímpar automaticamente.")

# Cria uma caixa para o usuário digitar ou selecionar o número
# (step=1 garante que só aceitará números inteiros)
numero = st.number_input("Digite um número inteiro:", step=1, value=0)

# O Streamlit roda o código de cima a baixo toda vez que o número muda
if numero % 2 == 0:
    st.success(f"O número **{numero}** é **PAR**! 🎉")
else:
    st.info(f"O número **{numero}** é **ÍMPAR**! 💡")
