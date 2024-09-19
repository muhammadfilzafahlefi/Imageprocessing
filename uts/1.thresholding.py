import cv2
import matplotlib.pyplot as plt

# 1. Membaca gambar dalam format grayscale
image = cv2.imread('asset/image3.png', cv2.IMREAD_GRAYSCALE)

# 2. Terapkan thresholding menggunakan metode Otsu's Thresholding
# Threshold Otsu secara otomatis menentukan nilai threshold optimal
ret, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 3. Tampilkan gambar asli dan hasil thresholding secara berdampingan
plt.figure(figsize=(10, 5))

# Menampilkan gambar asli
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Gambar Asli')
plt.axis('off')

# Menampilkan gambar hasil thresholding
plt.subplot(1, 2, 2)
plt.imshow(thresholded, cmap='gray')
plt.title('Hasil Thresholding (Otsu)')
plt.axis('off')

# Menampilkan gambar
plt.tight_layout()
plt.show()
