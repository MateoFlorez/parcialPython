persona = {
    'nombre':'Mateo',
    'edad':32,
    'estatura':1.72,
    'leGustaJugar':True
}

print(persona)
print(persona['nombre'])
print(persona.get('edad'))

# Agregar
persona['carrera']='Ingeniero'
print(persona)