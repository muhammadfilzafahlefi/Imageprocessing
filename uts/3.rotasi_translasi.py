import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar berwarna
image = cv2.imread('asset/image3.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB untuk tampilan matplotlib

# 2. Translasi gambar sebesar 50 piksel ke kanan dan 30 piksel ke bawah
(h, w) = image.shape[:2]
translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])  # Translasi 50 piksel ke kanan dan 30 piksel ke bawah
translated_image = cv2.warpAffine(image_rgb, translation_matrix, (w, h))

# 3. Rotasi gambar sebesar 45 derajat searah jarum jam
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotasi 45 derajat
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (w, h))

# 4. Tampilkan gambar asli, hasil translasi, dan hasil rotasi secara berdampingan
plt.figure(figsize=(15, 5))

# Menampilkan gambar asli
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Gambar Asli')
plt.axis('off')

# Menampilkan hasil translasi
plt.subplot(1, 3, 2)
plt.imshow(translated_image)
plt.title('Hasil Translasi')
plt.axis('off')

# Menampilkan hasil rotasi
plt.subplot(1, 3, 3)
plt.imshow(rotated_image)
plt.title('Hasil Rotasi')
plt.axis('off')

# Menampilkan semua gambar
plt.tight_layout()
plt.show()
