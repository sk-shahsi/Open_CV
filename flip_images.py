import cv2

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")

width = 600

height = 850
dim = (width, height)

resized = cv2.resize(img,dim)

cv2.imshow("resized",resized)

# flip =cv2.flip(resized,1)

flip_1 = cv2.flip(resized,0)
cv2.imshow("flip_1",flip_1)

# cv2.imshow('Horizontial',flip)

cv2.waitKey(0)
cv2.destroyAllWindows()
