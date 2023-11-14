"""
Sumar, restar, multiplicar y dividir segun el numero de opcion que escoja el usuario
"""

print("C A L C U L A D O R A")

print("Presione 1 para realizar una suma")
print("Presione 2 para realizar una resta")
print("Presione 3 para realizar una multiplicacion")
print("Presione 4 para realizar una division")

opcion=input("Ingrese el dato: ")

if(opcion == "1"):
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    suma = num1 + num2
    print(num1, "+", num2, "=", suma)
else:
    if(opcion == "2"):
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resta = num1 - num2
        print(num1, "-", num2, "=", resta)
    else:
        if(opcion == "3"):
            num1 = int(input("Ingrese el primer numero: "))
            num2 = int(input("Ingrese le segundo numero: "))
            multiplicacion = num1 * num2
            print(num1, "*", num2, "=", multiplicacion)
        else:
            if(opcion == "4"):
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                division = num1 / num2
                print(num1, "/", num2, "=", division)
                
             