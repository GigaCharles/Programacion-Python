"""
CONTADOR DE NUMEROS PARES
Escribe un programa en python que cuente la cantidad de numeros pares 
ingresados por el usuario en el rango de 1 a un numero dado.
Imprime el resultado
"""

#CONTADOR DE NUMEROS PARES 
numero = 1
contador = 0
while numero != 0:
    numero = float(input("Ingrese un numero: "))
    if(numero % 2 == 0):
        contador += 1
print("La cantidad de numeros pares ingresados fueron: ", contador, "numeros")