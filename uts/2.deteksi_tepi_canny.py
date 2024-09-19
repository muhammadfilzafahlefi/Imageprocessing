import cv2
import matplotlib.pyplot as plt

# 1. Membaca gambar dalam format grayscale
image = cv2.imread('asset/grayscale.png', cv2.IMREAD_GRAYSCALE)

# 2. Terapkan Gaussian Blur untuk mengurangi noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# 3. Deteksi tepi menggunakan Canny Edge Detection
edges = cv2.Canny(blurred, 100, 200)  # 100 dan 200 adalah nilai threshold rendah dan tinggi

# 4. Tampilkan gambar hasil deteksi tepi
plt.figure(figsize=(8, 6))

# Menampilkan gambar hasil deteksi tepi
plt.imshow(edges, cmap='gray')
plt.title('Deteksi Tepi Menggunakan Canny Edge Detection')
plt.axis('off')

# Menampilkan gambar
plt.show()
