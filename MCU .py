
import numpy as np
import matplotlib.pyplot as plt

# Primero definimos una funcion que calcule la frecuencia, velocidad angular,
# velocidad tangencial y la aceleracion centripeta a partir del ingreso de las
# revoluciones por minuto y el radio ingresado
def calculo_a_partir_de_rpm (rpm, radio):
    frecuencia = rpm / 60
    vel_angular = 2 * np.pi *frecuencia
    vel_tang = vel_angular * radio
    acel_centripeta = vel_tang * vel_angular
    return (frecuencia, vel_angular, vel_tang, acel_centripeta)

# Segundo, definimos una funcion que calcule la frecuencia a partir del ingreso
# de las revoluciones por minuto
def calculo_frecuencia(rpm):
    frecuencia = rpm / 60
    return frecuencia

# Tercero, definimos una funcion que calcule la velocidad angular a partir 
# del ingreso de la frecuencia
def calculo_vel_angular(frecuencia):
    vel_angular = 2 * np.pi * frecuencia
    return vel_angular

# Cuarto, definimos una funcions que calcule la velocidad tangencial a partir
# del ingreso de la velocidad angular y el radio 
def calculo_vel_tangencial(vel_angular, radio):
    vel_tangencial = vel_angular * radio
    return vel_tangencial

# Quinto, definimos una funcion que calcule la aceleracion centripeta a partir 
# del ingreso de la velocidad tangencial y de la velocidad angular
def calculo_acel_centripeta(vel_tangencial, vel_angular):
    acel_centripeta = vel_tangencial * vel_angular
    return acel_centripeta

# Sexto, definimos un bucle en el cual van a estar incluido el menu y las 
# diversas opciones que definimos en las funciones anteriores

while True:
    
    print("\nMOVIMIENTO CIRCULAR UNFORME")
    print("\n1.- Calcular frecuencia")
    print("2.- Calcular velocidad angular")
    print("3.- Calcular velocidad tangencial")
    print("4.- Calcular aceleracion centripeta")
    print("5.- Calcular todo lo anterior (necesario rpm y radio)")
    print("6.- Salir")
    
    opcion = input("\nIgrese una opcion: ")
    
    # Aqui se hacen los calculos para hallar la frecuencia llamando a la funcion que definimos anteriormente
    if opcion == "1":
        print("\nCALCULO DE FRECUENCIA EN M. C. U.")
        ingresar_rpm = float(input("Ingresar rpm (revoluciones por minuto): "))
        frecuencia = calculo_frecuencia(ingresar_rpm)
        print("La frecuencia es: ", frecuencia,"c/s (ciclos/segundo)")
    
    # Aqui se hacen los calculos para hallar la velocidad angular llamando a la funcion que definimos anteriormente
    elif opcion == "2":
        print("\nCALCULO DE VELOCIDAD ANGULAR EN M. C. U.")
        ingresar_frecuencia = float(input("Ingresar frecuencia: "))
        vel_angular = calculo_vel_angular(ingresar_frecuencia)
        print("La velocidad angular es: ", vel_angular, "rad/s")
    
    # Aqui se hacen los calculos para hallar la velocidad tangencial llamando a la funcion que definimos anteriormente
    elif opcion == "3":
        print("\nCALCULO DE VELOCIDAD TANGENCIAL EN M. C. U.")
        ingresar_vel_angular = float(input("Ingrese velocidad angular: "))
        ingresar_radio = float(input("Ingrese el radio del movimiento (en centimetros): "))
        vel_tangencial = calculo_vel_tangencial(ingresar_vel_angular, ingresar_radio)
        print("La velocidad tangencial es: ", vel_tangencial, "cm/s")
    
    # Aqui se hacen los calculos para hallar la aceleracion centripeta llamando a la funcion que definimos anteriormente
    elif opcion == "4":
        print("\nCALCULO DE ACELERACION CENTRIPETA EN M. C. U.")
        ingresar_vel_tang = float(input("Ingrese velocidad tangencial: "))
        ingresar_vel_ang = float(input("Ingresar velocidad angular: "))
        acel_centripeta = calculo_acel_centripeta(ingresar_vel_tang, ingresar_vel_angular)
        print("La aceleracion centripeta es: ", acel_centripeta, "cm/s^2")
    
    # Aqui se hacen los calculos para hallar todos los procesos anteriores llamando a la funcion que definimos anteriormente
    elif opcion == "5":
        print("\nCALCULO DE FRECUENCIA, VELOCIDAD ANGULAR, VELOCIDAD TANGENCIAL Y ACELERACION CENTRIPETA EN M. C. U.")
        ingresar_rpm = float(input("Ingresar rpm (revoluciones por minuto): "))
        ingresar_radio = float(input("Ingresar radio (en centimetros): "))

        r_frecuencia, r_vel_angular, r_vel_tangencial, r_acel_centri = calculo_a_partir_de_rpm(ingresar_rpm, ingresar_radio)
        
        print("\nR E S U L T A D O S")
        print("Frecuencia: ", r_frecuencia, "c/s (ciclos/segundos)")
        print("Velocidad angular: ", r_vel_angular, "rad/s")
        print("Velocidad tangencial: ", r_vel_tangencial, "cm/s")
        print("Aceleracion centripetaa: ", r_acel_centri, "cm/s^2")
        
        # A partir de esta seccion se definen los aspectos para elaborar el grafico del circulo
        tiempo_grafico = np.linspace(0, 4 * np.pi / r_vel_angular, 1000)
        posicion_grafico = ingresar_radio * np.cos(r_vel_angular * tiempo_grafico)
        
        circle = plt.Circle((0, 0), ingresar_radio, color='blue', fill=False, label='Círculo (MCU)')
        
        plt.figure()
        plt.gca().add_patch(circle)  # Agregar el círculo al gráfico
        plt.plot(tiempo_grafico, posicion_grafico, label='MCU (Opción 5)')
        plt.title('Movimiento Circular Uniforme (MCU)')
        plt.xlabel('Posición X')
        plt.ylabel('Posición Y')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    elif opcion == "6":
        print("¡VUELVA PRONTO!")
        break 
    
    else:
        print("¡OPCION INCORRECTA! -> Elija una opcion dentro del menu")
        
        
        
        
        
    