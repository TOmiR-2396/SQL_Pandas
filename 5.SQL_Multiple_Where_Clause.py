import pandas as pd  

# SQL Multiple Where Clauses #

df = pd.read_csv("data.csv")

#Uso de clausula Where donde "First Name" = "Julie" y "Email" termina en ".com"

filtered_df = df[(df['First Name'] == 'Julie') & (df['Email'].str.endswith('.com'))]

# Seleccionar solo las columnas de  "First Name" y de "Email"

filtered_df = filtered_df[['First Name', 'Email']]

print(filtered_df)