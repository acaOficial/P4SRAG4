# Análisis y Visualización de Trayectorias en 2D

### Autor

- [@acaOficial](https://github.com/acaOficial)

## Tabla de Contenidos

- [Introducción](#introducción)
- [Estructura del Código](#estructura-del-código)
  - [AnalyzePlayerStageLog.py](#analyzeplayerstagelogpy)
  - [ExtractPathScans.py](#extractpathscanspy)
  - [NextTokenLine.py](#nexttokenlinepy)
  - [main.py](#mainpy)
- [Requisitos](#requisitos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Resultados](#resultados)

---

## Introducción

Este módulo permite analizar los datos generados por el simulador Player/Stage para estudiar las trayectorias y la interacción del robot con obstáculos en un entorno simulado. Incluye herramientas para procesar los datos del archivo de registro, calcular velocidades y aceleraciones, y graficar resultados como trayectorias y distancias a obstáculos.

---

## Estructura del Código

### AnalyzePlayerStageLog.py

Este archivo implementa la función principal para analizar los datos de trayectoria obtenidos de un archivo de registro del simulador Player/Stage. Proporciona gráficos de:
- Velocidades (lineales y angulares).
- Aceleraciones calculadas.
- Distancias mínimas a obstáculos en cada momento.

### ExtractPathScans.py

Contiene la función `extract_path_scans`, que extrae:
- Trayectorias: tiempo, posición, ángulo, velocidades lineales y angulares.
- Coordenadas de obstáculos detectados por el sensor de rango (láser).

Los datos se ajustan a un ángulo inicial (`th0`) y se procesan para producir coordenadas consistentes.

### NextTokenLine.py

Define la función `next_token_line`, que busca líneas específicas en el archivo de registro basándose en palabras clave. Es utilizada por otros módulos para encontrar datos relevantes en los registros.

### main.py

Este archivo es el punto de entrada para ejecutar el análisis. Utiliza las funciones de los otros módulos para procesar un archivo de registro y visualizar los resultados.

---

## Requisitos

- **Python 3.x**: Asegúrate de tener instalada la última versión.
- **Librerías necesarias**:
  - `numpy`
  - `matplotlib`

```bash
pip install numpy matplotlib
```

---

## Instrucciones de Uso

1. Coloca el archivo de registro del simulador Player/Stage en el mismo directorio o ajusta la ruta en el script `main.py`.

2. Modifica el archivo `main.py` para apuntar al archivo de registro y establecer el ángulo inicial (`th0`).

  ```python
  filename = '../mydata2024_11_30_22_50_04.log'  # Cambia esto al nombre de tu archivo
  th0 = 0  # Ángulo inicial en radianes
  ```

3. Ejecuta el archivo main.py para iniciar el análisis y generar gráficos.

  ```python
  python main.py
  ```

---

## Resultados

![image](https://github.com/user-attachments/assets/103c201e-f1e1-4b49-b08b-8aa34699a20d)

![image](https://github.com/user-attachments/assets/c33152b9-2924-4512-b170-6310e4d7d93f)

---