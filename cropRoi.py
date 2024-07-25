import cv2
image = cv2.imread('asset/image3.png')
cv2.imshow('Original image',image)
x , y , w , h = 100,180,100,140
cropped = image[y:y+h, x:x+w] 
cv2.imshow('Crop Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()