import pandas as pd  
import numpy as np

# EJEMPLOS #

# Read the CSV file
df = pd.read_csv("data.csv")

# Filter people whose salary is higher than 58000
# high_salary = df[df['Salary'] > 58000]

# Print the names of people with a salary higher than 58000
# print(high_salary['Name'])

# Eliminar las columnas deseadas (reemplaza 'columna1' y 'columna2' por los nombres reales de tus columnas)
# df = df.drop(['Customer Id'], axis=1)

#df['Subscription Date'] = pd.to_datetime(df['Subscription Date'])

# Crear columna de "Age" con valores random
# np.random.seed(0)  
# df['Age'] = np.random.randint(20, 70, size=len(df))

# Renombrar la columna 'Phone 1' a 'Phone'
# df.rename(columns={'Phone 1': 'Phone'}, inplace=True)

#new_order = ['Index', 'First Name', 'Last Name', 'Age', 'Company', 'City', 'Country', 'Phone', 'Email', 'Subscription Date']

# Reordenar las columnas
#df = df[new_order]

# Guardar el archivo modificado (opcional)
df.to_csv('data.csv', index=False)
