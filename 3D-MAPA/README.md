# Representación 3D de Trayectorias y Obstáculos

### Autor

- [@acaOficial](https://github.com/acaOficial)

## Tabla de Contenidos

- [Introducción](#introducción)
- [Estructura del Código](#estructura-del-código)
  - [ExtractPathScans.py](#extractpathscanspy)
  - [extraer.py](#extraerpy)
  - [Archivos JSON](#archivos-json)
  - [primeraPersona.html](#primerapersonahtml)
- [Requisitos](#requisitos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Resultados](#resultados)

---

## Introducción

Este módulo está diseñado para representar trayectorias y obstáculos en un entorno tridimensional, utilizando datos generados por el simulador Player/Stage. Las visualizaciones se generan mediante una aplicación web interactiva que utiliza Three.js y un conjunto de datos previamente procesados en formato JSON.

El objetivo principal es analizar visualmente las trayectorias seguidas por un robot y su interacción con obstáculos detectados.

---

## Estructura del Código

### ExtractPathScans.py

- Contiene la función `extract_path_scans`, que procesa los archivos de registro generados por Player/Stage.
- Extrae las trayectorias del robot (posición, velocidad y orientación) y las posiciones de los obstáculos detectados por sensores.
- Incluye funciones auxiliares para guardar los datos procesados en formato JSON:
  - `save_path_to_json`
  - `save_obs_to_json`

### extraer.py

- Lee los archivos JSON generados por `ExtractPathScans.py`.
- Aplica un factor de discretización a las coordenadas para reducir el número de puntos y generar datos optimizados para la visualización.
- Genera archivos JSON con las coordenadas discretizadas:
  - `output_obs_coordinates.json` para los obstáculos.
  - `output_path_coordinates.json` para las trayectorias.

### Archivos JSON

- **obs_data.json**: Contiene las coordenadas originales de los obstáculos detectados.
- **output_obs_coordinates.json**: Coordenadas de obstáculos discretizadas para su representación en 3D.
- **path_data.json**: Contiene las coordenadas originales de la trayectoria del robot.
- **output_path_coordinates.json**: Coordenadas de la trayectoria discretizadas para la representación en 3D.

### primeraPersona.html

- Página HTML que visualiza las trayectorias y obstáculos en un entorno 3D interactivo utilizando Three.js.
- Incluye:
  - Un minimapa para visualizar las rutas y obstáculos desde una vista superior.
  - Representación visual del robot, la trayectoria y los obstáculos.
  - Controles para moverse a través de la trayectoria.
  - Un marcador de meta visual en la posición final del robot.

---

## Requisitos

### Python

- **Python 3.x**
- Librerías necesarias:
  - `numpy`
  - `json`

```bash
pip install numpy
```

- **Web**
  - Navegador moderno con soporte para WebGL (Chrome, Firefox, Edge).

---

## Instrucciones de Uso

1. **Procesar archivos de registro**:
  - Usa el script `ExtractPathScans.py` para procesar el archivo de registro del simulador Player/Stage:
  ```bash
  python ExtractPathScans.py
  ```

2. **Discretizar datos:**
  - Ejecuta el script *extraer.py* para aplicar discretización a los datos procesados

  ```python
  python extraer.py
  ```

3. **Cargar la visualización en 3D:**
  - Abre el archivo primeraPersona.html en un navegador compatible.
  - Asegúrate de que los archivos output_obs_coordinates.json y output_path_coordinates.json estén en el mismo directorio.

4. **Navegar por la simulación:**
  - Usa las flechas de dirección para moverte por la trayectoria.
  - Observa los obstáculos y las trayectorias en el entorno 3D.

## Resultados

![image](https://github.com/user-attachments/assets/491a6b22-4037-46a0-a57c-d89133b29c7a)

![image](https://github.com/user-attachments/assets/e38d8d4f-6f38-4b05-8244-31698aa646d1)

![image](https://github.com/user-attachments/assets/e5ffbcc3-6c16-41f0-b3ba-2ac5ed26414a)

---