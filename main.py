import cv2
import numpy as np

img = cv2.imread("mobile.png")
img = cv2.resize(img,None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)
cv2.imshow("mobil", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
