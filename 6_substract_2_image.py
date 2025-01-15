import cv2 
# Load the two images (ensure they are of the same size) 
image1 = cv2.imread("SEM-5 Codes/lastday/0_Virat_Kohli_1.jpeg") 
image2 = cv2.imread("SEM-5 Codes/lastday/0_Virat_Kohli_2.jpeg") 
# Resize the images if necessary to make them the same size 
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))          
# Add the images 
subtracted_image = cv2.subtract(image1, image2) 
# Save and display the result 
cv2.imwrite("subtracted_image.jpg", subtracted_image) 
cv2.imshow("Subtract Image", subtracted_image) 
resized_image1 = cv2.resize(subtracted_image, (500, 700)) 
# Display the resized image 
cv2.imshow('Subtract Image', resized_image1)
cv2.waitKey(0) 
cv2.destroyAllWindows()