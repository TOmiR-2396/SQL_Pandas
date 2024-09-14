import pandas as pd  

# SQL Group by Sum() #

df = pd.read_csv("data.csv")

#Ordenar paises segun la suma de salarios mas grande

SumaSalarios = df.groupby('Country').agg({'Income': 'sum'})

# Ordenar de menor a mayor o viceversa ascending=True/False

SumaSalariosOrdenada = SumaSalarios.sort_values(by='Income', ascending=False)

print(SumaSalariosOrdenada)