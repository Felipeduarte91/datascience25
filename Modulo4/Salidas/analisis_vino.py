import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#INSPECCION INICIAL
#carga de datos

df = pd.read_csv("../Entradas/winequality-red.csv")
print(df.head(10))
print(df.info())
print(df.describe())

#Medidas de tendencia central y dispersion

print("/n Medidas de tendencia central (ph): ")
print("pH", df['pH'].mean())
print("Mediana", df['pH'].median())
print("Moda", df['pH'].mode())

print("/n Estadisticas de dispersion (ph): ")
print("Rango", df['pH'].max())
print("Desviacion estandar", df['pH'].std())
print("Minimo", df['pH'].min())
print("Maximo", df['pH'].max())

print("/n Medidas de tendencia central (Alcohol): ")
print("Media", df['alcohol'].mean())
print("Mediana", df['alcohol'].median())
print("Moda", df['alcohol'].mode())

print("/n Estadisticas de dispersion (alcohol): ")
print("Rango", df['alcohol'].max())
print("Desviacion estandar", df['alcohol'].std())
print("Minimo", df['alcohol'].min())
print("Maximo", df['alcohol'].max())

print("/n Medidas de tendencia central (fixed acidity): ")
print("Media", df['fixed acidity'].mean())
print("Mediana", df['fixed acidity'].median())
print("Moda", df['fixed acidity'].mode())


print("/n Estadisticas de dispersion (fixed acidity): ")
print("Rango", df['fixed acidity'].max())
print("Desviacion estandar", df['fixed acidity'].std())
print("Minimo", df['fixed acidity'].min())
print("Maximo", df['fixed acidity'].max())

print("/n Medidas de tendencia central (volatile acidity): ")
print("Media", df['volatile acidity'].mean())
print("Mediana", df['volatile acidity'].median())
print("Moda", df['volatile acidity'].mode())

print("/n Estadisticas de dispersion (volatile acidity): ")
print("Rango", df['volatile acidity'].max())
print("Desviacion estandar", df['volatile acidity'].std())
print("Minimo", df['volatile acidity'].min())
print("Maximo", df['volatile acidity'].max())

print("/n Medidas de tendencia central (citric acid ): ")
print("Media", df['citric acid'].mean())
print("Mediana", df['citric acid'].median())
print("Moda", df['citric acid'].mode())

print("/n Estadisticas de dispersion (citric acid): ")
print("Rango", df['citric acid'].max())
print("Desviacion estandar", df['citric acid'].std())
print("Minimo", df['citric acid'].min())
print("Maximo", df['citric acid'].max())

#2. Limpieza de datos o Revisa si hay valores nulos en columnas como alcohol y pH. o Rellena con la mediana o elimina si hay pocos registros nulos.

print("Valores Faltantes", df.isnull().sum())
print("Filas Duplicadas", df.duplicated().sum())

df['alcohol'].fillna(df['alcohol'].median(), inplace=True)

#3. 3. Análisis univariado
#o Usa sns.histplot() para observar la distribución de quality.
#o Usa sns.boxplot() para detectar valores extremos en alcohol, pH, sulphates, etc.

#sns.histplot(df["quality"], kde=True)
#plt.title("Distribucion de Calidad")
#plt.xlabel("Calidad")
#plt.ylabel("Frecuencia")
#plt.show() 

#sns.boxplot(x=df["alcohol"])
#plt.title("Boxplot de alcohol")
#plt.xlabel("alcohol")
#plt.show() 

#sns.boxplot(x=df["pH"])
#plt.title("Boxplot de pH")
#plt.xlabel("pH")
#plt.show() 

#sns.boxplot(x=df["sulphates"])
#plt.title("Boxplot de sulphates")
#plt.xlabel("sulphates")
#plt.show() 

#sns.boxplot(x=df["fixed acidity"])
#plt.title("Boxplot de fixed acidity")
#plt.xlabel("fixed acidity")
#plt.show() 

#sns.boxplot(x=df["volatile acidity"])
#plt.title("Boxplot de volatile acidity")
#plt.xlabel("volatile acidity")
#plt.show() 

#sns.boxplot(x=df["residual sugar"])
#plt.title("Boxplot de residual sugar")
#plt.xlabel("residual sugar")
#plt.show() 

#sns.boxplot(x=df["chlorides"])
#plt.title("Boxplot de chlorides")
#plt.xlabel("chlorides")
#plt.show() 

#4. Detección de outliers
#o Aplica IQR a las variables químicas clave.
#o Justifica qué hacer con los valores extremos (corregir, eliminar o conservar).

#5. Análisis bivariado
# Genera un mapa de calor de correlación con sns.heatmap(corr_matrix, annot=True)
#para detectar variables más ligadas a quality.
# Calcular correlación
correlacion = df.corr()

# Graficar mapa de calor con anotaciones
sns.heatmap(correlacion, annot=True, cmap="coolwarm")
plt.title("Matriz de correlación")
plt.show()