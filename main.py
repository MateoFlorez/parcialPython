# LISTAS
valores = [1,2,3,4,5]

# TUPLA
valoresTupla = (1,2,3,4,5)
print(valoresTupla)
#for valor in valoresTupla:
    #print(valor)

# Accediendo a elemento de tupla
#print(valoresTupla[0])
#valoresTupla.append(6) # En las tuplas no existe el metodo append para agregar
#print(valoresTupla)

# Transformando una tupla en una lista
listaValores = list(valoresTupla)
print(listaValores)
listaValores.append(6)
print(listaValores)

valoresTupla = tuple(listaValores)
print(valoresTupla)