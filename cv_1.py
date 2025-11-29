import cv2
#reading images
img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg",0)

cv2.imshow("window",img)
cv2.imwrite('car_images.jpg',img)

cv2.waitKey(0)

cv2.destroyAllWindows()