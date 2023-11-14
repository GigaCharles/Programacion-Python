"""
Crear un programa que verifique si un a–o es bisiesto o no
"""

año=int(input("Ingrese el año: "))

if(año % 4 == 0 and año % 100 != 0) or (año % 100 == 0 and año % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
    
    
    