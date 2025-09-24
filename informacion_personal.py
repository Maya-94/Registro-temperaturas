# informacion_personal.py
# Ejemplo de uso de diccionarios en Python

# 1) Crear el diccionario inicial
informacion_personal = {
    "nombre": "Maria Pianda",
    "edad": 31,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

print("Diccionario inicial:")
print(informacion_personal)

# 2) Cambiar la ciudad
informacion_personal["ciudad"] = "Portoviejo"

# 3) Cambiar la profesión
informacion_personal["profesion"] = "Ingeniera en Tecnologias de la Informacion"

# 4) Revisar si tiene teléfono, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+59399368026"

# 5) Quitar la edad
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 6) Imprimir el resultado final
print("\nDiccionario final:")
print(informacion_personal)
