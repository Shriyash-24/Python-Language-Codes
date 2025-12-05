import cv2
img = cv2.imread('C:/Users/Shri/Coding/Additional-Files/bg.png')

print("Dimension of Original Image: ", img.shape)
scale = 50 # ( 50% scale)
width = int(img.shape[1]*scale / 100) # img.shape[1] means width remains same * 50 and divide by 100.
height = int(img.shape[0]*scale / 100) # img.shape[0] means height remains same * 50 and divide by 100

dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# INTER_CUBIC, INTER_LINEAR --> SCALING UP
# INTER_AREA, INTER_NEAREST --> SCALING DOWN
# To fill empty pixels when scaling up or down. That's the part of interpolation.
print("Dimension of Resized Image: ", resized.shape)

cv2.imshow("Original Image", img)
cv2.imshow("Inter-Area", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()