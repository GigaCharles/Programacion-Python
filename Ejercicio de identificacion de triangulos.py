lado_1=float(input("Ingrese el primer lado del triangulo: "))
lado_2=float(input("Ingrese el segundo lado del triangulo: "))
lado_3=float(input("Ingrese le tercer lado del triangulo: "))

if lado_1==lado_2==lado_3:
    print("Es un triangulo equilatero")
elif lado_1==lado_2 or lado_1==lado_3 or lado_2==lado_3:
    print("Esun triangulo isosceles")
else:
    print("El triangulo es escaleno")
    