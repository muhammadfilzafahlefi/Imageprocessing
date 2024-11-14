import cv2
image = cv2.imread('asset/image2.jpg')
cv2.imshow('Original image',image)
grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()