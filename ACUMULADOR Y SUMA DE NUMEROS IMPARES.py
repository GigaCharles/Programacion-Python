"""
ACUMULADOR DE SUMA DE NUMEROS IMPARES 
Desarrollar un programa que calcule la suma de todos los numeros impares 
en el rango de 1 a un numero dado.
Imprime la suma obtenida 
"""

#ACUMULADOR DE SUMA DE NUMEROS IMPARES

numero = 1
contador = 0
acumulador = 0
while numero != 0:
    numero = float(input("Ingrese un numero: "))
    if(numero % 2 != 0):
        contador += 1
        acumulador += numero
print("La suma total de los numeros impares ingresados es: ", acumulador)
print("La cantidad de numeros impares ingresados fueron: ", contador, "numeros")