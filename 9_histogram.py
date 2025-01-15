import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the grayscale image
# Replace 'image_path.jpg' with the path to your grayscale image
image = cv2.imread("SEM-5 Codes/lastday/0_Virat_Kohli_2.jpeg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error: Image not found or could not be loaded.")
    exit()
# Flatten the image to a 1D array of pixel values
pixel_values = image.flatten()
# Plot the histogram
plt.figure(figsize=(8, 6))
plt.hist(pixel_values, bins=256, range=(0, 256), color="gray", alpha=0.7)
plt.title("Histogram of Grayscale Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.grid(axis="y", alpha=0.75)
plt.show()
