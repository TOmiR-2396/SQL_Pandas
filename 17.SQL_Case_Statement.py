import pandas as pd  

# SQL Case Statemente #

df = pd.read_csv("data.csv")

def filtroEdad (age):
    if age <= 30:
        return "Young"
    elif age <= 50:
        return "Grown up"
    elif age < 65:
        return "Old"
    else:
        return "out of range"
    
df["Social Group"] = df["Age"].apply(lambda x: filtroEdad(x))

print(df.head(20))
