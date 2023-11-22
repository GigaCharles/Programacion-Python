"""
Clasificación de Edades: 
    Crea un programa que solicite la edad del usuario y 
    luego imprima si es un niño, adolescente, adulto o anciano.
"""

edad = int(input("Ingrese edad del usuario: "))

if edad <= 12:
    print("Es un niño")
else:
    if edad > 12 and edad < 18:
        print("Es un adolescente")
    else:
        if edad >=18 and edad < 65:
            print("Es un adulto")
        else:
            print("Es un anciano")
            
            
