import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar berwarna
image = cv2.imread('asset/image3.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB untuk tampilan matplotlib

# 2. Konversikan gambar ke ruang warna HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. Buat masker untuk mendeteksi objek dengan warna tertentu (misalnya merah)
# Rentang warna merah dalam ruang HSV
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

# Masker untuk deteksi warna merah
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# 4. Terapkan masker pada gambar asli untuk memisahkan objek berwarna merah
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
plt.title('Hasil Segmentasi Warna Merah')
plt.axis('off')

# Menampilkan semua gambar
plt.tight_layout()
plt.show()
