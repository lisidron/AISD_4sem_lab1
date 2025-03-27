import matplotlib.pyplot as plt

buffer_sizes = [512, 1024, 2048, 4096, 8192, 16384]
compression_ratios = {
    "Enwik7": [0.964, 1.083, 1.204, 1.333, 1.466, 1.610],
    "Book.txt": [1.230, 1.419, 1.610, 1.803, 2.005, 2.216],
    "Binfile.bin": [0.893, 1.005, 1.111, 1.230, 1.326, 1.416],
    "Img1.raw": [0.920, 0.987, 1.101, 1.577, 1.753, 1.897],
    "Img2.raw": [1.140, 1.223, 1.320, 2.246, 2.442, 2.640],
    "Img3.raw": [0.912, 0.961, 1.012, 1.376, 1.456, 1.539]
}
plt.figure(figsize=(10, 6))
for file, ratios in compression_ratios.items():
    plt.plot(buffer_sizes, ratios, marker='o', linestyle='-', label=file)

plt.xlabel('Размер буфера')
plt.ylabel('Коэффициент сжатия')
plt.title('Зависимость коэффициента сжатия от размера буфера (LZ77)')
plt.grid(True)
plt.legend()
plt.show()
