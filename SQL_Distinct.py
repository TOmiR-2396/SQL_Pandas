import pandas as pd  

# SQL Distinct #

df = pd.read_csv("data.csv")

print(df[["First Name","City"]].drop_duplicates())