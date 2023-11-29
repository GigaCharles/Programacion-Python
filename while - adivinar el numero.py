"""
Adivina el Número:

Genera un número aleatorio entre 1 y 100.
Pide al usuario que adivine el número.
Proporciona pistas si el número es mayor o menor.
Continúa hasta que el usuario adivine correctamente.
"""

numero_aleatorio = 15 

numero = int(input("Adivine el numero: "))

while numero != 15:
    numero = int(input("Ingrese nuevamente el numero: "))
    if numero > 15 and numero < 25:
        print("Estas cerca")
else:
    print("ADIVINASTE")
    
    