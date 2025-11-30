import cv2
import numpy as np

image = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")
width = 600
height = 850

dim = (width, height)
resized = cv2.resize(image, dim)

kernel = np.ones((5,5),dtype ='uint8')


gradient = cv2.morphologyEx(resized, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("original",resized)

cv2.imshow("gradient",gradient)


cv2.waitKey(0)
cv2.destroyAllWindows()