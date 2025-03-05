import cv2
import numpy as np

def extract_temperature_map(image_path, min_temp, max_temp):
    """
    Extracts a temperature mapping from a vertical color scale image by sampling the center pixel of each row.

    Parameters:
        image_path (str): Path to the temperature scale image.
        min_temp (float): Minimum temperature value.
        max_temp (float): Maximum temperature value.

    Returns:
        tuple: (temperature_map, size)
            - temperature_map (dict): Dictionary mapping RGB colors (as tuples) to temperature values.
            - size (int): Number of unique color-temperature mappings.
    """
    # Load the image
    scale_image = cv2.imread(image_path)
    scale_image = cv2.cvtColor(scale_image, cv2.COLOR_BGR2RGB)

    # Crop to remove black borders
    mask = np.all(scale_image != [0, 0, 0], axis=-1)
    coords = np.argwhere(mask)
    y_min, y_max = coords[:, 0].min(), coords[:, 0].max()
    x_min, x_max = coords[:, 1].min(), coords[:, 1].max()
    color_bar = scale_image[y_min:y_max+1, x_min:x_max+1]

    height = color_bar.shape[0]  # Number of rows

    # Create temperature mapping
    temperature_map = {}
    for y in range(height):
        center_x = color_bar.shape[1] // 2  # Middle column
        color = tuple(map(int, color_bar[y, center_x]))  # Convert np.uint8 to int
        temperature = float(min_temp + (max_temp - min_temp) * (1 - y / (height - 1)))  # Convert np.float64 to float
        temperature_map[color] = temperature

    return temperature_map

def getNormalizedData(path, min_value, max_value):
    tempMap = extract_temperature_map(path, min_value, max_value)
    normalized_data = {key: (value - min_value) / (max_value - min_value) for key, value in tempMap.items()}
    return normalized_data