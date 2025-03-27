import os
from runLZ import run_lz77, run_lz78
from HA import count_symb, huffman_compress, huffman_decompress, save_compressed, load_compressed
from Reader import get_file_size, read_file, calculate_compression_ratio, analyze_compression, write_to_file, png_to_raw

counter = 0
print("test1 HA+LZ77 enwik7.txt")
path_to_input_file_enwik77 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt"
original_size_enwik7 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
run_lz77("compress", path_to_input_file_enwik77, "compressed_enwik77.lz77", 4096, 255)
text_enwik7 = read_file("compressed_enwik77.lz77")
compressed_bytes_enwik7, huffman_codes_enwik7 = huffman_compress(text_enwik7)
codes_size_enwik7, data_size_enwik7 = save_compressed(huffman_codes_enwik7, compressed_bytes_enwik7, "compressed.bin")
loaded_codes_enwik7, loaded_data_enwik7 = load_compressed("compressed.bin")
print("Huffman_coding completed")
compressed_size_enwik7 = get_file_size('compressed.bin')
ratio_enwik7 = calculate_compression_ratio(original_size_enwik7, compressed_size_enwik7)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'compressed.bin')
decompressed_enwik7 = huffman_decompress(loaded_data_enwik7, loaded_codes_enwik7)
# print(type(decompressed_enwik7))
write_to_file("decompressed_enwik7.txt", decompressed_enwik7)
path_to_input_file_enwik77_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_enwik7.txt"
run_lz77("decompress", path_to_input_file_enwik77_d, "output_enwik77.txt", 4096, 255)
print("Правильность декдирования: ", read_file(path_to_input_file_enwik77)==read_file("output_enwik77.txt"))
if read_file(path_to_input_file_enwik77)==read_file("output_enwik77.txt"):
    counter += 1
# ----------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ77 book.txt")
path_to_input_file_book = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt"
original_size_book = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
run_lz77("compress", path_to_input_file_book, "compressed_book.lz77", 4096, 255)
text_book = read_file("compressed_book.lz77")
compressed_bytes_book, huffman_codes_book = huffman_compress(text_book)
codes_size_book, data_size_book = save_compressed(huffman_codes_book, compressed_bytes_book, "compressed_book.bin")
loaded_codes_book, loaded_data_book = load_compressed("compressed_book.bin")
print("Huffman_coding completed")
compressed_size_book = get_file_size('compressed_book.bin')
ratio_book = calculate_compression_ratio(original_size_book, compressed_size_book)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'compressed_book.bin')
decompressed_book = huffman_decompress(loaded_data_book, loaded_codes_book)
# print(type(decompressed_enwik7))
write_to_file("decompressed_book.txt", decompressed_book)
path_to_input_file_book_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_book.txt"
run_lz77("decompress", path_to_input_file_book_d, "output_book.txt", 4096, 255)
print("Правильность декдирования: ", read_file(path_to_input_file_book)==read_file("output_book.txt"))
if read_file(path_to_input_file_book)==read_file("output_book.txt"):
    counter += 1
# ------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ77 binfile.bin")
path_to_input_file_bin = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin"
original_size_bin = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
run_lz77("compress", path_to_input_file_bin, "compressed_bin.lz77", 4096, 255)
text_bin = read_file("compressed_bin.lz77")
compressed_bytes_bin, huffman_codes_bin = huffman_compress(text_bin)
codes_size_bin, data_size_bin = save_compressed(huffman_codes_bin, compressed_bytes_bin, "compressed_bin.bin")
loaded_codes_bin, loaded_data_bin = load_compressed("compressed_bin.bin")
print("Huffman_coding completed")
compressed_size_bin = get_file_size('compressed_bin.bin')
ratio_bin = calculate_compression_ratio(original_size_bin, compressed_size_bin)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'compressed_bin.bin')
decompressed_bin = huffman_decompress(loaded_data_bin, loaded_codes_bin)
# print(type(decompressed_enwik7))
write_to_file("decompressed_bin.txt", decompressed_bin)
path_to_input_file_bin_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_bin.txt"
run_lz77("decompress", path_to_input_file_bin_d, "output_bin.txt", 4096, 255)
print("Правильность декдирования: ", read_file(path_to_input_file_bin)==read_file("output_bin.txt"))
if read_file(path_to_input_file_bin)==read_file("output_bin.txt"):
    counter += 1
