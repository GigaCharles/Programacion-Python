"""
 Tabla de Multiplicar: 
     Escribe un programa que solicite al usuario un número e imprima 
     la tabla de multiplicar de ese número del 1 al 10.
"""

num = int(input("Ingrese el numero: "))

contador = 1

while contador <=10:
    print(contador, "x", num, "=", contador*num)
    contador = contador + 1
   
    
    