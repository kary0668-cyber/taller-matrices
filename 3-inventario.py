productos = []

opcion = 0

while opcion != 7:

    print("\n--- INVENTARIO DE LA TIENDA ---")
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Ordenar productos alfabéticamente")
    print("6. Mostrar número total de productos")
    print("7. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        producto = input("Ingrese el nombre del producto: ")
        productos.append(producto)
        print("Producto agregado correctamente")

    elif opcion == 2:
        cantidad = int(input("¿Cuántos productos desea agregar? "))

        for i in range(cantidad):
            producto = input("Ingrese el nombre del producto: ")
            productos.append(producto)

        print("Lote de productos agregado")

    elif opcion == 3:
        producto = input("Ingrese el producto que desea eliminar: ")

        if producto in productos:
            productos.remove(producto)
            print("Producto eliminado")
        else:
            print("El producto no existe")

    elif opcion == 4:
        if len(productos) > 0:
            eliminado = productos.pop()
            print("Producto retirado:", eliminado)
        else:
            print("El inventario está vacío")

    elif opcion == 5:
        productos.sort()
        print("Productos ordenados alfabéticamente")
        print(productos)

    elif opcion == 6:
        print("Total de productos:", len(productos))
        print(productos)

    elif opcion == 7:
        print("Saliendo del inventario...")

    else:
        print("Opción no válida")