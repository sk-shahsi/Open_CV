import cv2
#Canny Edge Detection

#1 Noise reduction
#2Intensity of the gradient of the images
#3Non-maximum suppression
#Threshold

img = cv2.imread("C:/Users/eraas/Downloads/car_images.jpg",0)
resize = cv2.resize(img,(520,520))
min_threash = 100
max_threash = 200

edges = cv2.Canny(resize,min_threash,max_threash)

cv2.imshow('Original',resize)
cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

