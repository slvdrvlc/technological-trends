# -*- coding: utf-8 -*-
"""Clase10RegresionLinealMultiple.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xu8G_sfJdNMxxCjCw0BD896eMa2Vs2dv

improtar las librerias necesarias para la regresion lineal multiple
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

from sklearn.model_selection import train_test_split #para dividir los datos
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

"""Subir datos y mostrar el dataset importado"""

dataset = pd.read_csv('salarios.csv')
print(dataset)

"""Crear una lista de paises para anexar posteriormente"""

paises = ['CO', 'MX', 'PE', 'BR', 'US'] 
print ('Fila paises (nueva)\n\n',paises)

"""Anexando pais ala dataset"""

dataset['Pais'] = [paises[np.random.randint(0,len(paises))] for i in range(len(dataset)) ]
dataset



dataset['IDPais'] = pd.factorize(dataset['Pais'])[0]
print (dataset)

"""dividir en x y la tabla de entrada"""

#Asigno valores para x,y
x = dataset[['Aexperiencia','IDPais']]
y = dataset['Salario']
print('\n\ncolumnas experiencia y idpaises\n\n',x)
print('\n\ncolumnas salarios\n\n',y)

"""creacion y division de datos de entrenamiento y prueba"""

X_Entrenamiento, X_Prueba, Y_Entrenamiento, Y_Prueba = train_test_split(x,y, test_size = 0.3, random_state=0)
print('\n\n x_entrenamiento\n\n',X_Entrenamiento)
print('\n\n x_prueba\n\n',X_Prueba)
print('\n\n y_entrenamiento\n\n',Y_Entrenamiento)
print('\n\n y_prueba\n\n',Y_Prueba)

"""Creando l regresion lineal multiple"""

regresionLinealMultiple=LinearRegression()
regresionLinealMultiple.fit(X_Entrenamiento, Y_Entrenamiento)

ajuste = regresionLinealMultiple.score(X_Prueba,Y_Prueba)
print('\nEl porcentaje de ajuste es: ', ajuste*100, '%\n')

#Grafico de los resultados de entrenamiento
fig = plt.figure(dpi=150)
Vista3d = fig.add_subplot(111, projection='3d')
Vista3d.scatter(X_Entrenamiento['Aexperiencia'], X_Entrenamiento['IDPais'], Y_Entrenamiento, color = 'blue', label = 'Entrenamiento')
Vista3d.scatter(X_Prueba['Aexperiencia'], X_Prueba['IDPais'], regresionLinealMultiple.predict(X_Prueba), color = 'red', label = 'Prueba')
Vista3d.plot_trisurf(X_Entrenamiento['Aexperiencia'],X_Entrenamiento['IDPais'], regresionLinealMultiple.predict(X_Entrenamiento),color = 'black', alpha = 0.5)
Vista3d.set_title('Salario, Experiencia y País')
Vista3d.set_xlabel('Experiencia (años)')
Vista3d.set_ylabel('País')
Vista3d.set_zlabel('Salario (USD)')
Vista3d.set_yticks(range(len(paises)))
Vista3d.set_yticklabels(paises)
plt.legend(loc="upper left") 
fig.show
