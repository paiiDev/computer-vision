import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('images/atomic-habits-dots.png', 0)
cv2.imshow('image',img)
key=cv2.waitKey(0)
if key==ord('s'):
 img2 = cv2.imread("images/xss.png", 0)
 cv2.imshow('image2',img2)
 cv2.waitKey(0)
cv2.destroyAllWindows()