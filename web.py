## importe de librerias

import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import folium
from streamlit_folium import folium_static
 

# Extrar los archivos pickle
with open('loc_reg.pkl', 'rb') as li:
  lin_reg = pickle.load(li)
#-----------------------------------------


def classify(num):
  """
    Funcion para poder mostrar el texto de acuerdo a la salida de la prediccion.
  """
  if(num[0]==1):
    st.sidebar.error('    SI, necesita cuidarse mas')
  elif(num[0]==0):
    st.sidebar.success('NO, no deje de cuidarse') 

def main():
    st.markdown('''<h1 style='text-align: center; font-size:60px;'>PORTAL COVID-19: <strong style='color:#8A1E41; font-weight: bold;'>COLIMA</strong></h1>''', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
      st.markdown('''<h4 style='color: green; text-align: center;'>ULTIMAS NOTICIAS</h4>''',unsafe_allow_html=True)
      st.image("img/covid.jpeg", caption='COVID')
      st.markdown('''
        <p style='text-align: justify'>Colima es la capital del estado mexicano del mismo nombre. Se ubica cerca de la costa del Pacífico central, en un valle al sur del volcán Colima. El Jardín Libertad es su plaza principal y cuenta con un quiosco belga del siglo XIX y el Portal Medellín, un gran edificio con filas de arcos.</p>
      ''',
      unsafe_allow_html=True
      )

    with col2:
      st.markdown('''<h4 style='color: white; text-align: center;'>CONOCE COLIMA</h4>''',unsafe_allow_html=True)
      st.image("img/colima.jpg",caption='COLIMA')
      st.markdown(
        """Colima es la capital del estado mexicano del mismo nombre. Se ubica cerca de la costa del Pacífico central, en un valle al sur del volcán Colima. El Jardín Libertad es su plaza 
        principal y cuenta con un 
        quiosco belga del siglo 
        XIX y el Portal Medellín,
        un gran edificio con fi-
        las de arcos."""
      )

    with col3:
      st.markdown('''<h4 style='color: red; text-align: center;'>VACUNAS</h4>''',unsafe_allow_html=True)
      st.image("img/vacuna.jpeg",caption='VACUNA')
      st.markdown(
        """Colima es la capital del estado mexicano del mismo nombre. Se ubica cerca de la costa del Pacífico central, en un valle al sur del volcán Colima. El Jardín Libertad es su plaza 
        principal y cuenta con un 
        quiosco belga del siglo 
        XIX y el Portal Medellín,
        un gran edificio con fi-
        las de arcos."""
      )

    # center on Liberty Bell
    m = folium.Map(location=[19.240488139909974, -103.83160271891987], zoom_start=9)

    # add marker for Liberty Bell
    tooltip = "Liberty Bell"
    folium.Marker(
        [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)

    st.sidebar.title('¿Quieres saber si eres propenso a COVID-19?')
    st.sidebar.subheader('Llena los siguientes campos:')

    def user_unput():
      displaySexo = ("Hombre", "Mujer")
      optionsSexo = list(range(len(displaySexo)))

      displayDiabetes = ("No", "Si")
      optionsDiabetes = list(range(len(displayDiabetes)))

      displayEpoc = ("No", "Si")
      optionsEpoc = list(range(len(displayEpoc)))

      displayAsma = ("No", "Si")
      optionsAsma = list(range(len(displayAsma)))

      displayInmunosupresion = ("No", "Si")
      optionsInmunosupresion = list(range(len(displayInmunosupresion)))

      displayHipertension = ("No", "Si")
      optionsHipertension = list(range(len(displayHipertension)))

      displayCardiovascular = ("No", "Si")
      optionsCardiovascular = list(range(len(displayCardiovascular)))

      displayObesidad = ("No", "Si")
      optionsObesidad = list(range(len(displayObesidad)))

      displayTabaquismo = ("No", "Si")
      optionsTabaquismo = list(range(len(displayTabaquismo)))

      displayRenal = ("No", "Si")
      optionsRenal = list(range(len(displayRenal)))

      displayNeumonia = ("No", "Si")
      optionsNeumonia = list(range(len(displayRenal)))

      edad = st.sidebar.slider('Edad', 0, 100, 25)
      sexo = st.sidebar.selectbox('Sexo', optionsSexo, format_func=lambda x: displaySexo[x])
      diabetes = st.sidebar.selectbox('Diabetes', optionsDiabetes, format_func=lambda x: displayDiabetes[x])
      epoc = st.sidebar.selectbox('Enfermedad pulmonar obstructiva crónica', optionsEpoc, format_func=lambda x: displayEpoc[x])
      asma = st.sidebar.selectbox('Asma', optionsAsma, format_func=lambda x: displayAsma[x])
      inmunosupresion = st.sidebar.selectbox('Inmunosupresión', optionsInmunosupresion, format_func=lambda x: displayInmunosupresion[x])
      hipertension = st.sidebar.selectbox('Hipertensión', optionsHipertension, format_func=lambda x: displayHipertension[x])
      cardiovascular = st.sidebar.selectbox('Cardiovascular', optionsCardiovascular, format_func=lambda x: displayCardiovascular[x])
      obesidad = st.sidebar.selectbox('Obesidad', optionsObesidad, format_func=lambda x: displayObesidad[x])
      tabaquismo = st.sidebar.selectbox('Tabaquismo', optionsTabaquismo, format_func=lambda x: displayTabaquismo[x])
      renal = st.sidebar.selectbox('Renal Cronica', optionsRenal, format_func=lambda x: displayRenal[x])
      neumonia = st.sidebar.selectbox('Neumonia', optionsNeumonia, format_func=lambda x: displayNeumonia[x])
      data = {
        'sexo': sexo,
        'neumonia': neumonia, 
        'edad': edad,
        'diabetes': diabetes,
        'epoc': epoc,
        'asma': asma,
        'inmunosupresion': inmunosupresion,
        'hipertension': hipertension,
        'cardiovascular': cardiovascular,
        'obesidad': obesidad,
        'renal': renal,
        'tabaquismo': tabaquismo
      }

      features = pd.DataFrame(data, index= [0])
      return features

    df = user_unput()
    st.write(df)

    if st.sidebar.button('Predict'): 
      classify(lin_reg.predict(df))

    

if __name__ == '__main__':
    main()