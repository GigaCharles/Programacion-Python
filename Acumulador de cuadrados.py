"""
Acumulador de Cuadrados: 
    Escribe un programa que solicite al usuario ingresar 
    cinco números y luego imprima la suma de los cuadrados de esos números.
"""

suma_cuad = 0

for x in range(5):
    numero = int(input("Ingresa los numeros: "))
    suma_cuad = suma_cuad + numero * numero
print("La suma de los cuadrados es:", suma_cuad)

