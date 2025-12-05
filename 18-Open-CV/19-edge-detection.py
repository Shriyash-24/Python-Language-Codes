# Canny Edge Detection Algorithm
# 1. Noise Reduction
# 2. Intensity of the gradient of the image.
# 3. Non-maximum suppression.
# 4. Thresholding

import cv2
import numpy as np

img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png", 0)
min_thresh = 100
max_thresh = 200

edges = cv2.Canny(img,min_thresh,max_thresh)

cv2.imshow("Input",img)
cv2.imshow("Output",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()