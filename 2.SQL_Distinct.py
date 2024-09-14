import pandas as pd  

# SQL Distinct #

df = pd.read_csv("data.csv")

#Imprimir sin repetidos

print(df[["First Name","City"]].drop_duplicates())