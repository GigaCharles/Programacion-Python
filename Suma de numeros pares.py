"""
Suma de Numeros Pares: 
    Desarrolla un programa que calcule la suma de los numeros pares 
    en el rango de 1 a 50 utilizando un bucle.
"""
contador = 0

for numero in range(1, 51):
    if numero % 2 == 0:
        contador += numero
print("La suma de los numeros pares en el rango de 1 a 50 es: ", contador)
        
        