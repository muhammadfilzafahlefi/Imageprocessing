import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar dalam format grayscale
image = cv2.imread('asset/image3.png', cv2.IMREAD_GRAYSCALE)

# 2. Hitung histogram intensitas gambar asli
hist_original = cv2.calcHist([image], [0], None, [256], [0, 256])

# 3. Terapkan equalisasi histogram
equalized_image = cv2.equalizeHist(image)

# Hitung histogram intensitas gambar setelah equalisasi
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# 4. Tampilkan gambar asli dan hasil equalization serta histogramnya
plt.figure(figsize=(15, 8))

# Menampilkan gambar asli
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Gambar Asli')
plt.axis('off')

# Menampilkan histogram gambar asli
plt.subplot(2, 2, 2)
plt.plot(hist_original, color='black')
plt.title('Histogram Gambar Asli')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Jumlah Pixel')

# Menampilkan gambar hasil equalisasi histogram
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Gambar Hasil Equalisasi')
plt.axis('off')

# Menampilkan histogram gambar hasil equalisasi
plt.subplot(2, 2, 4)
plt.plot(hist_equalized, color='black')
plt.title('Histogram Gambar Equalisasi')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Jumlah Pixel')

# Menampilkan semua grafik
plt.tight_layout()
plt.show()

