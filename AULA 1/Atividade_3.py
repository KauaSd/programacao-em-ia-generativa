import streamlit as st
curso = st.selectbox("Selecione o curso", ("BackEnd", "FrontEnd"))
if curso =="BackEnd":
    tecnologias = st.multiselect("escolha sua tecnologias", ["Python","Java","PHP","Express","Vue.js","FastAPI","Flask"])
elif curso == "FrontEnd":
    tecnologias = st.multiselect("escolha suas tecnologias", ["React","JS","TS","Next.js","Angular", "Tailwind"])
