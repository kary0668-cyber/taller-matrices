n =int(input("Ingrese el tamaño de la matriz: "))

matriz3 = []

for i in range(n):
    fila = []
    
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
            
    matriz3.append(fila)
    
for fila in matriz3:
    print(fila)