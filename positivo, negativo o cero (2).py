"""
Escribir un programa que determine si un numero
es positivo, negativo o cero
"""
caracter=float(input("Ingrese el numero: "))

if(caracter>0):
    print("Es un numero digitado es positivo")
else:
    if(caracter<0):
        print("El numero digitado es negativo")
    else:
        print("El numero digitado es 0")
    