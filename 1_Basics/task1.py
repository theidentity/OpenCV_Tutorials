import cv2
import numpy as np

img = cv2.imread('1.png')
print(img.shape)

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(grey.shape)

b,g,r = cv2.split(img)
print(b.shape)
print(g.shape)
print(r.shape)

out = np.vstack([grey,b,g,r])
cv2.imwrite('out.jpg',out)
