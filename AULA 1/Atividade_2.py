import streamlit as st

nome = st.text_input("Digite seu Nome:")
idade = st.number_input("Digite sua idade: ", value=0)
checkbox = st.checkbox("Eu aceito os termos de uso")
button = st.button("enviar")
if button and checkbox:
    st.info(nome)
    st.info(idade)
elif button:
    st.info("aceite os termos")