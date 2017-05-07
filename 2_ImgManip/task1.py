import cv2
import numpy as np


img = cv2.imread('A.png',0)
img2 = img.copy()

# Simple Thresholding
img2[img>127]=255
img2[img<=127]=0

# Dilation and Erosion
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 2)
dilation = cv2.dilate(img,kernel,iterations = 2)

out = np.hstack([img,img2,erosion,dilation])
cv2.imwrite('out.jpg',out)
