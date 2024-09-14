import pandas as pd  

# SQL Average #

df = pd.read_csv("data.csv")

# Convertir la columna 'Subscription Date' a tipo datetime

df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])

#Buscar promedio de fecha de subscripcion

print(df['Subscription Date'].mean())
