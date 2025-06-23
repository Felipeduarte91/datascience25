#Crear un DataFrame de datos de desempeño de empleados con índices personalizados (IDs de empleados). 
# Filtrar empleados con puntajes de desempeño altos (>80) en departamentos específicos (Ventas o Marketing). 
# Calcular el puntaje promedio por departamento e identificar calificaciones únicas de desempeño. Mostrar columnas específicas para los empleados filtrados y sus detalles.

import pandas as pd

data = {
    'Nombre': ['Pédro', 'Alejandra', 'Alicia', 'Juan'], 'Departamento': ['Ventas', 'Marketing', 'TI', 'Ventas' ] , 'Puntaje': [86, 96, 65, 45],'Calificacion': ['A', 'A', 'C', 'D']
                                                                         }
data = pd.DataFrame(data, index= ['A1', 'A2', 'A3', 'A4'])
print(data)
           

        
