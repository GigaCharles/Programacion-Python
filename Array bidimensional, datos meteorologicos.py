

import numpy as np

# Se crea el array bidimensional con los registros de temperatura y precipitación para cada día de la semana
registros = np.array([
    [29.5, 6.2],   # Día 1: Temperatura = 29.5°C, Precipitación = 6.2 mm
    [24.6, 9.5],   # Día 2: Temperatura = 24.6°C, Precipitación = 9.5 mm
    [30.8, 17.6],  # Día 3: Temperatura = 30.8°C, Precipitación = 17.6 mm
    [29.2, 5.0],   # Día 4: Temperatura = 29.2°C, Precipitación = 5.0 mm
    [26.9, 10.5],  # Día 5: Temperatura = 26.9°C, Precipitación = 10.5 mm
    [24.7, 8.1],   # Día 6: Temperatura = 24.7°C, Precipitación = 8.1 mm
    [23.4, 15.3]   # Día 7: Temperatura = 23.4°C, Precipitación = 15.3 mm
])

# Imprimir el array bidimensional
print("D A T O S  M E T E O R O L Ó G I C O S:")
for i in range(registros.shape[0]):
    dia = i + 1
    temperatura = registros[i, 0]
    precipitacion = registros[i, 1]
    print("Dia",dia,": , Temperatura = ", temperatura, "°C, Precipitacion =", precipitacion,"mm")

# Calcular la temperatura media y la precipitación total
temperatura_media = np.mean(registros[:, 0])
precipitacion_total = np.sum(registros[:, 1])

# Encontrar el día con la temperatura máxima y el día con la precipitación mínima
dia_temperatura_maxima = np.argmax(registros[:, 0]) + 1
dia_precipitacion_minima = np.argmin(registros[:, 1]) + 1

# Imprimir los resultados
print("TEMPERATURA MEDIA: ", temperatura,"°C")
print("PRECIPITACION TOTAL: ", precipitacion_total,"mm")
print("DIA CON TEMPERATURA MAXIMA: Dia", dia_temperatura_maxima)
print("DIA CON TEMPERATURA MINIMA: Dia", dia_precipitacion_minima)








