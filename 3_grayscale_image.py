import cv2 
import numpy as np 
# Read the image in grayscale mode 
image = cv2.imread('SEM-5 Codes/lastday/0_Virat_Kohli_2.jpeg', cv2.IMREAD_GRAYSCALE) 
# Check if the image is loaded successfully 
if image is None: 
        print("Error: Could not load the image.") 
else: 
# Resize the image to 256x256 
    image_resized = cv2.resize(image, (256, 256)) 
# Add 20 to each intensity value and ensure pixel values remain in range (0-255) 
modified_image = cv2.add(image_resized, 50) 
# Save the modified image to a new file 
cv2.imwrite('modified_image.jpg', modified_image) 
# Display the original and modified images 
cv2.imshow('Original Image', image_resized) 
cv2.imshow('Modified Image', modified_image) 
# Wait for a key press and close all windows 
cv2.waitKey(0) 
cv2.destroyAllWindows()