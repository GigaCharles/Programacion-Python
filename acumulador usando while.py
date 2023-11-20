
numero = 1 
acumulador = 0
contador = 0
while numero != 0:
    numero = float(input("Ingrese numeros: "))
    acumulador += numero
    contador = contador + 1
print("La suma total de los numeros es: ", acumulador)
print("La cantidad de numeros ingresados es: ", contador)
