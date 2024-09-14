import pandas as pd  

# SQL Joins #

df1 = pd.read_csv("joinPractice_1.csv")
df2 = pd.read_csv("joinPractice_2.csv")


joinedTables = pd.merge(df1,df2, how="inner", on="Name") 

print(joinedTables)
