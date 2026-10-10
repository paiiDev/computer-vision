import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('images/atomic-habits-dots.png', 0)
cv2.imshow('image',img)
key=cv2.waitKey(0)
if key==ord('s'):
 cv2.imwrite("images/xss.png", img)
 cv2.waitKey(0)
cv2.destroyAllWindows()