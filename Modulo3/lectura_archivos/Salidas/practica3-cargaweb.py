import pandas as pd
#Cargar desde web
url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n"

tablas = pd.read_html(url)

#imprimir el numero de tablas
print(f"El numero de tablas encontradas: {len(tablas)}")

#imprimir primera tabla

df = tablas[0]
print(df.head())

#guardar la tabla en un excel 
df.to_excel("../salidas/poblacion.xlsx", index=False, )
df.to_csv("../salidas/poblacion.csv", index=False, )
