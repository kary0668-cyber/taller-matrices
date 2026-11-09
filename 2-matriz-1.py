matriz = (int(input("Ingrese el tamaño de la matriz: ")))

matrizCompleta = []
contador = 1

for fila in range(matriz):
    nuevafila = []
    
    for columna in range(matriz):
        nuevafila.append(contador)
        contador += 1
        
    matrizCompleta.append(nuevafila)
    
for fila in matrizCompleta:
    print(fila)
    

