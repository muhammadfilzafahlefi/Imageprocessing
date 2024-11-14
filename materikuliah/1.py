import cv2
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca dan Menampilkan Citra
image = cv2.imread('asset/image3.png')
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

# 5. Memutar Gambar (Rotation 45 derajat)
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotasi 45 derajat
rotated_45 = cv2.warpAffine(image, matrix, (w, h))
cv2.imshow('Rotated image 45 degrees', rotated_45)

# 6. Memutar Gambar (Rotation 90 derajat)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)  # Rotasi 90 derajat
rotated_90 = cv2.warpAffine(image, matrix, (w, h))
cv2.imshow('Rotated image 90 degrees', rotated_90)

# 7. Memperbesar dan Memperkecil Gambar (Scaling)
# Skala memperbesar (1.5x)
scaled_up = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Scaled Up image (1.5x)', scaled_up)

# Skala memperkecil (0.5x)
scaled_down = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Scaled Down image (0.5x)', scaled_down)

# 8. Menambahkan Efek Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow('Half image', blurred)

# 9. Menampilkan Gambar dengan Matplotlib
# Mengubah ukuran gambar dengan berbagai skala
half = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)  # Mengurangi ukuran gambar 10%
bigger = cv2.resize(image, (1620, 1050))          # Memperbesar gambar ke ukuran tertentu
strech_near = cv2.resize(image, (780, 540), interpolation=cv2.INTER_LINEAR)  # Stretch gambar

# Daftar judul dan gambar
Titles = ["Original", "Half", "Bigger", "Interpolation Linear"]
images = [image, half, bigger, strech_near]

# Menampilkan gambar menggunakan matplotlib
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
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_rotated_45.png'), rotated_45)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_rotated_90.png'), rotated_90)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_scaled_up.png'), scaled_up)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_scaled_down.png'), scaled_down)
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_half.png'), blurred)

print(f"Gambar telah disimpan ke folder '{output_folder}' dengan timestamp {timestamp}.")
