import cv2
import os

# Debugging
print("Current Path:", os.getcwd())

img = cv2.imread(r"C:/Users/eraas/Downloads/car_images.jpg")

if img is None:
    print("Error: Image not found or can't be opened!")
    exit()

scale = 50

width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)

dim = (width, height)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
print('Dimensions of Resize Images: ', resized.shape)

cv2.imshow('Original', img)
cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
