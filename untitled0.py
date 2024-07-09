import numpy as np
import cv2

img = cv2.imread("high_jump.bmp",-1)
cv2.imshow("Example",img)

r = np.zeros_like(img)
g = np.zeros_like(img)
b = np.zeros_like(img)

r[:,:,2] = img[:,:,2]
g[:,:,1] = img[:,:,1]
b[:,:,0] = img[:,:,0]

cv2.imshow("r", r)
cv2.imshow("g", g)
cv2.imshow("b", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
