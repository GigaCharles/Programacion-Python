"""
Suma de Números Positivos: 
    Desarrolla un programa que solicite al usuario 
    ingresar números positivos hasta que ingrese un número negativo, 
    luego imprime la suma de los números positivos.
"""

contador = 0

numero = float(input("Ingrese numeros: "))

while numero >= 0:
    contador += numero
    numero = float(input("Ingrese numeros: "))
print("La suma de los numeros positivos es: ", contador)
