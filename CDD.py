import streamlit as st
st.title('Eco Política')
with st.sidebar:
  st.header("Eco Política")
  st.write("o seu guia sobre o meio ambiente na política")
  st.caption("Criado por Manuela Muniz, Clarissa Treptow e Maria Julia Figuereido") 

st.write("Nosso site tem como objetivo propor uma democratização da informação de projetos ou não que defendam e protejam mudanças climáticas. Para entender mais clique na nossa aba 'Saiba Mais'") 
tab_deputados, tab_ementas, tab_saibamais = st.tabs(["Deputados", "Ementas", "Saiba mais"])
         
         
