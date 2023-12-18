"""
Hacer un programa que permita el ingreso de numeros en un arreglo,
luego sacar el promedio de todos ellos y mostrarlo
"""
def suma (num_1, num_2, num_3, num_4, num_5):
    respuesta = num_1 + num_2 + num_3 + num_4 + num_5
    return respuesta

numeros = []

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))
num_3 = int(input("Ingrese otro numero: "))
num_4 = int(input("Ingrese otro numero: "))
num_5 = int(input("Ingrese un ultimo numero: "))

numeros.append(num_1)
numeros.append(num_2)
numeros.append(num_3)
numeros.append(num_4)
numeros.append(num_5)   

promedio = suma(num_1, num_2, num_3, num_4, num_5) / 5

print("El promedio de", numeros, "es igual a: ", promedio)


