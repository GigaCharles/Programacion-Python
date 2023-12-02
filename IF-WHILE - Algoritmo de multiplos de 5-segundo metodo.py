"""
Hacer  un algoritmo que genere los N primeros numeros multiplos de 5.
Validar que N sea positivo
"""

numero = int(input("Ingrese un numero: "))

contador = 1

if numero > 0:
    while contador <= numero:
        multiplo = contador * 5
        contador += 1
        print(multiplo)
else:
    print("ERROR -> INGRESE UN NUMERO POSITVO")