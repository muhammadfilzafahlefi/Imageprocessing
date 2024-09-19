import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar dalam grayscale
image = cv2.imread('asset/image3.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. Lakukan thresholding untuk menghasilkan gambar biner
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# 3. Deteksi kontur menggunakan cv2.findContours()
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. Gambar kontur pada gambar asli
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Gambar kontur dengan warna hijau dan ketebalan 2

# Konversi gambar untuk tampilan menggunakan matplotlib (BGR ke RGB)
contour_image_rgb = cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB)

# Tampilkan gambar asli dan gambar dengan kontur
plt.figure(figsize=(10, 5))

# Menampilkan gambar asli
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

# Menampilkan gambar dengan kontur
plt.subplot(1, 2, 2)
plt.imshow(contour_image_rgb)
plt.title('Gambar dengan Kontur')
plt.axis('off')

# Menampilkan semua gambar
plt.tight_layout()
plt.show()
