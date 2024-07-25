import cv2
from PIL import Image
image = Image.open('asset/image3.png')
image.show()
cropped = (100,150,280,400)
img_crop = image.crop(cropped)
img_crop.show()