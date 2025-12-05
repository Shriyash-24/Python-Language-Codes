# Blurring the image.
# Blurring works by looking at each pixel and replacing it with an average of its neighbors.
# A kernel is a small grid of numbers.
# A Gaussian kernel uses a bell-shaped curve (Gaussian distribution).
# Gives high importance to center pixels and low to far pixels.

import cv2
img = cv2.imread("C:/Users/Shri/Coding/Additional-Files/bg.png")
resize = cv2.resize(img,(740,493))

ksize = (7,1) # ksize is kernel size, it should be +ve and odd.
# kernel size = width x height of the window used for blurring.
# Width = 7, Height = 1 --> Horizontal blur.
# ← ← ← center → → →
# Odd width so center pixel should be there.
# Odd height so blur is symmetric.

# Sigma means how much to spread the gaussian blur.
# 0 means automatically.
sigmax = 0
sigmay = 0


blur = cv2.GaussianBlur(resize,ksize,0)
cv2.imshow("Output", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
