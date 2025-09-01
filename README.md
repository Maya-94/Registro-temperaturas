# Registro de Temperaturas Diarias (Matriz 3D con Python)

Este proyecto muestra cómo **iterar arreglos multidimensionales (matriz 3D)** con **bucles anidados** para calcular el **promedio de temperaturas por ciudad y por semana**.

## Estructura de la matriz
`matriz[ciudad][semana][dia]`

- `ciudad` → índice de la ciudad (Quito, Guayaquil, Ambato).
- `semana` → semana 1, 2,3 ...
- `dia` → Lunes...viernes.

## Requisitos
- Python 3.9 o superior (también funciona con 3.8).
- *No requiere librerías externas*.

## Cómo ejecutar

### Opción A) Doble clic (IDLE) en Windows
1. Descarga `registro_temperaturas.py` a una carpeta.
2. Haz **clic derecho** → *Edit with IDLE* (o ábrelo con IDLE).
3. Presiona **F5** para ejecutar. Verás el resultado en la consola de IDLE.

### Opción B) VS Code
1. Instala [Python] y [VS Code].
2. Abre la carpeta del proyecto en VS Code.
3. Crea o abre `registro_temperaturas.py`.
4. Abre una **Terminal** en VS Code (``Ctrl+` ``).
5. Ejecuta: `python registro_temperaturas.py` (o `py registro_temperaturas.py`).

### Opción C) PyCharm
1. Abre PyCharm y **Open** la carpeta del proyecto.
2. Clic derecho sobre `registro_temperaturas.py` → **Run 'registro_temperaturas'**.
3. Mira la salida en la consola *Run*.

## ¿Qué puedes cambiar?
- En el archivo, ajusta:
  - `semanas = 2` → pon 3, 4, etc.
  - Lista `ciudades` o `dias`.
  - Rango de temperaturas (`temp_min`, `temp_max`).
  - Semilla (`seed`) para resultados reproducibles.

## Subir a GitHub (pasos simples)

### 1) Usando GitHub (web)
1. Ve a GitHub → **New repository** → nómbralo `registro-temperaturas`.
2. Entra al repo → **Add file** → **Upload files** → sube `registro_temperaturas.py` y este `README.md`.
3. **Commit changes**.
4. Abre `registro_temperaturas.py` en GitHub y copia la URL del navegador. **Ese es el enlace** que debes pegar en la plataforma.

### 2) Con GitHub Desktop
1. **File → New repository** (ubicación: carpeta del proyecto).
2. Arrastra `registro_temperaturas.py` y `README.md` a esa carpeta si aún no están.
3. En GitHub Desktop: escribe un mensaje y **Commit to main** → **Publish repository**.
4. Clic derecho sobre `registro_temperaturas.py` → **View on GitHub** → copia la URL.

### 3) Con Git desde terminal
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
