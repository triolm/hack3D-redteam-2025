import numpy as np
import cv2
import matplotlib.pyplot as plt

def detect_cube_outline(normalized_img_array):
    """
    Detects and outlines the cube from a normalized temperature map.
    
    Parameters:
    - normalized_img_array: np.array, 2D array with normalized temperature values (0 to 1).
    
    Returns:
    - Edge-detected image (displayed via matplotlib).
    """
    
    # Scale to 0-255 for OpenCV processing
    img_scaled = (normalized_img_array * 255).astype(np.uint8)
    
    # Apply Gaussian blur to smooth the image
    img_blur = cv2.GaussianBlur(img_scaled, (5, 5), 0)
    
    # Apply Canny edge detection
    edges = cv2.Canny(img_blur, threshold1=50, threshold2=150)
    
    # Display the result
    plt.figure(figsize=(6, 6))
    plt.imshow(edges, cmap='gray')
    plt.title("Detected Cube Outline")
    plt.axis("off")
    plt.show()
    
    return edges
