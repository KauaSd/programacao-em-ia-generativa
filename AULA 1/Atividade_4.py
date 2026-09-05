import streamlit as st
import pandas as pd

data = {"nomes": ["Gustavo","Guilherme","João"], "Idade": ["30","20","26"]}
datap = pd.DataFrame (data=data)
nome = "oi"
st.dataframe(datap)
st.table(datap)


st.info(f"teste: {nome}")