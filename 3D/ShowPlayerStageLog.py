import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Necesario para gráficos 3D
from ExtractPathScans import extract_path_scans

import plotly.graph_objects as go
import numpy as np


def show_player_stage_log_3d_pro(filename, th0):
    """
    Professional 3D representation of trajectory, sensor readings, and velocity vectors 
    from a Player/Stage log file.

    Args:
        filename (str): Log filename.
        th0 (float): Initial robot angle in radians.

    Returns:
        None
    """
    pos, obs = extract_path_scans(filename, th0)

    if pos is None or obs is None:
        print("Error: No data extracted.")
        return

    # Convertir las matrices de obs a vectores unidimensionales
    obs_x = np.array(obs["x"]).flatten()
    obs_y = np.array(obs["y"]).flatten()

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.set_axis_off()  # Ocultar los ejes y la cuadrícula
    ax.set_facecolor('white')  # Fondo blanco

    # Trayectoria del robot (z=0.1)
    pos_z = np.full_like(pos["x"], 0.1)
    sampled_indices = np.arange(0, len(pos["x"]))
    ax.scatter(
        np.array(pos["x"])[sampled_indices],
        np.array(pos["y"])[sampled_indices],
        pos_z[sampled_indices],
        color='red',
        label="Trayectoria del Robot",
        s=10 
    )

    velocity_sample_indices = np.arange(0, len(pos["x"]), 30)
    for i in velocity_sample_indices:
        x, y, z = pos["x"][i], pos["y"][i], 0.1
        vx, vy = pos["vx"][i], pos["vy"][i]
        angle = pos["th"][i] 

        # Rotar los vectores de velocidad según el ángulo del robot
        vx_rot = vx * np.cos(angle) - vy * np.sin(angle)
        vy_rot = vx * np.sin(angle) + vy * np.cos(angle)

        # Dibujar la flecha en el gráfico
        ax.quiver(
            x, y, z,              
            vx_rot, vy_rot, 0,    
            color='black',
            length=1.0,           
            arrow_length_ratio=0.5,  
            linewidth=2
        )
        
        ax.scatter(
            x, y, z,
            color='black',
            s=20 
        )
        
        # Calcular la magnitud de la velocidad
        velocity_magnitude = np.sqrt(vx ** 2 + vy ** 2)
        
        # Añadir el texto con la velocidad
        ax.text(
            x + vx_rot * 0.5,  
            y + vy_rot * 0.5,  
            z,                 
            f"{velocity_magnitude:.2f}", 
            color='blue',
            fontsize=8,
            ha='center' 
        )


    # Lecturas del sensor (z=2)
    sampled_indices_obs = np.arange(0, len(obs_x), 500)

    # Líneas de conexión entre trayectorias y lecturas
    for i in sampled_indices_obs:
        x = obs_x[i]
        y = obs_y[i]
        ax.plot(
            [x, x],
            [y, y],
            [0.1, 2],
            color='blue',
            alpha=0.3,
            linewidth=5
        )

    # Ajustar la vista inicial
    ax.view_init(elev=25, azim=30)

    # Leyenda y título
    ax.legend(loc='upper right', fontsize=10)
    ax.set_title("Representación 3D Simple de la Trayectoria del Robot, Lecturas de los Sensores y Velocidades", fontsize=14)

    plt.show()







