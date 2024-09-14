import pandas as pd  

# SQL Select Columns #

df = pd.read_csv("data.csv")

#Solo imprimir [["columna 1", "columna 2"]]
print(df[["First Name", "Last Name"]].head(10))