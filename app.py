import streamlit as st
from PIL import Image
from textblob import TextBlob
from googletrans import Translator

st.title("Mi primera app")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("facilmente puedo realizar backend y frontend:")
image = Image.open("gato.jpg")

st.image(image, caption="GATO")


texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("Texto ingresado:", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto")
with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual","Auditiva", "Tactil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "Tactil":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de Botones")
if st.button("Presiona el botón"):
      st.write("Gracias por presionar")
else:
  st.write("No has presionado eso")

st.subheader("Selectbox")
in_mod = st.selectbox("Selecciona la modalidad", ("Audio", "Visual", "Háptico"),)



if in_mod == "Audio":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir Video"
elif in_mod == "Háptico":
  set_mod = "Activar la vibración"
st.write("La acción es:",set_mod)

translator = Translator()
st.title('Uso de textblob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
               st.subheader("Polaridad y Subjetividad")
               ("""
                Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
                Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
                
               Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
               (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.

                 """
               ) 


with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:

        #translation = translator.translate(text1, src="es", dest="en")
        #trans_text = translation.text
        #blob = TextBlob(trans_text)
        blob = TextBlob(text1)
       
        
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
       text2 = st.text_area('Escribe por favor: ',key='4')
       if text2:
          blob2=TextBlob(text2)
          st.write((blob2.correct()))                  
  
  
