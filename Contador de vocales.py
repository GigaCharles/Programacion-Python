"""
Contador de Vocales: 
    Desarrolla un programa que solicite al usuario ingresar una frase 
    y luego cuente e imprima la cantidad de vocales presentes en la frase.
"""

frase = input("Ingrese una frase: ")

vocales = ("aeiouAEIOU")

contador = 0

for x in frase:
    if x in vocales:
         contador = contador + 1
print("La cantidad de vocales presentes en la frase es: ", contador)


    