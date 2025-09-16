def calcular_descuento(total, porcentaje=10):
    # Convierte a número decimal por si escribe texto
    total = float(total)
    porcentaje = float(porcentaje)
    descuento = (total * porcentaje) / 100.0
    return descuento

def main():
    # Ejemplo con descuento por defecto (10%)
    compra1 = 100.0
    descuento1 = calcular_descuento(compra1)
    print("Compra:", compra1)
    print("Descuento (10%):", round(descuento1, 2))
    print("Total a pagar:", round(compra1 - descuento1, 2))
    print("-----")

    # Ejemplo con descuento personalizado (20%)
    compra2 = 250.0
    descuento2 = calcular_descuento(compra2, 20)
    print("Compra:", compra2)
    print("Descuento (20%):", round(descuento2, 2))
    print("Total a pagar:", round(compra2 - descuento2, 2))

if __name__ == "__main__":
    main()
