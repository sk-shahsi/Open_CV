import cv2
import numpy as np

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")



threshold_value = 200

_,thresh_img = cv2.threshold( img,threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Binary Threshold", thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
