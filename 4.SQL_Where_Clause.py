import pandas as pd  

# SQL Where Clause #

df = pd.read_csv("data.csv")

#Uso de clausula Where donde "First Name" = "Julie"

print(df[df['First Name'] == 'Julie'])