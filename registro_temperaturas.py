# registro_temperaturas.py
# Registro de Temperaturas Diarias con matriz 3D y bucles anidados
# Estructura: matriz[ciudad][semana][dia]

import random

# --- Parámetros del problema ---
ciudades = ["Quito", "Guayaquil", "cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado"]
semanas = 2  # Cambia a 3 o más si necesitas

# --- Generar datos (reproducibles) ---
def generar_matriz_temperaturas(ciudades, dias, semanas, temp_min=10, temp_max=30, seed=42):
    random.seed(seed)  # para que el resultado sea reproducible
    matriz = []
    for _c in range(len(ciudades)):            # nivel 1: por ciudad
        ciudad_data = []
        for _s in range(semanas):              # nivel 2: por semana
            semana_data = []
            for _d in range(len(dias)):        # nivel 3: por día
                temperatura = random.randint(temp_min, temp_max)
                semana_data.append(temperatura)
            ciudad_data.append(semana_data)
        matriz.append(ciudad_data)
    return matriz

# --- Cálculo de promedios usando bucles anidados ---
def promedios_por_ciudad_y_semana(matriz, ciudades, dias):
    resultados = []  # [(ciudad, semana_index, promedio), ...]
    for c in range(len(ciudades)):
        for s in range(len(matriz[c])):
            suma = 0
            for d in range(len(dias)):
                suma += matriz[c][s][d]
            promedio = suma / len(dias)
            resultados.append((ciudades[c], s + 1, promedio))
    return resultados

# --- Mostrar resultados ---
def mostrar_registro(matriz, ciudades, dias):
    print("=== Registro de Temperaturas ===")
    for c in range(len(ciudades)):
        for s in range(len(matriz[c])):
            print(f"{ciudades[c]} - Semana {s+1}: {matriz[c][s]}")
    print()

def mostrar_promedios(resultados):
    print("=== Promedios de Temperatura ===")
    for ciudad, semana, promedio in resultados:
        print(f"Ciudad: {ciudad}, Semana {semana}, Promedio: {promedio:.2f}°C")

if __name__ == "__main__":
    matriz = generar_matriz_temperaturas(ciudades, dias, semanas)
    mostrar_registro(matriz, ciudades, dias)
    resultados = promedios_por_ciudad_y_semana(matriz, ciudades, dias)
    mostrar_promedios(resultados)
