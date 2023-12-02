"""
Hacer  un algoritmo que genere los N primeros numeros multiplos de 5.
Validar que N sea positivo
"""

numero = int(input("Ingrese un numero: "))

if numero < 0:
    print("ERROR")
else:
    contador = 1
    while numero > 0:
        multiplo_5 = contador * 5 
        print(multiplo_5)
        contador += 1
        numero -= 1