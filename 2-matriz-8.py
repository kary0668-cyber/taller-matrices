n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []

for fila in range(n):
    nuevaFila = []

    for columna in range(n):
        if columna <= fila:
            if columna % 2 == 0:
                nuevaFila.append("A")
            else:
                nuevaFila.append("B")
        else:
            nuevaFila.append(" ")

    matriz.append(nuevaFila)

for fila in matriz:
    print(fila)