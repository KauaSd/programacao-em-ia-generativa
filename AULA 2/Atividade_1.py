import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

model = LinearRegression()

dados = pd.read_csv('vendas.csv')

df = pd.DataFrame(dados)

X = df[["mes"]]
y = df["vendas"]
model.fit(X,y)


st.header("Vendas")

st.write(df)

value = st.number_input("digite o mês:", value=0 , max_value=12)

if value:
    if st.button("analisar"):
        res = model.predict([[value]])[0]

        st.write(f"valor para o mês {value} é: {res:.2f}")
