from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
image = Image.open('asset/image2.jpg')
plt.imshow(image, cmap=cm.gray)
plt.show()