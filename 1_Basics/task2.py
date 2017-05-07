import cv2
import numpy as np


out = cv2.imread('out.jpg',0)
h,w = out.shape

# Converting from gray to bgr
shape = h,w,3
bgr = np.zeros(shape,dtype=out.dtype)
bgr[:,:,0] = out
bgr[:,:,1] = out
bgr[:,:,2] = out
print(bgr.shape)

crop_bgr = bgr[h/4:,:,:]
# Writing Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(crop_bgr,"Blue",(300,100),font,1,(255,0,0),2,cv2.LINE_AA)
cv2.putText(crop_bgr,"Green",(300,250),font,1,(0,255,0),2,cv2.LINE_AA)
cv2.putText(crop_bgr,"Red",(300,500),font,1,(0,0,255),2,cv2.LINE_AA)
cv2.imwrite('crop_bgr.jpg',crop_bgr)
