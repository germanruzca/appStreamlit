## importe de librerias
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import os 

# Extrar los archivos pickle
with open('loc_reg.pkl', 'rb') as li:
  lin_reg = pickle.load(li)
#-----------------------------------------

def classify(num):
  """

    Funcion para poder mostrar el texto de acuerdo a la salida de la prediccion.

  """
  if(num[0]==1):
    st.sidebar.error('Usted es una persona propensa a contagiar de COVID, necesita cuidarse mas')
  elif(num[0]==0):
    st.sidebar.success('Usted no es una persona propensa a contagiar de COVID, no deje de cuidarse')

def main():
  """

    Funcion principal, donde se carga lo que no debe de llevar un proceso con el conjunto de datos.

  """

  st.markdown(
    '''
      <h1 style='text-align: center; font-size:60px;'>
        PORTAL COVID-19: <strong style='color:#8A1E41; font-weight: bold;'>COLIMA</strong>
      </h1>
    '''
      , unsafe_allow_html=True
  )
  st.markdown(
    '''
      <div
        style='text-align:justify;'
      >
        <h1 style='text-align:center;'>Conoce más</h1>
        <p>
          Los coronavirus son una familia de virus que causan enfermedades que van desde el resfriado común hasta enfermedades respiratorias más graves, circulan entre humanos y animales. A veces, los coronavirus que infectan a los animales pueden evolucionar, transmitirse a las personas y convertirse en una nueva cepa de coronavirus capaz de provocar enfermedades en los seres humanos, tal y como sucedió con el Síndrome Respiratorio Agudo Severo (SARS), en Asia en febrero de 2003 y, el Síndrome Respiratorio de Oriente Medio (MERS-CoV), que fue detectado por primera vez en Arabia Saudita en 2012.
          <hr>    
        </p>
      </div>
    '''
    ,unsafe_allow_html=True
  )

  # MAPA
def mapa():
  """

     Funcion que renderiza el mapa

  """
  json= f"mun.geojson"
  m = folium.Map(location=[19.186312000984255, -103.84036982502],tiles='CartoDB positron',name="Light Map", zoom_start=9, attr="My Data attribution")

  #Carga el conjunto de datos de los municipios.
  colima_info = f'municipios.csv'
  colima_info_data = pd.read_csv(colima_info)
  st.markdown(
    """
      <h3 style='text-align:center;'>Mapa del Estado de Colima</h3>
    """
    , unsafe_allow_html=True
  )
  st.warning("Mapa que indica los casos y muertes del estado de Colima por municipios.")

  choice = ['Casos', 'Muertes']
  choice_selected = st.selectbox('Selecciona: ',choice)

  folium.Choropleth(
    geo_data = json,
    name="choropleth",
    data= colima_info_data,
    columns=["code",choice_selected],
    key_on="feature.properties.num_mun",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.1,
    legend_name=choice_selected
  ).add_to(m)
  folium.features.GeoJson('mun.geojson',name="Municipios",popup=folium.features.GeoJsonPopup(fields=['nombre'],labels=False)).add_to(m)
  folium_static(m)
  st.markdown("""<hr>""",unsafe_allow_html=True)

#Despliegue de la interfaz izquierda
st.sidebar.image('img/logo.png')
st.sidebar.title('¿Quieres saber si eres propenso a COVID-19?')
st.sidebar.subheader('Llena los siguientes campos:')


def user_unput():
  """
  
    Funcion que se encarga de obtener los valores del usuario para poder usar el modelo de ML.
  
  """
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

# Crea un conjuto de datos que se guarda en la variable df
df = user_unput()

#Si el boton el presionado se llama a hablar a la funcion que reproduce el mensaje
#Pasando compo parametro el resultado de la prediccion del modelo previamente entreando.
if st.sidebar.button('Predict'):
  classify(lin_reg.predict(df))


