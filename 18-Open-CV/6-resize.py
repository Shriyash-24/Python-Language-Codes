import cv2 # Imports OpenCV

img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png") # Black-White Images.
print("Dimensions of the image: ", img.shape) # It will give dimensions of the image.

width = img.shape[1] # width remains unchanged.
width = 1920
height = img.shape[0] # height remains changed.
height = 1080
dim = (width, height)
resized = cv2.resize(img, dim)

cv2.imshow("Window", resized) # Open GUI window named "Window".
# Passing resized, so I am now opening resized image there.

cv2.waitKey(0) # Waits indefinitely until you press a key. Without this window appears and disappears immediately.
# Number inside waitKey is in milliseconds.
cv2.destroyAllWindows() # Closes all OpenCV windows after key is pressed.
