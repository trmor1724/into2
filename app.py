import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("facilmente puedo realizar backend y frontend:")
image = Image.open("gato.jpg")

st.image(image, caption="Interfaces multimodales")
