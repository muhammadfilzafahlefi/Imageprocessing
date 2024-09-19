import cv2
import os
from datetime import datetime

# 1. Membaca dan Menampilkan Citra
image = cv2.imread('asset/image10.jpg')
cv2.imshow('Original image', image)

# 2. Konversi Gambar Berwarna ke Grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)

# 3. Pendeteksian Tepi dengan Canny Edge Detection
edges = cv2.Canny(grayscale, 100, 200)
cv2.imshow('Canny Edge Detection', edges)

# 4. Mengubah Ukuran Gambar (Resizing)
resized = cv2.resize(image, (400, 300))  # Resize image to 400x300 pixels
cv2.imshow('Resized image', resized)

# 5. Memutar Gambar (Rotation)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotasi 45 derajat
rotated = cv2.warpAffine(image, matrix, (w, h))
cv2.imshow('Rotated image', rotated)

# Menunggu input dari pengguna untuk menutup jendela gambar
cv2.waitKey(0)
cv2.destroyAllWindows()

# Tentukan folder tujuan
output_folder = 'store'

# Buat folder jika belum ada
os.makedirs(output_folder, exist_ok=True)

# Dapatkan timestamp saat ini
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

# Simpan gambar ke folder yang ditentukan dengan nama berdasarkan timestamp
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_original.png'), image)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_grayscale.png'), grayscale)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_canny.png'), edges)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_resized.png'), resized)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_rotated.png'), rotated)

print(f"Gambar telah disimpan ke folder '{output_folder}' dengan timestamp {timestamp}.")
