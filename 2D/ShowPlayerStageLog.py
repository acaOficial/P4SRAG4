import numpy as np
import matplotlib.pyplot as plt
from ExtractPathScans import extract_path_scans

def show_player_stage_log(filename, th0):
    """
    Show trajectory and sensor readings from a Player/Stage log file.

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

    precision = 1e-9

    plt.figure()
    plt.axis("equal")
    plt.grid(True)

    plt.xlabel("x (m)")
    plt.ylabel("y (m)")

    trajectory_init_color = np.array([0, 1, 0])  # green
    trajectory_last_color = np.array([1, 0, 0])  # red

    # Drawing trajectory points (odometry)
    for i in range(len(pos["x"])):
        lambda_val = i / len(pos["x"])
        color = trajectory_init_color * (1 - lambda_val) + trajectory_last_color * lambda_val
        plt.plot(pos["x"][i], pos["y"][i], ".", color=color)

    sensory_init_color = np.array([0, 1, 1])  # cyan
    sensory_last_color = np.array([0, 0, 0])  # black

    # Drawing sensor readings (laser)
    for i in range(len(obs["x"])):
        lambda_val = i / len(obs["x"])
        color = sensory_init_color * (1 - lambda_val) + sensory_last_color * lambda_val
        plt.plot(obs["x"][i], obs["y"][i], ".", color=color)

    plt.show()

# Uso de la función
# show_player_stage_log('mydata2018_02_26_14_42_05.log', np.pi * 45 / 180)
