import cv2
import numpy as np

img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png")
column = img.shape[1] # Takes default width
row = img.shape[0] # Takes default height

# Creating transition arrays - Helps us denote x,y axis values so we can shift.
s = np.float32([(1,0,150),(0,1,70)])
# [ 1 0 150 ]
# [ 0 1 70  ]
# Controls rotation, scaling, shearing.
# (x,y) --> Each pixel at (x,y)
# For shifting, x(new) = x + 150, y(new) = y + 70
# 1*x + 0*y + 150 --> so x value increases by 150 --> right move
# 0*x + 1*y + 70 --> so y vale increases by 70 --> down

shifted = cv2.warpAffine(img, s, (column,row))
# warpAffine --> 2x3 transformation matrix. It tells how to move, rotate, scale, shear image.
cv2.imshow("Original", img)
cv2.imshow("Shifted", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()

