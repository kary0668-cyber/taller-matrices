n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []
contador = 1

for fila in range(n):
    nuevaFila = []
    matriz.append(nuevaFila)

for columna in range(n):
    for fila in range(n):
        matriz[fila].append(contador)
        contador += 1

for fila in matriz:
    print(fila)