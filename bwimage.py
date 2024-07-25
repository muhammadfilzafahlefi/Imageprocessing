import cv2
import os
from datetime import datetime

# Memuat gambar dari file
image = cv2.imread('asset/image3.png')

# Menampilkan gambar asli
cv2.imshow('Original image', image)

# Mengonversi gambar ke skala abu-abu
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)

# Menerapkan threshold untuk membuat gambar hitam-putih
(th, bw) = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('BW Image', bw)

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
cv2.imwrite(os.path.join(output_folder, f'{timestamp}_bw.png'), bw)

print(f"Gambar telah disimpan ke folder '{output_folder}' dengan timestamp {timestamp}.")