# ------------------------------------------------------------------------------------------------------------------------------------
print("test4 HA+LZ77 img1.png")
png_img1 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.png"
png_to_raw(png_img1, "img1.raw")
original_size_img1 = get_file_size("img1.raw")
run_lz77("compress", "img1.raw", "compressed_img1.lz77", 4096, 255)
text_img1 = read_file("compressed_img1.lz77")
compressed_bytes_img1, huffman_codes_img1 = huffman_compress(text_img1)
codes_size_img1, data_size_img1 = save_compressed(huffman_codes_img1, compressed_bytes_img1, "compressed_img1.bin")
loaded_codes_img1, loaded_data_img1 = load_compressed("compressed_img1.bin")
print("Huffman_coding completed")
compressed_size_img1 = get_file_size('compressed_img1.bin')
ratio_img1 = calculate_compression_ratio(original_size_img1, compressed_size_img1)
analyze_compression("img1.raw", 'compressed_img1.bin')
decompressed_img1 = huffman_decompress(loaded_data_img1, loaded_codes_img1)
# print(type(decompressed_enwik7))
write_to_file("decompressed_img1.txt", decompressed_img1)
path_to_input_file_img1_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_img1.txt"
run_lz77("decompress", path_to_input_file_img1_d, "output_img1.txt", 4096, 255)
print("Правильность декдирования: ", read_file("img1.raw")==read_file("output_img1.txt"))
if read_file("img1.raw")==read_file("output_img1.txt"):
    counter += 1
# ------------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ77 img2.png")
png_img2 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.png"
png_to_raw(png_img2, "img2.raw")
original_size_img2 = get_file_size("img2.raw")
run_lz77("compress", "img2.raw", "compressed_img2.lz77", 4096, 255)
text_img2 = read_file("compressed_img2.lz77")
compressed_bytes_img2, huffman_codes_img2 = huffman_compress(text_img2)
codes_size_img2, data_size_img2 = save_compressed(huffman_codes_img2, compressed_bytes_img2, "compressed_img2.bin")
loaded_codes_img2, loaded_data_img2 = load_compressed("compressed_img2.bin")
print("Huffman_coding completed")
compressed_size_img2 = get_file_size('compressed_img2.bin')
ratio_img2 = calculate_compression_ratio(original_size_img2, compressed_size_img2)
analyze_compression("img2.raw", 'compressed_img2.bin')
decompressed_img2 = huffman_decompress(loaded_data_img2, loaded_codes_img2)
# print(type(decompressed_enwik7))
write_to_file("decompressed_img2.txt", decompressed_img2)
path_to_input_file_img2_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_img2.txt"
run_lz77("decompress", path_to_input_file_img2_d, "output_img2.txt", 4096, 255)
print("Правильность декдирования: ", read_file("img2.raw")==read_file("output_img2.txt"))
if read_file("img2.raw")==read_file("output_img2.txt"):
    counter += 1
# -----------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ77 img3.png")
png_img3 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.png"
png_to_raw(png_img3, "img3.raw")
original_size_img3 = get_file_size("img3.raw")
run_lz77("compress", "img3.raw", "compressed_img3.lz77", 4096, 255)
text_img3 = read_file("compressed_img3.lz77")
compressed_bytes_img3, huffman_codes_img3 = huffman_compress(text_img3)
codes_size_img3, data_size_img3 = save_compressed(huffman_codes_img3, compressed_bytes_img3, "compressed_img3.bin")
loaded_codes_img3, loaded_data_img3 = load_compressed("compressed_img3.bin")
print("Huffman_coding completed")
compressed_size_img3 = get_file_size('compressed_img3.bin')
ratio_img3 = calculate_compression_ratio(original_size_img3, compressed_size_img3)
analyze_compression("img3.raw", 'compressed_img3.bin')
decompressed_img3 = huffman_decompress(loaded_data_img3, loaded_codes_img3)
# print(type(decompressed_enwik7))
write_to_file("decompressed_img3.txt", decompressed_img3)
path_to_input_file_img3_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_img3.txt"
run_lz77("decompress", path_to_input_file_img3_d, "output_img3.txt", 4096, 255)
print("Правильность декдирования: ", read_file("img3.raw")==read_file("output_img3.txt"))
if read_file("img3.raw")==read_file("output_img3.txt"):
    counter += 1
if counter == 6:
    print('айлялюлю, все круто')
