import random 

jugador_1 = int(input("Ingrese numero de fichas(deben ser minimo 20 fichas): "))

while jugador_1 < 20:
    jugador_1 = int(input("Ingrese un numero valido de fichas(¡MINIMO 20!): "))
    
recipiente = jugador_1 * 2 
fichas_J1 = 0
fichas_J2 = 0

while recipiente > 0:
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    
    suma_dado = dado_1 + dado_2
    if suma_dado > recipiente:
        suma_dado = recipiente
    recipiente -= suma_dado
    print("En el recipiente quedan", recipiente,"fichas")
    print("El jugador 1 saca", suma_dado, "fichas")
    fichas_J1 += suma_dado
    print("El jugador 1 tiene", fichas_J1, "fichas")
    
    if recipiente > 0:
        dado_1 = random.randint(1,6)
        dado_2 = random.randint(1,6)
        
        suma_dado = dado_1 + dado_2
        if suma_dado > recipiente:
            suma_dado = recipiente
        recipiente -= suma_dado
        print("En el recipiente quedan", recipiente,"fichas")
        print("El jugador 2 saca", suma_dado, "fichas")
        fichas_J2 += suma_dado
        print("El jugador 1 tiene", fichas_J2, "fichas")

if  fichas_J1 > fichas_J2:
    print("¡JUGADOR 1 ES EL GANADOR!")
elif fichas_J2 > fichas_J1:
    print("¡JUGADOR 2 ES EL GANADOR!")
else:
    print("ES UN EMPATE")
    
print("JUGADOR 1: ", fichas_J1)
print("JUGADOR 2: ", fichas_J2)


    
    
    