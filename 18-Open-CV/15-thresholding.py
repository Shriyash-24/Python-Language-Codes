import cv2
import numpy as np

img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold_value = 200

# Apply binary threshold
ret, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Binary Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()