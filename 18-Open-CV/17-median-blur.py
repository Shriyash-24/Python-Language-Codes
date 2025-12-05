# Median Blur - Median blur is a type of smoothing that replaces each pixel with the median value of its surrounding pixels.

import cv2
img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png")
resize = cv2.resize(img,(740,493))

kernel = 3
# A 3x3 neighbourhood for each pixel.
# [ p1 p2 p3 ]
# [ p4 PC p6 ]
# [ p7 p8 p9 ]

# Kernel size should be odd.
blur = cv2.medianBlur(resize,kernel)

cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()