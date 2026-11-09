n = int(input("Ingrese el tamaño de la matriz: "))

matriz2 = []

for fila in range(n):
    nuevafila =  []
    
    if fila % 2 == 0:
        for columna in range(1, n + 1):
            nuevafila.append(columna)
            
    else:
        for columna in range(n, 0, -1):
            nuevafila.append(columna)
            
    matriz2.append(nuevafila)
    
for fila in matriz2:
    print(fila)