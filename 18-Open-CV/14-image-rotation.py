import cv2

img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png")

row = img.shape[1] # Default width
column = img.shape[0] # Default height

center = (column/2, row/2) # Rotate around the middle.
angle = 90
# OpenCV rotates counter-clockwise by default, so 90 degree CCW.
# Negative angle is CW.

r = cv2.getRotationMatrix2D(center, angle, 1)
# getRotationMatrix2D tells openCV where center, degree and how much to scale.
# scale --> 1 (original), 2 (zoom in), 0.5 (shrink)

rotate = cv2.warpAffine(img,r,(column,row))

cv2.imshow("Rotated",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()