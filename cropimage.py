import cv2
image = cv2.imread('asset/image3.png')
cv2.imshow('Original image',image)
cropped = image[150:300, 400:800] 
cv2.imshow('Crop Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()