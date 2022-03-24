numeros = (50,45,20,30,40,87)

# Vonvierto tupla en lista
listaNumeros = list(numeros)

# Recorrer la lista
listaNumerosMayores = []
for numero in listaNumeros:
    # Condición
    if (numero > 40):
        listaNumerosMayores.append(numero)

# Imprimo la lista
print(listaNumerosMayores)
