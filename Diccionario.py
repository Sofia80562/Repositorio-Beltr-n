#Tarea Semana 15

#Primero, creamos un diccionario inicial

informacion_personal = {
    "nombre": "María Beltrán",
    "edad": 20,
    "ciudad": "Quito",
    "profesion": "ninguna (estudiante)"
}

#Accedemos al valor asociado con la clave "ciudad" y lo modificamos. Cambiamos la ciudad de Quito a Guayaquil

informacion_personal["ciudad"] = "Guayaquil"

#Verificamos si la clave "telefono" existe en el diccionario. Ya que no existe, la agregamos con un número de teléfono ficticio

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número ficticio

#Eliminamos la clave "edad" porque ya no es necesaria en el diccionario
del informacion_personal["edad"]


#Imprimimos el diccionario final

print(informacion_personal)
