# Inicio do modulo novo

# Séra importante para o modulo novo: Pandas, dataframe, series, arrays, numpy, aprender sobre bibliotecas de python, aprender sobre pandas, aprender sobre numpy, aprender sobre arrays, aprender sobre series, aprender sobre dataframes, aprender sobre bibliotecas de python, aprender sobre pandas e numpy, aprender sobre pandas e arrays, aprender sobre pandas e series, aprender sobre pandas e dataframes, aprender sobre numpy e arrays, aprender sobre numpy e series, aprender sobre numpy e dataframes, aprender sobre arrays e series, aprender sobre arrays e dataframes, aprender sobre series e dataframes

# py global
#ETL e PIPLINE
#Power BI
# Criar o habito de ativar o venv e aprender a usa-lo

# pip install: para instalar bibliotecas
# aprender o apelido de bibliotecas


import pandas as pd #alias 'pd' para pandas
import numpy as np #alias 'np' para numpy

numeros_impares = [43, 55, 1 ,3 , 11, 27, 109]
numeros_seq = [2,3,4,5,6,7]
print(type(numeros_impares))

serie_impares = pd.Series(numeros_impares)
print(serie_impares)

print((serie_impares.sum()))
print((serie_impares.mean()))
print((serie_impares.max()))
print((serie_impares.min()))
print(len(serie_impares))
print(serie_impares.describe())

series2_imopares = pd.Series(
    numeros_impares, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(series2_imopares)