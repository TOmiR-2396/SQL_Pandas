import pandas as pd  

# SQL IN() #

df = pd.read_csv("data.csv")

#Lista de nombres que quiero buscar

names = ['Alejandro', 'Heather', 'Hiroko']

#Filtrado segun lista

print(df[df["First Name"].isin(names)])