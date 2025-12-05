import cv2 # Imports OpenCV

img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/ram.jpeg", 0) # Black-White Images.



cv2.imshow("Window", img) # Open GUI window named "Window".
cv2.imwrite("Ram.jpg", img) # filename and image are the parameters.
# Puts image in specific directory. instead of Krishna.jpg you can also specify the path

cv2.waitKey(0) # Waits indefinitely until you press a key. Without this window appears and disappears immediately.
# Number inside waitKey is in milliseconds.
cv2.destroyAllWindows() # Closes all OpenCV windows after key is pressed.

