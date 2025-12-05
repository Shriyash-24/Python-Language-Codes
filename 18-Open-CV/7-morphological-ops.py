# Morphological Operations - Processing images based on shapes and edges.
# Erosion - Removes pixels on foreground objects. cv2.erode() function is used.
# Dilation - Adds pixels, cv2.dilate() function
# Opening - Erosion followed by dilation.cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# Closing - Dilation followed by Erosion. cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# Morphological Gradient - Difference between dilation and erosion. cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# Top Hat - Diff. between input image and opening of image. cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# Black Hat - Diff. between closing of input image and input image. cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Kernel - Changing value of pixel.
# CONVOLUTION - When kernel is applied to every pixel in the image one by one to produce the final image.
# There is a image matrix and kernel matrix. When you change kernel matrix the changes directs to image matrix.

# DATA TYPES OF IMAGE -->
# 1. uint is the most used one.
# 2. signed, unsigned, floating point.
# UnSigned --> No Negative
# Signed --> Negative & Positive.
# If Image --> 8-bit, unsigned it is displayed as it is.
# If Image --> 16-bit unsigned/ 32-bit unsigned, pixel --> divided by 256, range[0,255]
# If Image --> 32-bit floating point, pixel --> Multiplied by 256, range[0:1]
