# Registro de Temperaturas Diarias (Matriz 3D con Python)

Este proyecto muestra cómo **iterar arreglos multidimensionales (matriz 3D)** con **bucles anidados** para calcular el **promedio de temperaturas por ciudad y por semana**.

## Estructura de la matriz
`matriz[ciudad][semana][dia]`

- `ciudad` → índice de la ciudad (Quito, Guayaquil, Ambato).
- `semana` → semana 1, 2,3 ...
- `dia` → Lunes...viernes.

## Requisitos
- Python 3.9 o superior 


###  PyCharm
1. Abre PyCharm y **Open** la carpeta del proyecto.
2. Clic derecho sobre `registro_temperaturas.py` → **Run 'registro_temperaturas'**.
3. Mira la salida en la consola *Run*.


## Subir a GitHub (pasos simples)

### Git desde terminal
```bash
git init
git add registro_temperaturas.py README.md
git commit -m "feat: matriz 3D y promedios"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/registro-temperaturas.git
git push -u origin main
```
Luego abre el archivo en GitHub y copia la URL.

## Salida esperada (ejemplo)
```
=== Registro de Temperaturas ===
Quito - Semana 1: [30, 11, 11, 23, 26, 28, 24]
Quito - Semana 2: [16, 20, 27, 14, 22, 22, 15]
Guayaquil - Semana 1: [24, 24, 11, 17, 25, 17, 29]
Guayaquil - Semana 2: [11, 20, 20, 20, 22, 23, 19]
Cuenca - Semana 1: [30, 14, 14, 18, 12, 24, 11]
Cuenca - Semana 2: [29, 26, 19, 25, 22, 17, 29]

=== Promedios de Temperatura ===
Ciudad: Quito, Semana 1, Promedio: 21.86°C
Ciudad: Quito, Semana 2, Promedio: 19.43°C
Ciudad: Guayaquil, Semana 1, Promedio: 21.00°C
Ciudad: Guayaquil, Semana 2, Promedio: 19.29°C
Ciudad: Cuenca, Semana 1, Promedio: 17.57°C
Ciudad: Cuenca, Semana 2, Promedio: 23.86°C
```

## Notas
- Todo el cálculo se hace con **bucles anidados**, sin librerías adicionales, tal como suele pedirse en cursos introductorios.
- Si tu docente pide *no usar números aleatorios*, reemplaza la generación por una lista fija de valores.
