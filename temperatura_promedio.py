"""
temperatura_promedio.py
Función para calcular temperaturas promedio por ciudad.
Incluye ejemplos y comprobaciones sencillas.
"""
from typing import Dict, List, Optional
import math

def _is_number(x):
    try:
        f = float(x)
        return not math.isnan(f)
    except:
        return False

def calcular_promedios(temperaturas: Dict[str, List[Optional[float]]]) -> Dict[str, Optional[float]]:
    """
    temperaturas: dict donde cada clave es el nombre de la ciudad y el valor
    es una lista de valores de temperatura (float, int) o None o strings no numéricos.
    Devuelve dict con promedios redondeados a 2 decimales (o None si no hay datos).
    """
    promedios = {}
    for ciudad, temps in temperaturas.items():
        # filtrar valores numéricos válidos
        cleaned = [float(t) for t in temps if t is not None and _is_number(t)]
        if len(cleaned) == 0:
            promedios[ciudad] = None
        else:
            avg = sum(cleaned)/len(cleaned)
            promedios[ciudad] = round(avg,2)
    return promedios

def calcular_promedios_de_tabla(ciudades: List[str], tabla: List[List[Optional[float]]]) -> Dict[str, Optional[float]]:
    """
    alternativa: recibir lista de ciudades y una "tabla" (lista de filas)
    donde cada fila corresponde a las temperaturas de una ciudad.
    """
    if len(ciudades) != len(tabla):
        raise ValueError("El número de ciudades debe coincidir con las filas de la tabla.")
    return calcular_promedios({ciudades[i]: tabla[i] for i in range(len(ciudades))})

# Ejemplo de datos (3 ciudades x 4 semanas)
datos_ejemplo = {
    "Quito": [15.2, 14.8, 16.0, 15.6],
    "Guayaquil": [28.1, 27.9, 28.4, 28.0],
    "Cuenca": [12.3, 12.0, 12.5, 11.9]
}

if __name__ == "__main__":
    promedios = calcular_promedios(datos_ejemplo)
    print("Promedios por ciudad:")
    for ciudad, prom in promedios.items():
        print(f"- {ciudad}: {prom} °C")
    # comprobaciones simples
    assert abs(promedios["Quito"] - 15.4) < 1e-6
    assert abs(promedios["Guayaquil"] - 28.1) < 1e-6
    assert abs(promedios["Cuenca"] - 12.17) < 1e-6
    print("Pruebas: OK")
