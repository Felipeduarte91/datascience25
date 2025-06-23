import pandas as pd

# Cargar el archivo CSV
#df = pd.read_csv("../entradas/estudiantes.csv", sep=";")
#print(df)

#cargar archivo csv ventas
#df = pd.read_csv("../entradas/ventas.csv", na_values="N/A")
#df = df.dropna()
#print(df)

#Crear archivo CSV 

data = {"Producto": ["Manzana", "Banana"], "Precio": [0.5, 0.3]}
df = pd.DataFrame(data)
df.to_csv("../entradas/productos.csv", index=False, sep=",")
print(df)