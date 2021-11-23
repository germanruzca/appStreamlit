from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
import pickle
from web import confu

## cargar los datos 

data = pd.read_csv('data/210510COVID19MEXICO.csv')

data = data.drop(columns=['SECTOR','ENTIDAD_UM','INTUBADO','ENTIDAD_NAC','ENTIDAD_RES','MUNICIPIO_RES', 'TIPO_PACIENTE','FECHA_INGRESO','FECHA_SINTOMAS','FECHA_DEF','NACIONALIDAD','EMBARAZO','HABLA_LENGUA_INDIG','INDIGENA', 'OTRA_COM','TOMA_MUESTRA_LAB','TOMA_MUESTRA_ANTIGENO','RESULTADO_LAB','ID_REGISTRO','MIGRANTE','PAIS_NACIONALIDAD','PAIS_ORIGEN','UCI','FECHA_ACTUALIZACION','ORIGEN','RESULTADO_ANTIGENO','OTRO_CASO'])

for i in range(data.shape[1]):
    if(data.columns[i]!='EDAD' and data.columns[i]!='CLASIFICACION_FINAL'):
        data = data.query(f"{data.columns[i]}==1 or {data.columns[i]}==2")

for i in range(data.shape[1]):
    if(data.columns[i]=='CLASIFICACION_FINAL'):
        data = data.query(f"{data.columns[i]}==3 or {data.columns[i]}==7")

for i in range(data.shape[1]):
    if(data.columns[i]!='EDAD' and data.columns[i]!='CLASIFICACION_FINAL'):
        convertion = {
            data.columns[i]:{
                1:1,
                2:0
            }
        }
    data.replace(convertion, inplace=True)
## 0 es hombre
## 1 es mujer
## 1 es si, 0 es no

for i in range(data.shape[1]):
    if(data.columns[i]=='CLASIFICACION_FINAL'):
        convertion = {
            data.columns[i]:{
                3:1,
                7:0
            }
        }
    data.replace(convertion, inplace=True)

X = data
y = data.pop('CLASIFICACION_FINAL')

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr', random_state=42)
model.fit(x_train, y_train)

confu(y_train,y_test)
print('s')


#lin_reg = LinearRegression()

# Entrenar el modelo

#lin_regr = lin_reg.fit(x_train, y_train)

with open('loc_reg.pkl', 'wb') as li:
    pickle.dump(model, li)