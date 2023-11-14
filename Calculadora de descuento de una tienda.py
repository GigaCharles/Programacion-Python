"""
CALCULADORA DE DESCUENTO DE UNA TIENDA
Desarrollar un programa que solicite al usuario ingresar el precio de un producto
y la cantidad que desea comprar. 
El programa debera calcular el descuento aplicable en funcion de la cantidad comprada:
10% de descuento si compra 10 o mas productos. 
Luego muestra el total sin descuento, el descuento aplicado y el total con descuento.
"""

precio=float(input("Ingrese el precio del producto: "))
cantidad=int(input("Ingrese cuantos productos llevara: "))

totalsindescuento = precio * cantidad
descuento = (totalsindescuento*10)/100
total = totalsindescuento - descuento

if(cantidad >=10):
    print("El subtotal es de: $",totalsindescuento, ",por su compra tiene un descuento de: $",descuento, 
          "por lo que tiene un total de: $",total, "a cancelar.")
elif(cantidad < 10):
    print("No tiene descuento por lo que su total es de: $",totalsindescuento)
    
    
    