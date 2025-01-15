import cv2 
# Read the image 
image = cv2.imread('SEM-5 Codes/lastday/0_Virat_Kohli_2.jpeg')  # Replace 'image.jpg' with your image file path 
# Resize the image to 128x128 pixels 
resized_image = cv2.resize(image, (500, 700)) 
# Display the resized image 
cv2.imshow('Resized Image', resized_image)   
# Wait for a key press indefinitely 
cv2.waitKey(0) 
# Close all OpenCV windows 
cv2.destroyAllWindows() 