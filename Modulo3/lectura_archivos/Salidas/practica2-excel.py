import pandas as pd
#cargar el archivop excel
df = pd.read_excel("../entradas/reporte_ventas.xlsx", sheet_name='Ventas2023') 
print(df.head())

df1 = pd.read_excel("../entradas/reporte_ventas.xlsx", sheet_name='Productos2023') 
print(df1.head())