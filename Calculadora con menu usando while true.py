"""
Escribe un programa en Python que funcione como un conversor de unidades. 
El programa deberá presentar un menú interactivo con las siguientes opciones:
 - Convertir de metros a pies
 - Convertir de pies a metros
 - Convertir de kilogramos a libras
 - Convertir de libras a kilogramos
 - Salir
Cuando el usuario elija una opción (1-4), el programa solicitará un valor 
correspondiente a la unidad de medida seleccionada y mostrará el resultado 
de la conversión. El programa continuará ejecutándose hasta que el usuario 
seleccione la opción 5 (Salir).
"""
while True:
    print("\n C O N V E R S O R  D E  U N I D A D E S")
    print("1.- Convertir de metros(m) a pies(ft) ")
    print("2.- Convertir de pies(ft) a metros(m)")
    print("3.- Convertir de kilogramos(kg) a libras(lb)")
    print("4.- Conmvertir de libras(lb) a kilogramos(kg)")
    print("5.- Salir")
    
    opcion = input("Ingrese una opcion: ")
    
    if(opcion == "1"):
        metro = float(input("Ingrese la cantidad en metros: "))
        pies = metro * 3.28
        print("Son", pies, "(ft)")
    else:
        if(opcion == "2"): 
            pies = float(input("Ingrese la cantidad en pies: "))
            metro = pies / 3.28
            print("Son", metro, "(m)")
        else:
            if(opcion == "3"):
                kilo = float(input("Ingrese la cantidad en Kilogramos: "))
                libra = kilo * 2.205
                print("Son", libra, "(lb)")
            else:
                if(opcion == "4"):
                    libra = float(input("Ingrese la cantidad en libras: "))
                    kilo = libra / 2.205
                    print("Son", kilo, "(kg)")
                else:
                    if(opcion == "5"):
                        print("¡Vuelva pronto!")
                        break
                    else:
                        print("La opcion ingresada es incorrecta")
   
                    
                