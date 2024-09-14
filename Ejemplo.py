import pandas as pd  

# EJEMPLO #

# Read the CSV file
df = pd.read_csv("data.csv")

# Filter people whose salary is higher than 58000
high_salary = df[df['Salary'] > 58000]

# Print the names of people with a salary higher than 58000
print(high_salary['Name'])

# Eliminar las columnas deseadas (reemplaza 'columna1' y 'columna2' por los nombres reales de tus columnas)
df = df.drop(['Customer Id'], axis=1)

# Guardar el archivo modificado (opcional)
df.to_csv('data.csv', index=False)
