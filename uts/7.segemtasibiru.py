import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar berwarna
image = cv2.imread('asset/image3.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB untuk tampilan matplotlib

# 2. Konversikan gambar ke ruang warna HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. Buat masker untuk mendeteksi objek dengan warna biru
# Rentang warna biru dalam ruang HSV
lower_blue = np.array([100, 150, 50])  # Batas bawah untuk warna biru
upper_blue = np.array([140, 255, 255])  # Batas atas untuk warna biru

# Masker untuk deteksi warna biru
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# 4. Terapkan masker pada gambar asli untuk memisahkan objek berwarna biru
segmented_image = cv2.bitwise_and(image_rgb, image_rgb, mask=mask)

# 5. Tampilkan gambar asli dan hasil segmentasi secara berdampingan
plt.figure(figsize=(12, 6))

# Menampilkan gambar asli
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Gambar Asli')
plt.axis('off')

# Menampilkan hasil segmentasi
plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title('Hasil Segmentasi Warna Biru')
plt.axis('off')

# Menampilkan semua gambar
plt.tight_layout()
plt.show()
