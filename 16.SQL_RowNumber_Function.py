import pandas as pd  

# SQL Multiple Aggregates #

df = pd.read_csv("data.csv")


df["rn"] = df.sort_values(["First Name", "Age"]).groupby("Country").cumcount() + 1

print(df.sort_values(by="Age").head())