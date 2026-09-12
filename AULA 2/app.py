import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

model = LinearRegression()

dados_vd = pd.DataFrame({
    'investimento': [100,200,300,550,750,800],
    'faturamento' : [1200,2500,3700,3900,5500,6900]
})

st.header('Previsão de Vendas') 
st.write(dados_vd)

X = dados_vd[['investimento']]
y = dados_vd['faturamento']

model.fit(X,y)

inv = st.number_input('Digite o investimento', value = 0)

if inv:
    if st.button("Analisar"):
        prev = model.predict([[inv]])[0]
        st.write(f'Faturamento previsto: {prev:.2f} **') 