import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar berwarna
image = cv2.imread("asset/image3.png", 1)

# Mengubah ukuran gambar
half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)  # Mengurangi ukuran gambar 10%
bigger = cv2.resize(image, (1650, 1320))          # Memperbesar gambar ke ukuran tertentu
strech_near = cv2.resize(image, (780, 540), interpolation=cv2.INTER_LINEAR)  # Stretch gambar

# Daftar judul dan gambar
Titles = ["Original", "Half", "Bigger", "Interpolation Linear"]
images = [image, half, bigger, strech_near]

# Menampilkan gambar
count = 4
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    # Konversi BGR ke RGB untuk ditampilkan dengan matplotlib
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Menghilangkan sumbu

# Menampilkan plot
plt.tight_layout()
plt.show()
