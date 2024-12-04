import numpy as np

def extract_path_scans(filename, th0):
    """
    Extract path and obstacle scans from a log file.
    
    Args:
        filename (str): Log filename.
        th0 (float): Initial robot angle in radians.
        
    Returns:
        path (dict): Contains time, x, y, th, vx, vy, vth.
        obs (dict): Contains x and y coordinates for NSCANS.
    """
    ranger_name = 'laser'
    position_name = 'position2d'

    obs = {"x": [], "y": []}
    path = {"time": [], "x": [], "y": [], "th": [], "vx": [], "vy": [], "vth": []}
    n_scans = 0

    try:
        fP = open(filename, 'r')
    except FileNotFoundError:
        print(f"GetObstacles: ERROR file not found {filename}")
        return None, None

    def next_token_line(file, token):
        for line in file:
            if token in line:
                return line.strip(), line.find(token)
        return None, None

    # First ranger header
    ranger_line, pos = next_token_line(fP, ranger_name)

    # Ranger configuration
    ranger_line, pos = next_token_line(fP, ranger_name)
    ranger_conf = list(map(float, ranger_line[pos + len(ranger_name) + 1:].split()))

    min_angle = ranger_conf[4]
    max_angle = ranger_conf[5]
    max_dist = ranger_conf[7]

    # First position header
    position_line, pos = next_token_line(fP, position_name)

    finish = False
    while not finish:
        # Next position
        position_line, pos = next_token_line(fP, position_name)

        if position_line:
            position_data = list(map(float, position_line[:pos].split()))
            path["time"].append(position_data[0])

            position_data = list(map(float, position_line[pos + len(position_name) + 1:].split()))
            # Odometric positions
            path["x"].append(position_data[3])
            path["y"].append(position_data[4])
            path["th"].append(position_data[5])
            # Odometric velocities
            path["vx"].append(position_data[6])
            path["vy"].append(position_data[7])
            path["vth"].append(position_data[8])

            # Next scan
            ranger_line, pos = next_token_line(fP, ranger_name)

            if ranger_line:
                ranger_data = list(map(float, ranger_line[pos + len(ranger_name) + 1:].split()))
                n_data = int(ranger_data[8])
                ranger_data = ranger_data[9::2]
                ranger_data = np.array(ranger_data)
                ranger_data[ranger_data >= max_dist] = np.nan

                angles = np.linspace(min_angle, max_angle, n_data)

                xo = ranger_data * np.cos(angles + path["th"][-1])
                yo = ranger_data * np.sin(angles + path["th"][-1])

                n_scans += 1
                obs["x"].append(xo + path["x"][-1])
                obs["y"].append(yo + path["y"][-1])
            else:
                finish = True
        else:
            finish = True

    fP.close()

    # Adjust coordinates based on th0
    # Adjust coordinates based on th0
    for i in range(len(obs["x"])):
        angles = np.arctan2(obs["y"][i], obs["x"][i])
        radii = np.hypot(obs["x"][i], obs["y"][i])
        obs["x"][i] = radii * np.cos(angles + th0)
        obs["y"][i] = radii * np.sin(angles + th0)

    for i in range(len(path["x"])):
        p_theta = np.arctan2(path["y"][i], path["x"][i])
        p_r = np.hypot(path["x"][i], path["y"][i])
        path["x"][i] = p_r * np.cos(p_theta + th0)
        path["y"][i] = p_r * np.sin(p_theta + th0)


    return path, obs
