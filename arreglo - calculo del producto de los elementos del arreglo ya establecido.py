"""
Crea un arreglo de números y calcula el producto de todos sus elementos.
"""

arreglo_num = [2,4,6,8,10]

producto = 1

for x in arreglo_num:
    producto *= x
    
print("Arreglo: ", arreglo_num)
print("El producto de los elementos de este arreglo es: ", producto)

