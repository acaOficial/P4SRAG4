import numpy as np
import matplotlib.pyplot as plt
from ExtractPathScans import extract_path_scans


def analyze_player_stage_log(filename, th0):
    # Extraer datos
    path, obs = extract_path_scans(filename, th0)

    # Velocidades y aceleraciones
    time = np.array(path['time'])
    vx = np.array(path['vx'])
    vth = np.array(path['vth'])

    # Calcular aceleraciones (diferencias finitas)
    dt = np.diff(time)
    ax = np.diff(vx) / dt
    ath = np.diff(vth) / dt

    # Graficar velocidades
    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.plot(time, vx, 'r', label='v_x')
    plt.plot(time, vth, 'b', label='v_θ')
    plt.legend()
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title('Velocidades Comandadas')

    # Graficar aceleraciones
    plt.subplot(3, 1, 2)
    plt.plot(time[:-1], ax, 'r', label='a_x')
    plt.plot(time[:-1], ath, 'b', label='a_θ')
    plt.legend()
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Aceleración (m/s²)')
    plt.title('Aceleraciones')

    # Distancia a obstáculos
    n_scans = len(obs['x'])
    d_min = np.zeros(n_scans)
    time_scans = time[:n_scans]  # Tiempo asociado a los escaneos

    for i in range(n_scans):
        distances = np.sqrt(np.array(obs['x'][i])**2 + np.array(obs['y'][i])**2)
        d_min[i] = np.nanmin(distances)

    # Graficar distancias mínimas
    plt.subplot(3, 1, 3)
    plt.plot(time_scans, d_min, 'k')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Distancia mínima (m)')
    plt.title('Distancia a los obstáculos más cercanos')

    plt.tight_layout()
    plt.show()

# Nota: `extract_path_scans` debe implementarse por separado para extraer los datos de archivo, como en MATLAB.
