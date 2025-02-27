import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("facilmente puedo realizar backend y frontend:")
image = Image.open("gato.jpg")

st.image(image, caption="GATO")


texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("Texto ingresado:", texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)
