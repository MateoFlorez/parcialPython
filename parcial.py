opcion = 1
productos = []

# MENÚ
print('MENÚ DEL PROGRAMA')
print('1. Agregar producto')
print('2. Mostrar productos')
print('3. Buscar producto y editar precio')
print('4. Buscar producto y eliminarlo')
print('5. Salir')

while (opcion != 5):
    opcion = int(input('Digita una opción: '))
    if (opcion == 1):
        producto = {}
        ## Llenando el diccionario
        producto['codigo'] = input('Codigo producto: ')
        producto['nombreProducto'] = input('Producto: ')
        producto['precio'] = int(input('Precio producto: '))
        
        # Llenando la lista
        productos.append(producto)
    
    elif (opcion == 2):
        print(productos)

    elif (opcion == 3):
        bandera = True
        buscarCodigo = input('Digita el codigo a buscar: ')
        for producto in productos:
            if (producto['codigo'] == buscarCodigo):
                # Editar registro de la lista
                producto['precio'] = input('Digite el nuevo precio: ')
                bandera = True
                break
            else:
                bandera = False

    elif (opcion == 4):
        bandera = True
        buscarCodigo = input('Digita el codigo a buscar: ')
        for producto in productos:
            if (producto['codigo'] == buscarCodigo):
                # Borrar registro de la lista
                productos.remove(producto)
                bandera = True
                break
            else:
                bandera = False
    elif (opcion == 5):
        print('Saliendo del programa...')
    else:
        print('Digita una opción valida')
else:
    print('---------------------------------')
    print('Saliste del programa.')