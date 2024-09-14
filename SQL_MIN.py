import pandas as pd  

# SQL MIN #

df = pd.read_csv("data.csv")

# Busqueda fecha de subscripcion mas antigua

print(df['Subscription Date'].min())