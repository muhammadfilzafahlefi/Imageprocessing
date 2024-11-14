from PIL import Image

# Membuka gambar dari file
image = Image.open('asset/image2.jpg')

# Memutar gambar dengan sudut 45 derajat, dan mengisi area kosong dengan warna putih
rotated_image = image.rotate(45, expand=True, fillcolor='#fff')

# Menyimpan gambar hasil rotasi
rotated_image.save('output_rotated.jpg')

# Menampilkan gambar asli dan gambar hasil rotasi
image.show()
rotated_image.show()

