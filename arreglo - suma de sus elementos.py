"""
Crea un arreglo de números y calcula la suma de todos sus elementos.
"""

arreglo_num = []

numeros = 0

while numeros != 1: 
    numeros = int(input("Ingrese numeros (cuando ingrese 1 se acabara el ingreso de numeros): "))
    arreglo_num.append(numeros)
    
suma = 0

for x in arreglo_num:
    suma += x
    
print(suma)

