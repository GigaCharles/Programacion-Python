

arreglo = []

with open(r'C:\Users\Estudiante\Downloads\HEROES.txt', 'r') as recuperacion:

    for x in recuperacion:
        arreglo.append(x.strip())

print(arreglo)