else:
    print("расстреливаем всех")
counter78 = 0
print("test1 HA+LZ78 enwik7.txt")
path_to_input_file_enwik78 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt"
original_size_enwik78 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
run_lz78("compress", path_to_input_file_enwik78, "compressed_enwik78.lz78")
text_enwik78 = read_file("compressed_enwik78.lz78")
compressed_bytes_enwik78, huffman_codes_enwik78 = huffman_compress(text_enwik78)
codes_size_enwik78, data_size_enwik78 = save_compressed(huffman_codes_enwik78, compressed_bytes_enwik78, "compressed78.bin")
loaded_codes_enwik78, loaded_data_enwik78 = load_compressed("compressed78.bin")
print("Huffman_coding completed")
compressed_size_enwik78 = get_file_size('compressed78.bin')
ratio_enwik78 = calculate_compression_ratio(original_size_enwik78, compressed_size_enwik78)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'compressed78.bin')
decompressed_enwik78 = huffman_decompress(loaded_data_enwik78, loaded_codes_enwik78)
# print(type(decompressed_enwik7))
write_to_file("decompressed_enwik78.txt", decompressed_enwik78)
path_to_input_file_enwik78_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_enwik78.txt"
run_lz78("decompress", path_to_input_file_enwik78_d, "output_enwik78.txt")
print("Правильность декдирования: ", read_file(path_to_input_file_enwik78)==read_file("output_enwik78.txt"))
if read_file(path_to_input_file_enwik78)==read_file("output_enwik78.txt"):
    counter78 += 1
# ----------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ78 book.txt")
path_to_input_file_book78 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt"
original_size_book78 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
run_lz78("compress", path_to_input_file_book78, "compressed_book78.lz78")
text_book78 = read_file("compressed_book78.lz78")
compressed_bytes_book78, huffman_codes_book78 = huffman_compress(text_book78)
codes_size_book78, data_size_book78 = save_compressed(huffman_codes_book78, compressed_bytes_book78, "compressed_book78.bin")
loaded_codes_book78, loaded_data_book78 = load_compressed("compressed_book78.bin")
print("Huffman_coding completed")
compressed_size_book78 = get_file_size('compressed_book78.bin')
ratio_book78 = calculate_compression_ratio(original_size_book78, compressed_size_book78)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'compressed_book78.bin')
decompressed_book78 = huffman_decompress(loaded_data_book78, loaded_codes_book78)
# print(type(decompressed_enwik7))
write_to_file("decompressed_book78.txt", decompressed_book78)
path_to_input_file_book78_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_book78.txt"
run_lz78("decompress", path_to_input_file_book78_d, "output_book78.txt")
print("Правильность декдирования: ", read_file(path_to_input_file_book78)==read_file("output_book78.txt"))
if read_file(path_to_input_file_book78)==read_file("output_book78.txt"):
    counter78 += 1
# ------------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ78 binfile.bin")
path_to_input_file_bin78 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin"
original_size_bin78 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
run_lz78("compress", path_to_input_file_bin78, "compressed_bin78.lz78")
text_bin78 = read_file("compressed_bin78.lz78")
compressed_bytes_bin78, huffman_codes_bin78 = huffman_compress(text_bin78)
codes_size_bin78, data_size_bin78 = save_compressed(huffman_codes_bin78, compressed_bytes_bin78, "compressed_bin78.bin")
loaded_codes_bin78, loaded_data_bin78 = load_compressed("compressed_bin78.bin")
print("Huffman_coding completed")
compressed_size_bin78 = get_file_size('compressed_bin78.bin')
ratio_bin = calculate_compression_ratio(original_size_bin78, compressed_size_bin78)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'compressed_bin78.bin')
decompressed_bin78 = huffman_decompress(loaded_data_bin78, loaded_codes_bin78)
# print(type(decompressed_enwik7))
write_to_file("decompressed_bin78.txt", decompressed_bin78)
path_to_input_file_bin78_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_bin78.txt"
run_lz78("decompress", path_to_input_file_bin78_d, "output_bin78.txt")
print("Правильность декдирования: ", read_file(path_to_input_file_bin78)==read_file("output_bin78.txt"))
if read_file(path_to_input_file_bin78)==read_file("output_bin78.txt"):
    counter78 += 1
