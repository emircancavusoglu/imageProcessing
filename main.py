import cv2
import numpy as np


def trackChanged(x):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 250, 300)

lh = 0
ll = 0
ls = 0
uh = 179
ul = 255
us = 255

cv2.createTrackbar("LOWER-H", "Trackbars", 0, 179, trackChanged)
cv2.createTrackbar("LOWER-L", "Trackbars", 0, 255, trackChanged)
cv2.createTrackbar("LOWER-S", "Trackbars", 0, 255, trackChanged)

cv2.createTrackbar("UPPER-H", "Trackbars", 179, 179, trackChanged)
cv2.createTrackbar("UPPER-L", "Trackbars", 255, 255, trackChanged)
cv2.createTrackbar("UPPER-S", "Trackbars", 255, 255, trackChanged)

while True:
    img = cv2.imread("mobile.png")
    hls_image = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    lowerH = cv2.getTrackbarPos("LOWER-H", "Trackbars")
    lowerL = cv2.getTrackbarPos("LOWER-L", "Trackbars")
    lowerS = cv2.getTrackbarPos("LOWER-S", "Trackbars")

    upperH = cv2.getTrackbarPos("UPPER-H", "Trackbars")
    upperL = cv2.getTrackbarPos("UPPER-L", "Trackbars")
    upperS = cv2.getTrackbarPos("UPPER-S", "Trackbars")

    lowerHsl = np.array([lowerH, lowerL, lowerS], np.uint8)
    upperHsl = np.array([upperH, upperL, upperS], np.uint8)

    mask = cv2.inRange(hls_image, lowerHsl, upperHsl)

    sonuc = cv2.bitwise_and(hls_image, hls_image, mask=mask)

    cv2.imshow("hls_image", sonuc)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
