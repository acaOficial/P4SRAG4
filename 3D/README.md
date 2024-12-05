# Representación 3D Simple de Trayectorias y Obstáculos

### Autor

- [@acaOficial](https://github.com/acaOficial)

## Tabla de Contenidos

- [Introducción](#introducción)
- [Estructura del Código](#estructura-del-código)
  - [ExtractPathScans.py](#extractpathscanspy)
  - [ShowPlayerStageLog.py](#showplayerstagelogpy)
  - [main.py](#mainpy)
  - [Archivos JSON](#archivos-json)
- [Requisitos](#requisitos)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Resultados](#resultados)

---

## Introducción

Este módulo permite visualizar en 3D las trayectorias y las lecturas de sensores de un robot a partir de datos generados por el simulador Player/Stage. La representación incluye:
- La trayectoria del robot.
- Las lecturas de los sensores (coordenadas de obstáculos).
- Vectores de velocidad y orientación en puntos específicos de la trayectoria.

El objetivo principal es ofrecer una visualización sencilla pero informativa de los datos de navegación del robot.

---

## Estructura del Código

### ExtractPathScans.py

- Función `extract_path_scans`:
  - Extrae la trayectoria y las lecturas de sensores del archivo de registro del simulador Player/Stage.
  - Procesa los datos y los ajusta según un ángulo inicial dado (`th0`).
- Funciones auxiliares:
  - `save_obs_to_json`: Guarda las coordenadas de obstáculos en un archivo JSON.
  - `save_path_to_json`: Guarda las coordenadas de trayectoria en un archivo JSON.

### ShowPlayerStageLog.py

- Función `show_player_stage_log_3d_pro`:
  - Genera una visualización 3D de la trayectoria del robot, las lecturas de sensores y los vectores de velocidad.
  - Utiliza `matplotlib` y herramientas de gráficos 3D para crear una representación profesional y detallada.

### main.py

- Script principal que ejecuta la visualización:
  - Procesa un archivo de registro.
  - Llama a la función `show_player_stage_log_3d_pro` para mostrar la visualización 3D.

### Archivos JSON

- **obs_data.json**: Coordenadas de los obstáculos detectados.
- **path_data.json**: Coordenadas de la trayectoria del robot.

---

## Requisitos

- **Python 3.x**
- Librerías necesarias:
  - `numpy`
  - `matplotlib`
  - `mpl_toolkits.mplot3d`

Instala las dependencias con:

```bash
pip install numpy matplotlib
```

---

## Instrucciones de Uso

1. **Procesar un archivo de registro**:
   - Modifica el archivo `main.py` para apuntar al archivo de registro del simulador Player/Stage y establecer el ángulo inicial (`th0`).
   ```python
   filename = '../mydata2024_11_30_22_50_04.log'  # Cambia esto al nombre de tu archivo
   th0 = 0  # Ángulo inicial en radianes
   ```

2. **Ejecutar la visualización:**
    - Ejecuta el script main.py para generar y mostrar la visualización en 3D
    ```python
    python main.py
    ```

3. **Explorar la visualización:**
    - Observa la trayectoria en 3D, las lecturas de sensores y los vectores de velocidad en puntos clave.

---

## Resultados

![image](https://github.com/user-attachments/assets/a38072b2-1a88-4e61-97b2-4f1604fb83ce)

![image](https://github.com/user-attachments/assets/47e6618d-1c98-439a-944b-ba93581a9b01)

---
