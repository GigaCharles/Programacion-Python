"""
Crea un arreglo de números y calcula el producto de todos sus elementos.
"""

arreglo_num = []

numeros = 0

while numeros != 1:
    numeros = int(input("Ingrese numeros (cuando ingrese 1 se acabara el ingreso de los numeros): "))
    arreglo_num.append(numeros)
    
producto = 1

for x in arreglo_num:
    producto *= x 
    
print("El producto de todos los elementos ingresados es: ", producto)

