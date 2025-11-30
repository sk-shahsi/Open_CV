import cv2
import numpy as np

image = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")
width = 600
height = 850

dim = (width, height)
resized = cv2.resize(image, dim)

kernel = np.ones((5,5),dtype ='uint8')

tophat = cv2.morphologyEx(resized, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(resized, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("original",resized)


cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()