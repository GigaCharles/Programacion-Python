"""
escribir un programa que clasifique una pelicula en funcion de la edad
(niño, adolescente, o adulto) basado en la edad ingresada por el usuario
"""

edad=int(input("Ingrese la edad: "))

if(edad < 12):
    print("El individuo puede ver una pelicula apto solo para niños")
else:
    if(edad > 12 and edad <= 17):
        print("El individuo puede ver una pelicula apta para adolescentes")
    else:
        print("El individuo puede ver una pelicula apta para adultos")
    
    
    