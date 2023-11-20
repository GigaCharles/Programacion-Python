"""
CONTADOR DE VOCALES DE UNA CADENA
Crear un programa en python que cuente la cantidad de vocales (a,e,i,o,u)
en una cadena dada (por ejemplo: Python es un lenguaje de programacion)
Imprime el numero total de vocales encontradas en la cadena
"""

#CONTADOR DE VOCALES

print("\n CONTADOR DE VOCALES")

cadena = input("Ingrese una oracion: ")

contador = 0
vocales = ("aeiouAEIOU")

for x in cadena:
    if  x in vocales:
        contador += 1
print("El numero de vocales que contiene la oracion ingresada es: ", contador)

