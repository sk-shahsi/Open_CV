import cv2
import numpy as np

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")
resize = cv2.resize(img,(460,640))

ksize = (7,7)

sigmax= 0
sigmay= 0

blur = cv2.GaussianBlur(resize,ksize,sigmax)

cv2.imshow("Input",resize)

cv2.imshow("GaussianBlur", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
