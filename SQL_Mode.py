import pandas as pd  

# SQL Mode #

df = pd.read_csv("data.csv")


print(df['Age'].mode())