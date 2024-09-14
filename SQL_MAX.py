import pandas as pd  

# SQL MAX #

df = pd.read_csv("data.csv")

# Busqueda fecha de subscripcion mas nueva

print(df['Subscription Date'].max())