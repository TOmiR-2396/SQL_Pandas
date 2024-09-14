import pandas as pd  

# SQL Mode #

df = pd.read_csv("data.csv")

# Edad que mas se repite

print(df['Age'].mode())