import cv2

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")

resize = cv2.resize(img,(520,520))

d = 7
sigma_color = 100
sigma_space = 100

b= cv2.bilateralFilter(resize,d,sigma_color,sigma_space)

cv2.imshow('Input',resize)
cv2.imshow('Output',b)
cv2.waitKey(0)
cv2.destroyAllWindows()