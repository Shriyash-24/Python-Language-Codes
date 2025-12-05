import cv2 # Imports OpenCV
img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/ram.jpeg") # imread() loads an image from given file path.
# The image is stored as NumPy array (img).
img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/ram.jpeg", 0) # Black-White Images.



cv2.imshow("Window", img) # Open GUI window named "Window".
cv2.waitKey(0) # Waits indefinitely until you press a key. Without this window appears and disappears immediately.
# Number inside waitKey is in milliseconds.
cv2.destroyAllWindows() # Closes all OpenCV windows after key is pressed.

