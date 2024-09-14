import pandas as pd  

# SQL Group by Avg() #

df = pd.read_csv("data.csv")

#Ordenar paises segun el promedio de edad mas grande

PromedioEdad = df.groupby('Country').agg({'Age': 'mean'})

# Ordenar de menor a mayor o viceversa ascending=True/False

PromedioEdadOrdenada = PromedioEdad.sort_values(by='Age', ascending=False)

print(PromedioEdadOrdenada)