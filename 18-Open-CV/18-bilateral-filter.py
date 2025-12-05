# DETECTS EDGES AND SMOOTHENS
# 1. src -> INPUT
# 2. d -> diameter of pixel neighbourhood.
# 3. Sigma color -->
# 4. Sigma space --> Depends on d. If d increases it mixes with each other.
# Bilateral filter depends on Gaussian blur.
import cv2
img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png")

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(img, d, sigmacolor, sigmaspace)

cv2.imshow("original",img)
cv2.imshow("Output", b)

cv2.waitKey(0)
cv2.destroyAllWindows()