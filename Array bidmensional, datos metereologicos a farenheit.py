
import numpy as np

# Crear el array bidimensional con los registros de temperatura y precipitación para cada día
registros = np.array([
    [29.5, 6.2],  # Día 1: Temperatura = 25.5°C, Precipitación = 10.2 mm
    [24.6, 9.5],   # Día 2: Temperatura = 24.0°C, Precipitación = 5.5 mm
    [30.8, 17.6],  # Día 3: Temperatura = 26.8°C, Precipitación = 15.0 mm
    [29.2, 5.0],   # Día 4: Temperatura = 23.2°C, Precipitación = 2.0 mm
    [26.9, 10.5],  # Día 5: Temperatura = 28.5°C, Precipitación = 20.5 mm
    [24.7, 8.1],   # Día 6: Temperatura = 22.7°C, Precipitación = 8.8 mm
    [23.4, 15.3]   # Día 7: Temperatura = 27.3°C, Precipitación = 12.3 mm
])

# Extraer las temperaturas originales del array
temperaturas_originales = registros[:, 0]

# Aplicar la conversión a grados Fahrenheit
temperatura_fahrenheit = temperaturas_originales * 9/5 + 32

# Crear el nuevo array bidimensional con las temperaturas en grados Fahrenheit
registros_fahrenheit = np.column_stack((temperatura_fahrenheit, registros[:, 1]))

print("DATOS METEREOLOGICOS EN GRADOS FARENHEIT:")
for i in range(registros_fahrenheit.shape[0]):
    dia = i + 1
    temperatura_f = registros_fahrenheit[i, 0]
    precipitacion = registros_fahrenheit[i, 1]
    print("Dia",dia,": , Temperatura = ", temperatura_f, "°C, Precipitacion =", precipitacion,"mm")
    
# Filtrar los días donde la temperatura supera los 25 grados Celsius
dias_calurosos_indices = np.where(registros[:, 0] > 25)[0]
dias_calurosos = registros[dias_calurosos_indices]

# Calcular la desviación estándar de las temperaturas
desviacion_estandar_temperaturas = np.std(registros[:, 0])

# Calcular la correlación entre la temperatura y la precipitación
correlacion_temperatura_precipitacion = np.corrcoef(registros[:, 0], registros[:, 1])[0, 1]

# Imprimir los resultados
print("Dias con temperatura superior a 25°C: ")
for i, dia in enumerate(dias_calurosos_indices, start=1):
    temperatura = registros[dia, 0]
    precipitacion = registros[dia, 1]
    print(f"Día {dia + 1}: Temperatura = {temperatura}°C")
print("Desviación estándar de las temperaturas: ", desviacion_estandar_temperaturas)
print("Correlación entre temperatura y precipitación: ", correlacion_temperatura_precipitacion)




