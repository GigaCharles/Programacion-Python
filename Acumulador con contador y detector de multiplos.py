numero = 1
acumulador = 0
contador = 0
multiplo = 0
while numero != 0:
    numero = float(input("Ingrese numeros: "))
    acumulador += numero
    contador = contador + 1 
    if(numero % 3 == 0 != numero > 0):
        multiplo += 1 
print("La suma total de los numeros es: ", acumulador)
print("La cantidad de numeros ingresados es: ", contador)
print("La cantidad de numeros quen son multiplos de 3 son: ", multiplo)
