"""
Desarrolla un programa en Python que simule una calculadora simple. 
El programa debe presentar un menú interactivo con las siguientes opciones:
 - Sumar
 - Restar
 - Multiplicar
 - Dividir
 - Salir
El usuario podrá seleccionar una opción ingresando el número correspondiente. 
En caso de seleccionar una operación matemática (opciones 1-4), el programa 
solicitará dos números al usuario y mostrará el resultado de la operación. 
El programa continuará ejecutándose hasta que el usuario elija la opción 5 (Salir).
"""

while True:
    print("\n C A L C U L A D O R A")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir") 

    opcion = input("Ingrese una opcion del 1 al 5: ")
    
    if (opcion == "5"):
        print("¡Vuelva pronto!")
        break
    else:
        if(opcion == "1"):
            num1 = float(input("Ingrese primer numero: "))
            num2 = float(input("Ingrese segundo numero: "))
            resultado = num1 + num2
            print(num1, "+", num2, "=", resultado)
        else:
            if(opcion == "2"):
                num1 = float(input("Ingrese primer numero: "))
                num2 = float(input("Ingrese segundo numero: "))
                resultado = num1 - num2
                print(num1, "-", num2, "=", resultado)
            else:
                if(opcion == "3"):
                    num1 = float(input("Ingrese primer numero: "))
                    num2 = float(input("Ingrese segundo numero: "))
                    resultado = num1 * num2
                    print(num1, "x", num2, "=", resultado)
                else:
                    if(opcion == "4"):
                        num1 = float(input("Ingrese primer numero: "))
                        num2 = float(input("Ingrese segundo numero: "))
                        resultado = num1 / num2
                        print(num1, "/", num2, "=", resultado)
                    else:
                        print("La opcion ingresada es incorrecta")
                        
                        
                        
                        
                        
                    
    
                        

                
    