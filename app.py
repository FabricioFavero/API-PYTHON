import requests
import streamlit as st

st.image("https://i.imgur.com/SmktDIH.png")

st.title ("Letra de Músicas")

banda = st.text_input ("Digite o nome da banda", key="banda")
musica = st.text_input ("Digite o nome da Música", key="musica")