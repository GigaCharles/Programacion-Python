"""
Crear un programa que verifique si un a�o es bisiesto o no
"""

a�o=int(input("Ingrese el a�o: "))

if(a�o % 4 == 0 and a�o % 100 != 0) or (a�o % 100 == 0 and a�o % 400 == 0):
    print("Es un a�o bisiesto")
else:
    print("No es un a�o bisiesto")
    
    
    