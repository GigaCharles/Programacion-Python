"""
Utilizar while para calcular un numero "n" elevado a una potencia
"""

base = int(input("Ingrese una base: "))
exponente = int(input("Ingrese un exponente: "))

contador = 0
acumulador = 1

while contador < exponente:
    acumulador = acumulador * base
    contador += 1
print(acumulador)

