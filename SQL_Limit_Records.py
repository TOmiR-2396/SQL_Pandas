import pandas as pd  

# SQL Limit Records #

df = pd.read_csv("data.csv")

#Solo imprimir primeras 'n' filas
print(df.head(15))