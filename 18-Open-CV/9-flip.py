import cv2

img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png")
width = 740
height = 493
dim = (width, height)
resized = cv2.resize(img, dim)
print('Size in byes: ', img.size)

cv2.imshow("Original", resized)
flip0 = cv2.flip(resized, 0)
cv2.imshow("Flip", flip0) # VERTICAL FLIP

flip1 = cv2.flip(resized, 1)
cv2.imshow("Flip1", flip1) # HORIZONTAL FLIP

flip2 = cv2.flip(resized, -1)
cv2.imshow("Flip2", flip2) # HORIZONTAL & VERTICAL




cv2.waitKey(0)
cv2.destroyAllWindows()
