"""
Escriba un programa que permita elegir entre tres productos (Leche, huevo y harina)
siendo los precios ($1.10, $4.50, $0.50) y que solicite:
    cantidad, nombre del producto y precio,
    si la cantidad del producto es mayor a 3, aplicar 10% de descuento.
    Permitir al usuario ingresar otro producto si desea y al finalizar mostrar el total.
"""
total = 0
opcion = "0"

while opcion != "4":

    print(" T I E N D A")
    print("1.- Leche -------------- $1.10")
    print("2.- Huevo -------------- $4.50")
    print("3.- Harina -------------- $0.50")
    print("4.- Salir")
    
    opcion = input("Ingrese la opcion: ")
    
    if (opcion == "1"):
        print("Ha escogido Leche")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        subtotal = cantidad * 1.10
        if cantidad > 3:
            print("¡TIENE UN 10% DE DESCUENTO EN SU COMPRA!")
            descuento = subtotal * 0.10
            total_condscto = subtotal - descuento
            print("El total de su compra con el dscto. realizado es de: $", total_condscto)
        else:
            print("Su total es de: $", subtotal)
        total += subtotal
    else:
        if (opcion == "2"):
            print("Ha escogido Huevos")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = cantidad * 4.50
            if cantidad > 3:
                print("¡TIENE UN 10% DE DESCUENTO EN SU COMPRA!")
                descuento = subtotal * 0.10
                total_condscto = subtotal - descuento
                print("El total de su compra con el dscto. realizado es de: $", total_condscto)
            else:
                print("Su total es de: $", subtotal)
            total += subtotal
        else:
            if (opcion == "3"):
                print("Ha escogido Harina")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                subtotal = cantidad * 0.50
                if cantidad > 3:
                    print("¡TIENE UN 10% DE DESCUENTO EN SU COMPRA!")
                    descuento = subtotal * 0.10
                    total_condscto = subtotal - descuento
                    print("El total de su compra con el dscto. realizado es de: $", total_condscto)
                else:
                    print("Su total es de: $", subtotal)
                total += subtotal
            else:
                if (opcion == "4"):
                    print("Ha finalizado su compra")
print("EL TOTAL DE SU COMPRA ES: $", total)
    
            
            
        
                            
   

