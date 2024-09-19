import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar berwarna
image = cv2.imread('asset/image3.png')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB untuk tampilan matplotlib

# 2. Terapkan Gaussian Blur pada gambar
blurred_image = cv2.GaussianBlur(image_rgb, (15, 15), 0)  # Menggunakan kernel 15x15 untuk blur

# 3. Terapkan sharpening menggunakan kernel khusus
# Kernel sharpening untuk meningkatkan ketajaman gambar
sharpening_kernel = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])
sharpened_image = cv2.filter2D(image_rgb, -1, sharpening_kernel)

# 4. Tampilkan gambar asli, hasil Gaussian Blur, dan hasil sharpening secara berdampingan
plt.figure(figsize=(15, 5))

# Menampilkan gambar asli
plt.subplot(1, 3, 1)
plt.imshow(image_rgb)
plt.title('Gambar Asli')
plt.axis('off')

# Menampilkan hasil Gaussian Blur
plt.subplot(1, 3, 2)
plt.imshow(blurred_image)
plt.title('Hasil Gaussian Blur')
plt.axis('off')

# Menampilkan hasil sharpening
plt.subplot(1, 3, 3)
plt.imshow(sharpened_image)
plt.title('Hasil Sharpening')
plt.axis('off')

# Menampilkan semua gambar
plt.tight_layout()
plt.show()
