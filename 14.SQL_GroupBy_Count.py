import pandas as pd  

# SQL Group by Count() #

df = pd.read_csv("data.csv")

#Ordenar segun la mayor cantidad de usuarios por pais

CantidadUsuariosPorPais = df.groupby('Country').agg({'Index': 'count'})

# Ordenar de menor a mayor o viceversa ascending=True/False

CantidadUsuariosPorPaisOrdenada = CantidadUsuariosPorPais.sort_values(by='Index', ascending=False)

print(CantidadUsuariosPorPaisOrdenada)