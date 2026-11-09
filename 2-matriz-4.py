n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []

for i in range(n):
    fila = []

    for j in range(n):
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)

    matriz.append(fila)

for fila in matriz:
    print(fila)