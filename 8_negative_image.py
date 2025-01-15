import cv2 
# Load the image 
image = cv2.imread('SEM-5 Codes/lastday/0_Virat_Kohli_2.jpeg') 
# Create the negative image 
negative_image = 255 - image 
# Save the negative image 
cv2.imwrite('negative_image.jpg', negative_image) 
# Display the original and negative images 
cv2.imshow('Original Image', image) 
cv2.imshow('Negative Image', negative_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 