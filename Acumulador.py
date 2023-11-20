"""
Acumulador
Contador

Crear un programa que permita el ingreso de "n" numeros y vaya acumulando la 
suma de los mismos, hasta que el usuario ingrese 0.
Al finalizar se debe mostrar la suma total de los mismos
"""
print("  ACUMULADOR")
suma = 0

while True:
    numero = float(input("Ingrese numero: "))
    
    if(numero == 0):
        break
    suma += numero
print("La suma total de los numeros ingresados es: ",suma)