def generadorMultimedia():
  """

    Funcion que sirve para generar las imagenes de las graficas, asi como los archvios faltantes.
  
  """

  # Si no se encuentra las imagenes o el archivo de la informacion de los municipios procede a generarlos
  if not os.path.isfile('img/SEXO.png') or not os.path.isfile('municipios.csv'):
    with st.spinner('Wait for it...'):
      #Carga del archivo, desde una direccion externa a la carpeta principal
      #Esto con la razon de que el repositorio que estara guardando la infor no acepta archivos pesados

      #Se puede sustituir por el archvio descargado en https://datos.gob.mx/busca/dataset/informacion-referente-a-casos-covid-19-en-mexico
      data = pd.read_csv('../../../Desktop/tesis/analisis/211122COVID19MEXICO.csv')

      munList = ['ARMERÍA','COLIMA','COMALA','COQUIMATLÁN','CUAUHTÉMOC','IXTLAHUACÁN','MANZANILLO','MINATITLÁN','TECOMÁN','VILLA DE ÁLVAREZ']
      codeList = []
      casosList = []
      muertesList = []

      #Ciclo para poder realizar el conjunto de datos
      for i in range(1,11):
        codeList.append(i)
        casosList.append(((data['ENTIDAD_RES'] == 6) & (data['MUNICIPIO_RES'] == i)).sum())
        muertesList.append(((data['ENTIDAD_RES'] == 6) & (data['MUNICIPIO_RES']==i) & (data['FECHA_DEF'] != '9999-99-99')).sum())
      
      municipiosDF = {'code': codeList, 'Municipio': munList, 'Casos': casosList, 'Muertes': muertesList}
      mun_data = pd.DataFrame(municipiosDF)

      #Se guarda el conjunto de datos.
      mun_data.to_csv('municipios.csv', header=True, index=False)

      #Se eliminan los campos inecesarios o no requeridos para la creacion de las graficas.
      data = data.drop(columns=['SECTOR','ENTIDAD_UM','INTUBADO','ENTIDAD_NAC','ENTIDAD_RES','MUNICIPIO_RES', 'TIPO_PACIENTE','FECHA_INGRESO','FECHA_SINTOMAS','FECHA_DEF','NACIONALIDAD','EMBARAZO','HABLA_LENGUA_INDIG','INDIGENA', 'OTRA_COM','TOMA_MUESTRA_LAB','TOMA_MUESTRA_ANTIGENO','RESULTADO_LAB','ID_REGISTRO','MIGRANTE','PAIS_NACIONALIDAD','PAIS_ORIGEN','UCI','FECHA_ACTUALIZACION','ORIGEN','RESULTADO_ANTIGENO','OTRO_CASO','NEUMONIA','EDAD','ASMA','EPOC','RENAL_CRONICA','TABAQUISMO','INMUSUPR'])

      #Colores a poder utilizar en las graficas
      colors  = ("dodgerblue","salmon", "palevioletred", 
              "steelblue", "seagreen", "plum", 
              "blue", "indigo", "beige", "yellow")
      
      #Ciclo que genera las graficas
      for i in range(data.shape[1]):
          sizes=data[f'{data.columns[i]}'].value_counts()
          pie=data[f'{data.columns[i]}'].value_counts().plot(kind='pie',colors=colors,shadow=True,autopct="%1.1f%%'",
                                          startangle=30,radius=1.5,center=(0.5,0.5),
                                          textprops={'fontsize':12},frame=False,pctdistance=.65)
          labels=sizes.index.unique()
          plt.gca().axis("equal")
          plt.title(data.columns[i],weight='bold',size=14)
          plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)

          #Se crean los archivos png
          plt.savefig('img/'+str(data.columns[i])+'.png', dpi=100,bbox_inches="tight")
          plt.cla()

  ## GRAFICOS
def estadistica():
  """
  
    Funcion encargada de la carga de las graficas previamente hechas.
  
  """
  st.markdown(
    '''
      <h3 style='color: #fff; text-align: center;'>
        ESTADISTICA
      </h6>
    '''
    ,unsafe_allow_html=True
  )

  #Columnas para las graficas: 3
  img1, img2, img3= st.columns(3)
  with img1:
    st.markdown('''<h5 style='color: #8A1E41; text-align: center;'>SEXO</h6>''',unsafe_allow_html=True)
    st.image("img/SEXO.png",caption='SEXO')
    st.markdown('''
      <p style='text-align: justify'>
        El 52.5% de la poblacion es del sexo masculino, y el resto del sexo femenino, con un porcentaje del 47.5%
      </p>
    ''',
    unsafe_allow_html=True
    )

  with img2:
    st.markdown('''<h5 style='color: #8A1E41; text-align: center;'>OBESIDAD</h5>''',unsafe_allow_html=True)
    st.image("img/OBESIDAD.png",caption='OBESIDAD')
    st.markdown('''
      <p style='text-align: justify'>
        Se cuenta que solo el 9.7% de la poblacion se encuentra en el estado de obesidad.
      </p>
    ''',
    unsafe_allow_html=True
    )

  with img3:
    st.markdown('''<h5 style='color: #8A1E41; text-align: center;'>DIABETES</h5>''',unsafe_allow_html=True)
    st.image("img/DIABETES.png",caption='DIABETES')
    st.markdown('''
      <p style='text-align: justify'>
        Los datos proporcinados por el gobierno federal marca que solo el 8.4% de la poblacion cuenta con diabetes.
      </p>
    ''',
    unsafe_allow_html=True
    )

  dataTable = pd.read_csv('municipios.csv')
  dataTable = dataTable.drop(columns=['code'])
  st.table(dataTable)

def footer():
  st.markdown("<hr>", unsafe_allow_html=True)
  st.image('img/info.jpg')


# Carga de las diferentes funciones
if __name__ == "__main__":
  main()
  generadorMultimedia()
  mapa()
  estadistica()
  footer()