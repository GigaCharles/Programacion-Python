"""
Contador de Números Pares e Impares:

Solicita al usuario que ingrese un número.
Utiliza un bucle para contar y mostrar la cantidad de números pares e impares desde 1 hasta el número ingresado.
"""

numero = int(input("Ingrese un numero: "))

contador_pares = 0
contador_impares = 0

for x in range(1, numero +1):
    if x % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
print("La suma de los numeros pares es igual a: ", contador_pares)
print("La suma de los numeros impares es igual a: ", contador_impares)


        

        