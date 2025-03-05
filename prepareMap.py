from PIL import Image
import numpy as np

def getTemperatureMap(image_path, normalized_temp_data, block_size=4):
    """
    Applies a temperature map to a thermal image based on a normalized temperature map,
    processing the image in block_size x block_size chunks for efficiency.

    Parameters:
    - image_path: str, path to the PNG image file.
    - normalized_temp_data: dict, normalized temperature values for RGB keys (key = RGB, value = normalized temperature).
    - block_size: int, size of the block to process at once (default is 4x4).
    
    Returns:
    - None: Displays the temperature map image.
    """
    
    # Reverse the normalized temperature data for easy lookup
    min_temp = min(normalized_temp_data.values())
    max_temp = max(normalized_temp_data.values())
    
    # Load the thermal image
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure the image is in RGB format

    # Convert image to numpy array for processing
    img_array = np.array(img)
    height, width, _ = img_array.shape

    # Initialize an array for the normalized temperature map
    normalized_img_array = np.zeros((height, width), dtype=float)

    # Process the image in block_size x block_size chunks
    for i in range(0, height, block_size):
        print(i)
        for j in range(0, width, block_size):
            # Get the block
            block = img_array[i:i+block_size, j:j+block_size]

            # Compute the average RGB value for the block
            avg_pixel = np.mean(block.reshape(-1, 3), axis=0).astype(int)
            avg_pixel_tuple = tuple(avg_pixel)

            # Find the closest matching temperature based on the average RGB value
            closest_temp = min(normalized_temp_data, key=lambda x: np.linalg.norm(np.array(x) - np.array(avg_pixel_tuple)))
            normalized_temp = (normalized_temp_data[closest_temp] - min_temp) / (max_temp - min_temp)
            
            # Assign the normalized temperature to all pixels in the block
            normalized_img_array[i:i+block_size, j:j+block_size] = normalized_temp

    return normalized_img_array
