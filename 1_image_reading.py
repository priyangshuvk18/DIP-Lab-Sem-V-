import cv2

# Read the image
image = cv2.imread(
    "SEM-5 Codes/lastday/0_Virat_Kohli_1.jpeg"
)
# Display the image in a window
cv2.imshow("Image", image)

# ’Image’ is the name of the tab where the image will be displayed
# Wait for a key press indefinitely or for a specified amount of time (in milliseconds)
cv2.waitKey(0)
# Close all OpenCV windows
cv2.destroyAllWindows()
