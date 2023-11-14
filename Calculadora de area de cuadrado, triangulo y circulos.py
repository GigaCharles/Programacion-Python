
print("   CALCULO DE AREAS DE DIFERENTES FIGURAS GEOMETRICAS\n")

print("a) Ingrese 1 para calcular el area de un cuadrado")
print("b) Ingrese 2 para calcular el area de un triangulo")
print("c) Ingrese 3 para calcular el area de un circulo\n")

opcion = input( "Ingrese la opcion: ")

if(opcion == "1"):
    print("\nAREA DE UN CUADRADO")
    lado1 = float(input("Ingrese el lado: "))
    areac = lado1 * lado1
    print("\nFORMULA: lado * lado")
    print(lado1, "*", lado1, "=", areac)
else:
    if(opcion == "2"):
        print("\nAREA DE UN TRIANGULO")
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        areat = (base * altura)/2 
        print("\nFORMULA: (base * altura)/2")
        print("(",base, "*", altura, ")/2  =", areat)
    else:
        if(opcion == "3"):
            print("\nAREA DE UN CIRCULO")
            pi = 3.14
            radio = float(input("Ingrese el radio del circulo: "))
            areaci = pi * radio * radio
            print("\nFORMULA: π * r^2")
            print(pi, "* (", radio,")^2  =", areaci)


            