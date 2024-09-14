import pandas as pd  

# SQL NOT_IN() #

df = pd.read_csv("data.csv")

#Lista de nombres que quiero buscar

names = ['Fernando', 'Andrew', 'Julie']

#Filtrado segun lista. Negacion con " ~ "

print(df[~df["First Name"].isin(names)].head())