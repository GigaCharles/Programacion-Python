"""
Crea un arreglo de números y crea un nuevo arreglo que contenga los elementos en orden inverso.
"""

arreglo_num = []

numeros = 0

while numeros != 1:
    numeros = int(input("Ingrese numeros(cuando ingrese 1 se acabara el ingreso): "))
    arreglo_num.append(numeros)
    
arreglo_reves = arreglo_num[::-1]
    
print("Arreglo original: ", arreglo_num)
print("Ahora el arreglo al reves: ", arreglo_reves)

