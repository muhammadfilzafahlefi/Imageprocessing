import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("asset/image3.png",1)
half = cv2.resize(image,(0,0), fx=0.1, fy=0.1)
bigger = cv2.resize(image, (1050,1620))
strech_near = cv2.resize(image,(780,540), interpolation=cv2.INTER_LINEAR)
Titles = ["Original", "Half", "Bigger","Interpolation Nearts"]
images = [image,half,bigger,strech_near]
count = 4
for i in range(count):
    plt.subplot(2,2,i+1)
    plt.title(Titles[i])
    plt.imshow(image[i])
plt.show()