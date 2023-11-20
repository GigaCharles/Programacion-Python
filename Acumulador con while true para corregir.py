

print("  ACUMULADOR")
suma = 0
contador = 1
multiplo_3 = 0
while True:
    numero = float(input("Ingrese numero: "))
    
    if(numero == 0): 
        suma += numero
        break
    contador += 1
    if(numero % 3 == 0):
        multiplo_3 += 1
print("La suma total de los numeros ingresados es: ",suma)
print("Los numeros que han sido ingresados son los siguientes: ", contador)
print("La cantidad de numeros que son divisibles entre 3 son los siguientes: ", multiplo_3)

#Hay un error en este codigo que debo corregir 