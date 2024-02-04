import cv2
import numpy as np

def remove_background(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to create a binary mask
    _, mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # Apply morphological operations to remove noise and close gaps in the mask
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)

    # Create a transparent background
    transparent_bg = np.zeros_like(image, dtype=np.uint8)

    # Copy the image where the mask is not zero
    transparent_bg[:] = cv2.bitwise_and(image, image, mask=mask_inv)

    # Save the result
    cv2.imwrite(output_path, transparent_bg)

# Example usage
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.png'
remove_background(input_image_path, output_image_path)
