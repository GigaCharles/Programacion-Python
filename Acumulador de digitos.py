"""
Acumulador de Dígitos:
    Crea un programa que solicite al usuario ingresar un número
    y luego imprima la suma de sus dígitos.
"""

numero = input("Ingrese numeros: ")

acumulador = 0

for x in numero:
    digito = int(x)
    acumulador = acumulador + digito
print("La suma de los digitos del numero ingresado es: ", acumulador)


