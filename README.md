# Representación Gráfica de Pruebas de Algoritmos de Evitación de Obstáculos

### Autor

- [Acaymo Jesús Granado Sánchez](https://github.com/acaOficial)

## Tabla de Contenidos

- [Introducción](#introducción)
- [Estructura del Repositorio](#estructura-del-repositorio)
  - [2D](#2d)
  - [3D-MAPA](#3d-mapa)
  - [3D](#3d)
- [Requisitos](#requisitos)
- [Referencias Bibliográficas](#referencias-bibliográficas)

---

## Introducción

Este repositorio contiene el código necesario para la representación gráfica de pruebas realizadas con algoritmos de evitación de obstáculos. Los mapas generados permiten visualizar trayectorias en 2D y 3D, utilizando herramientas modernas como Python y JavaScript.

El objetivo principal es proporcionar herramientas de análisis visual de la trayectoria seguida por un robot bajo distintos algoritmos, facilitando la interpretación de resultados y la comparación entre técnicas.

---

## Estructura del Repositorio

El repositorio está organizado en las siguientes carpetas:

### 2D

Esta carpeta contiene la traducción de un código originalmente desarrollado en MATLAB a Python. Su finalidad es generar mapas bidimensionales que representen el entorno y las trayectorias del robot.

![image](https://github.com/user-attachments/assets/df9b60b6-6258-4456-9219-7ed7260185fc)

### 3D-MAPA

Incluye el código en Python necesario para representar las trayectorias del robot en un mapa tridimensional. Este mapa puede visualizarse mediante una aplicación web desarrollada en JavaScript.

![image](https://github.com/user-attachments/assets/d966d647-53f7-42f1-ac0c-75cd749a9096)

### 3D

Contiene una implementación simplificada para la visualización en 3D de las trayectorias del robot. Este código genera una representación básica que puede utilizarse como referencia rápida.

![image](https://github.com/user-attachments/assets/eb10a0bd-d655-417d-ae51-4a4c9cc948ad)

---

## Requisitos

- **Python 3.x**: Asegúrate de tener instalada la última versión.
- **Librerías necesarias**:
  - `matplotlib`
  - `numpy`
  - `plotly`

```bash
pip install matplotlib numpy plotly
```

- JavaScript (para 3D-MAPA):
  - Se utiliza una biblioteca para representar el mapa en una aplicación web
 
---

## Referencias Bibliográficas

- [Documentación matplotlib](https://matplotlib.org/stable/index.html)
- [Documentación numpy](https://numpy.org/doc/)
- [Documentación numpy](https://numpy.org/doc/)
- [Documentación plotly](https://plotly.com/python/)
