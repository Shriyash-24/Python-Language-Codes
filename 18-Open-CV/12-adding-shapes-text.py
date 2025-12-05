import cv2
import numpy as np

img = cv2.imread('C:/Users/Shri/Coding/Additional-Files/bg.png', cv2.IMREAD_COLOR) # To read color
img = np.zeros(shape=[600,800,3], dtype='uint8') # Black screen.. 600,800 is dimension, 3 is to get color
img.fill(255) # Makes background white

# Line consists of 2 points.  Then color and thickness is mentioned.
cv2.line(img, (0,0), (150,150), (255,0,0), 2)

# Rectangle consists of 4 points, but we can give 2 points, top left, and bottom right. Then, color and thickness.
cv2.rectangle(img, (200,150), (250,300), (0,255,0), 3)

# Circle has center and radius with color snd thickness.
cv2.circle(img, (300,75), 70, (255,0,255), 3)

pts_polygon = np.array([[100,50],[100,300],[500,50],[500,300]], np.int32) # Store points in numpy array.
cv2.polylines(img, [pts_polygon], True, (0,0,255), 3) # pts, isClosed, color, thickness.

font = cv2.FONT_HERSHEY_DUPLEX # Picking the font.
cv2.putText(img, 'HELLO!', (10,500),font,3,(200,255,255),8,cv2.LINE_AA) # cv2. LINE_AA makes lines more smoother.

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
