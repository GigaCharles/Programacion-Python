"""
Calculadora de Factorial:

Solicita al usuario que ingrese un número.
Utiliza un bucle para calcular el factorial del número ingresado.
Imprime el resultado.
"""

numero = int(input("Ingrese un numero: "))
factorial = numero
for x in range(1, numero):
    factorial *= x
print("El factorial del numero ingresado es: ", factorial)
