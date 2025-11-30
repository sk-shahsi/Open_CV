import cv2
import numpy as np

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")
rows = img.shape[1]
column = img.shape[0]

center = (column/2,rows/2)

angle = 90

r = cv2.getRotationMatrix2D(center,angle,1)
rotate = cv2.warpAffine(img,r,(column,rows))

cv2.imshow("Rotate",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()