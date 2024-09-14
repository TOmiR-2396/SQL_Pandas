import pandas as pd  

# SQL Multiple Aggregates #

df = pd.read_csv("data.csv")

#Para cada Company, se calcula promedio de edad y suma de ingresos de la misma

EstadisticaEmpresa = df.groupby('Company', dropna=False).agg({'Age': 'mean', 'Income': 'sum'})

# Ordenar de menor a mayor o viceversa ascending=True/False

EstadisticaEmpresaOrdenada = EstadisticaEmpresa.sort_values(by='Income', ascending=False)

print(EstadisticaEmpresaOrdenada)

# Nota1:En caso de tener doble agg, hay que elgir un criterio de orden 
# (en este caso puede ser por promedio de edad o por suma total de salario)

# Nota2: "dropna=False" <--- True: Elimina Nulls / False: no los elimina