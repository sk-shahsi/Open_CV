import cv2

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg")
print("Dimension of images:",img.shape)

width =img.shape[1]
height = 400
dim = (width, height)
resized = cv2.resize(img, dim)

cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
