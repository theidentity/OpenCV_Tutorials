import cv2
import numpy as np


noise_img = cv2.imread('A_noise.png',0)
holes_img = cv2.imread('A_closing.png',0)

# Opening - erosion followed by dilation
# Useful in removing noise
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(noise_img, cv2.MORPH_OPEN, kernel)
opening_result = np.hstack([noise_img,opening])

# Closing - dilation followed by erosion
# Useful in closing holes
kernel = np.ones((20,20),np.uint8)
closing = cv2.morphologyEx(holes_img, cv2.MORPH_CLOSE, kernel)
closing_result = np.hstack([holes_img,closing])

out = np.vstack([opening_result,closing_result])
cv2.imwrite('out2.jpg',out)
