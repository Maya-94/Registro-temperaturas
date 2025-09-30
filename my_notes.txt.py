# Tarea: trabajar con archivos (explicado para niños)
# Crea my_notes.txt, escribe 3 líneas, las lee y las muestra.

# 1) Abrir (crear) el archivo para escribir
file = open("my_notes.txt", "w")  # "w" = write (escribir)

# 2) Escribir tres líneas (cada "\n" es como presionar Enter)
file.write("Nota 1: Hoy practiqué mucho Python.\n")
file.write("Nota 2: Aprendí a abrir y cerrar archivos.\n")
file.write("Nota 3: Me gusta programar.\n")

# 3) Cerrar el archivo para guardar (como cerrar un cuaderno)
file.close()

# 4) Abrir el archivo para leer lo que escribimos
file = open("my_notes.txt", "r")  # "r" = read (leer)

# 5) Leer línea por línea usando readline()
linea = file.readline()  # lee la primera línea
while linea:             # mientras haya texto
    print(linea.strip()) # muestra la línea en pantalla
    linea = file.readline()  # leer la siguiente línea

# 6) Cerrar el archivo otra vez
file.close()

print("¡Listo! Terminó el programa.")