# ------------------------------------------------------------------------------------------------------------------------------------
print("test4 HA+LZ78 img1.png")
png_img178 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.png"
png_to_raw(png_img178, "img178.raw")
original_size_img178 = get_file_size("img178.raw")
run_lz78("compress", "img178.raw", "compressed_img178.lz78")
text_img178 = read_file("compressed_img178.lz78")
compressed_bytes_img178, huffman_codes_img178 = huffman_compress(text_img178)
codes_size_img178, data_size_img178 = save_compressed(huffman_codes_img178, compressed_bytes_img178, "compressed_img178.bin")
loaded_codes_img178, loaded_data_img178 = load_compressed("compressed_img178.bin")
print("Huffman_coding completed")
compressed_size_img178 = get_file_size('compressed_img178.bin')
ratio_img178 = calculate_compression_ratio(original_size_img178, compressed_size_img178)
analyze_compression("img178.raw", 'compressed_img178.bin')
decompressed_img178 = huffman_decompress(loaded_data_img178, loaded_codes_img178)
# print(type(decompressed_enwik7))
write_to_file("decompressed_img178.txt", decompressed_img178)
path_to_input_file_img178_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_img178.txt"
run_lz78("decompress", path_to_input_file_img178_d, "output_img178.txt")
print("Правильность декдирования: ", read_file("img178.raw")==read_file("output_img178.txt"))
if read_file("img178.raw")==read_file("output_img178.txt"):
    counter78 += 1
# ------------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ78 img2.png")
png_img278 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.png"
png_to_raw(png_img278, "img278.raw")
original_size_img278 = get_file_size("img278.raw")
run_lz78("compress", "img278.raw", "compressed_img278.lz78")
text_img278 = read_file("compressed_img278.lz78")
compressed_bytes_img278, huffman_codes_img278 = huffman_compress(text_img278)
codes_size_img278, data_size_img278 = save_compressed(huffman_codes_img278, compressed_bytes_img278, "compressed_img278.bin")
loaded_codes_img278, loaded_data_img278 = load_compressed("compressed_img278.bin")
print("Huffman_coding completed")
compressed_size_img278 = get_file_size('compressed_img278.bin')
ratio_img278 = calculate_compression_ratio(original_size_img278, compressed_size_img278)
analyze_compression("img278.raw", 'compressed_img278.bin')
decompressed_img278 = huffman_decompress(loaded_data_img278, loaded_codes_img278)
# print(type(decompressed_enwik7))
write_to_file("decompressed_img278.txt", decompressed_img278)
path_to_input_file_img278_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_img278.txt"
run_lz78("decompress", path_to_input_file_img278_d, "output_img278.txt")
print("Правильность декдирования: ", read_file("img278.raw")==read_file("output_img278.txt"))
if read_file("img278.raw")==read_file("output_img278.txt"):
    counter78 += 1
# -----------------------------------------------------------------------------------------------------------------------------------
print("test1 HA+LZ77 img3.png")
png_img378 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.png"
png_to_raw(png_img378, "img378.raw")
original_size_img378 = get_file_size("img378.raw")
run_lz78("compress", "img378.raw", "compressed_img378.lz78")
text_img378 = read_file("compressed_img378.lz78")
compressed_bytes_img378, huffman_codes_img378 = huffman_compress(text_img378)
codes_size_img378, data_size_img378 = save_compressed(huffman_codes_img378, compressed_bytes_img378, "compressed_img378.bin")
loaded_codes_img378, loaded_data_img378 = load_compressed("compressed_img378.bin")
print("Huffman_coding completed")
compressed_size_img378 = get_file_size('compressed_img378.bin')
ratio_img378 = calculate_compression_ratio(original_size_img378, compressed_size_img378)
analyze_compression("img378.raw", 'compressed_img378.bin')
decompressed_img378 = huffman_decompress(loaded_data_img378, loaded_codes_img378)
# print(type(decompressed_enwik7))
write_to_file("decompressed_img378.txt", decompressed_img378)
path_to_input_file_img378_d = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/HA+LZ/decompressed_img378.txt"
run_lz78("decompress", path_to_input_file_img378_d, "output_img378.txt")
print("Правильность декдирования: ", read_file("img378.raw")==read_file("output_img378.txt"))
if read_file("img378.raw")==read_file("output_img378.txt"):
    counter78 += 1
if counter78 == 6:
    print('айлялюлю, все круто')
else:
    print("расстреливаем всех")