"""
Desarrollar un programa que calcule el maximo 
de tres numeros ingresados por el usuario.
"""

numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))

if(numero1 > numero2 and numero1 > numero3):
    print("El primer numero es el maximo")
else:
    if(numero2 > numero1 and numero2 > numero3):
        print("El segundo numero es el maximo")
    else:
        if(numero3 > numero1 and numero3 > numero2):
            print("El tercer numero es el maximo")
        else:
            print("Los tres numeros son iguales")
    
    
    
    
    