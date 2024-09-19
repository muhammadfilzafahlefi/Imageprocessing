import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar dalam format grayscale
image = cv2.imread('asset/image3.png', cv2.IMREAD_GRAYSCALE)

# Terapkan thresholding untuk membuat gambar menjadi biner
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 2. Definisikan kernel untuk operasi morfologi
kernel = np.ones((5, 5), np.uint8)  # Kernel 5x5 untuk operasi erosi dan dilasi

# Terapkan operasi erosi
eroded_image = cv2.erode(binary_image, kernel, iterations=1)

# Terapkan operasi dilasi
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

# 3. Tampilkan gambar asli, hasil erosi, dan hasil dilasi secara berdampingan
plt.figure(figsize=(15, 5))

# Menampilkan gambar asli (biner)
plt.subplot(1, 3, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Gambar Biner Asli')
plt.axis('off')

# Menampilkan hasil erosi
plt.subplot(1, 3, 2)
plt.imshow(eroded_image, cmap='gray')
plt.title('Hasil Erosi')
plt.axis('off')

# Menampilkan hasil dilasi
plt.subplot(1, 3, 3)
plt.imshow(dilated_image, cmap='gray')
plt.title('Hasil Dilasi')
plt.axis('off')

# Menampilkan semua gambar
plt.tight_layout()
plt.show()
