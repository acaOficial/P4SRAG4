import json

# Nombres de los archivos
input_file = "obs_data.json"
output_file = "output_obs_coordinates.json"

# Factor de discretización (por ejemplo, cada 10 puntos)
discretization_factor = 10

# Leer el JSON desde el archivo
with open(input_file, "r") as file:
    input_json = json.load(file)

# Crear la estructura de coordenadas x y z con discretización
output_data = []

for x_row, y_row in zip(input_json["x"], input_json["y"]):
    for i, (x, z) in enumerate(zip(x_row, y_row)):
        if i % discretization_factor == 0:  # Agregar solo cada n-ésimo punto
            output_data.append({"x": x, "z": z})

# Guardar el resultado como JSON
output_json = {"coordinates": output_data}

with open(output_file, "w") as file:
    json.dump(output_json, file, indent=4)

print(f"Archivo JSON discretizado generado como '{output_file}'")


# Nombres de los archivos
path_input_file = "path_data.json"
path_output_file = "output_path_coordinates.json"

# Factor de discretización (por ejemplo, cada 10 puntos)
discretization_factor = 10

# Leer el JSON desde el archivo
with open(path_input_file, "r") as file:
    input_json = json.load(file)

# Crear la estructura de coordenadas x e y con discretización
output_data = []

# Iterar a través de las coordenadas x e y
for i, (x, y) in enumerate(zip(input_json["x"], input_json["y"])):
    if i % discretization_factor == 0:  # Agregar solo cada n-ésimo punto
        output_data.append({"x": x, "y": y})

# Guardar el resultado como JSON
output_json = {"coordinates": output_data}

with open(path_output_file, "w") as file:
    json.dump(output_json, file, indent=4)

print(f"Archivo JSON discretizado generado como '{path_output_file}'")

