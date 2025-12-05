import cv2
import numpy as np

img = cv2.imread('C:/Users/Shri/Coding/Additional-Files/bg.png')
width = 740
height = 493
dim = (width, height)
resized = cv2.resize(img, dim) # Resized image.

kernel = np.ones((5,5), dtype='uint8') # 5x5 matrix, dtype is unsigned int 8 bytes.

erosion = cv2.erode(resized, kernel, iterations = 1)
# iterations means how many times the image should be eroded.

dilation = cv2.dilate(erosion, kernel, iterations = 1)

opening = cv2.morphologyEx(resized, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(resized, cv2.MORPH_CLOSE, kernel)
morphological_gradient = cv2.morphologyEx(resized, cv2.MORPH_GRADIENT, kernel)
top_hat = cv2.morphologyEx(resized, cv2.MORPH_TOPHAT, kernel)
black_hat = cv2.morphologyEx(resized, cv2.MORPH_BLACKHAT, kernel)


cv2.imshow('Original', resized)
cv2.imshow('Eroded', erosion)
cv2.imshow('Dilated', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Morphological Gradient', morphological_gradient)
cv2.imshow('Top hat', top_hat)
cv2.imshow('Black hat', black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
