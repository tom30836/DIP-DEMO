import numpy as np
import cv2

img = cv2.imread("Breakfast.bmp",-1)

o = img[110:342,455:690,:]
r = np.zeros_like(o)
g = np.zeros_like(o)
b = np.zeros_like(o)

r[:,:,2] = img[110:342,455:690,2]
g[:,:,1] = img[110:342,455:690,1]
b[:,:,0] = img[110:342,455:690,0]

A = np.concatenate((o,g),axis=0)
B = np.concatenate((r,b),axis=0)
C = np.concatenate((A,B),axis=1)

cv2.imshow("RGB",C)

cv2.rectangle(img,(690,342),(455,110),(255,0,0),cv2.LINE_AA)
cv2.putText(img, "latte", (455,110), cv2.FONT_HERSHEY_COMPLEX , 1, (0,255,0),2)
cv2.imshow("Example",img)

cv2.waitKey(0)
cv2.destroyAllWindows()