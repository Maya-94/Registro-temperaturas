# Función para calcular la temperatura promedio por ciudad
def calcular_promedios(datos):
    """
    Calcula el promedio de temperatura por ciudad.
    :param datos: Diccionario con ciudades como claves y listas de temperaturas semanales como valores.
    :return: Diccionario con las ciudades y sus temperaturas promedio.
    """
    promedios = {}
    for ciudad, temps in datos.items():
        promedio = sum(temps) / len(temps)   # suma las temperaturas y divide por la cantidad
        promedios[ciudad] = promedio
    return promedios


# Ejemplo de uso con 3 ciudades y 4 semanas
if __name__ == "__main__":
    temperaturas = {
        "Quito": [18, 20, 19, 17],
        "Guayaquil": [28, 30, 29, 31],
        "Cuenca": [15, 16, 14, 15]
    }

    resultado = calcular_promedios(temperaturas)
    print("Promedio de temperaturas por ciudad:")
    for ciudad, promedio in resultado.items():
        print(f"{ciudad}: {promedio:.2f} °C")
