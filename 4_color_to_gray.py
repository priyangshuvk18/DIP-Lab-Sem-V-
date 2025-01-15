import cv2 
# Read the color image 
color_image = cv2.imread("SEM-5 Codes/lastday/0_Virat_Kohli_2.jpeg") 
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)  
#OpenCV reads images in BGR format by default, so the conversion to grayscale is handled correctly with cv2.COLOR_BGR2GRAY.Save the grayscale image 
cv2.imwrite('grayscale_image.jpg', gray_image) 
# Display the original color image and the grayscale image after resizing 
resized_image1 = cv2.resize(color_image, (500, 700)) 
resized_image2 = cv2.resize(gray_image, (500, 700))
# Display the resized image 
cv2.imshow('Gray Image', resized_image1)
cv2.imshow('Color Image', resized_image2)     
# Wait for a key press and close all windows 
cv2.waitKey(0) 
cv2.destroyAllWindows() 