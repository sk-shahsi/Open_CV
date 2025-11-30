import cv2

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")

width = 600
height = 850

dim = (width,height)

resized = cv2.resize(img,dim)
print('size in bytes: ',img.size)
cv2.imshow('Original',resized)

flip_2 = cv2.flip(resized,-2)
cv2.imshow('Horizontial & Vertiacal',flip_2)

cv2.waitKey(0)
cv2.destroyAllWindows()