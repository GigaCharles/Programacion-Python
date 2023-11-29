"""
Verificador de Palíndromos:

Solicita al usuario que ingrese una palabra.
Verifica si la palabra es un palíndromo 
(se lee igual de izquierda a derecha que de derecha a izquierda) 
y muestra el resultado.
"""

palabra = input("Ingrese una palabra: ") 

palabra = palabra.lower()

palindromo = palabra == palabra[::-1]

if palindromo:
    print("Es un palindromo")
else:
    print("No es un palindromo")
    
    
