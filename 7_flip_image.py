import cv2 
# Load the image 
image = cv2.imread('SEM-5 Codes/lastday/0_Virat_Kohli_2.jpeg') 
# Flip the image 
# Flip Code: 0 = vertical flip, 1 = horizontal flip, -1 = both axes 
flipped_vertically = cv2.flip(image, 0)  # Vertical flip 
flipped_horizontally = cv2.flip(image, 1)  # Horizontal flip 
flipped_both = cv2.flip(image, -1)  # Flip both vertically and horizontally 
# Save the flipped images 
cv2.imwrite('flipped_vertical.jpg', flipped_vertically) 
cv2.imwrite('flipped_horizontal.jpg', flipped_horizontally) 
cv2.imwrite('flipped_both.jpg', flipped_both) 
# Display the flipped images 
cv2.imshow('Original Image', image) 
cv2.imshow('Vertically Flipped', flipped_vertically) 
cv2.imshow('Horizontally Flipped', flipped_horizontally) 
cv2.imshow('Flipped Both', flipped_both) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 