import sys
from collections import deque
from BWT.BWT import generate_bwt_suffix_array,revert_bwt, process_bwt_blocks, restore_bwt_blocks
from Reader import get_file_size, calculate_compression_ratio, read_file, write_to_file, analyze_file, analyze_compression, png_to_raw
from HA import count_symb, huffman_compress, huffman_decompress, save_compressed, load_compressed
from MTF import move_to_front_decode, move_to_front_encode

counter = 0
print("test1 enwik7.txt")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", "enwik7_bwte.bin")
mtf_encoded_enwik7 = move_to_front_encode(read_file("enwik7_bwte.bin"))
write_to_file('enwik7_bwt+mtf_encoded.txt', mtf_encoded_enwik7)
compressed_bytes_enwik7, huffman_codes_enwik7 = huffman_compress(read_file('enwik7_bwt+mtf_encoded.txt'))
codes_size_enwik7, data_size_enwik7 = save_compressed(huffman_codes_enwik7, compressed_bytes_enwik7, "enwik_HA+bwt+mtf_e.bin")
loaded_codes_enwik7, loaded_data_enwik7 = load_compressed("enwik_HA+bwt+mtf_e.bin")
decompressed_enwik7 = huffman_decompress(loaded_data_enwik7, loaded_codes_enwik7)
mtf_decoded_enwik7 = move_to_front_decode(decompressed_enwik7)
write_to_file('enwik7_mtf_decoded.txt', mtf_decoded_enwik7)
restore_bwt_blocks("enwik7_mtf_decoded.txt", "decompressed_enwik7.txt")
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'enwik_HA+bwt+mtf_e.bin')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")==read_file("decompressed_enwik7.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt") == read_file("decompressed_enwik7.txt"):
    counter += 1
# ---------------------------------------------------------------------------------------------------------------------------------------------
print("TEST 2 BOOK")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", "book_bwte.bin")
mtf_encoded_book = move_to_front_encode(read_file("book_bwte.bin"))
write_to_file('book_bwt+mtf_encoded.txt', mtf_encoded_book)
compressed_bytes_book, huffman_codes_book = huffman_compress(read_file('book_bwt+mtf_encoded.txt'))
codes_size_book, data_size_book = save_compressed(huffman_codes_book, compressed_bytes_book, "book_HA+bwt+mtf_e.bin")
loaded_codes_book, loaded_data_book = load_compressed("book_HA+bwt+mtf_e.bin")
decompressed_book = huffman_decompress(loaded_data_book, loaded_codes_book)
mtf_decoded_book = move_to_front_decode(decompressed_book)
write_to_file('book_mtf_decoded.txt', mtf_decoded_book)
restore_bwt_blocks("book_mtf_decoded.txt", "decompressed_book.txt")
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'book_HA+bwt+mtf_e.bin')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")==read_file("decompressed_book.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt") == read_file("decompressed_book.txt"):
    counter += 1
# --------------------------------------------------------------------------------------------------------------------------------------------
print("TEST 3 BINARY FILE")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", "bin_bwte.bin")
mtf_encoded_bin = move_to_front_encode(read_file("bin_bwte.bin"))
write_to_file('bin_bwt+mtf_encoded.txt', mtf_encoded_bin)
compressed_bytes_bin, huffman_codes_bin = huffman_compress(read_file('bin_bwt+mtf_encoded.txt'))
codes_size_bin, data_size_bin = save_compressed(huffman_codes_bin, compressed_bytes_bin, "bin_HA+bwt+mtf_e.bin")
loaded_codes_bin, loaded_data_bin = load_compressed("bin_HA+bwt+mtf_e.bin")
decompressed_bin = huffman_decompress(loaded_data_bin, loaded_codes_bin)
mtf_decoded_bin = move_to_front_decode(decompressed_bin)
write_to_file('bin_mtf_decoded.txt', mtf_decoded_bin)
restore_bwt_blocks("bin_mtf_decoded.txt", "decompressed_bin.txt")
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'bin_HA+bwt+mtf_e.bin')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")==read_file("decompressed_bin.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin") == read_file("decompressed_bin.txt"):
    counter += 1
# ---------------------------------------------------------------------------------------------------------------------------------------------
print("TEST 4 IMAGE 1")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", "img1_bwte.bin")
mtf_encoded_img1 = move_to_front_encode(read_file("img1_bwte.bin"))
write_to_file('img1_bwt+mtf_encoded.txt', mtf_encoded_img1)
compressed_bytes_img1, huffman_codes_img1 = huffman_compress(read_file('img1_bwt+mtf_encoded.txt'))
codes_size_img1, data_size_img1 = save_compressed(huffman_codes_img1, compressed_bytes_img1, "img1_HA+bwt+mtf_e.bin")
loaded_codes_img1, loaded_data_img1 = load_compressed("img1_HA+bwt+mtf_e.bin")
decompressed_img1 = huffman_decompress(loaded_data_img1, loaded_codes_img1)
mtf_decoded_img1 = move_to_front_decode(decompressed_img1)
write_to_file('img1_mtf_decoded.txt', mtf_decoded_img1)
restore_bwt_blocks("img1_mtf_decoded.txt", "decompressed_img1.txt")
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", 'img1_HA+bwt+mtf_e.bin')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")==read_file("decompressed_img1.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw") == read_file("decompressed_img1.txt"):
    counter += 1
# ---------------------------------------------------------------------------------------------------------------------------------------------
print("TEST 5 IMAGE 2")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", "img2_bwte.bin")
mtf_encoded_img2 = move_to_front_encode(read_file("img2_bwte.bin"))
write_to_file('img2_bwt+mtf_encoded.txt', mtf_encoded_img2)
compressed_bytes_img2, huffman_codes_img2 = huffman_compress(read_file('img2_bwt+mtf_encoded.txt'))
codes_size_img2, data_size_img2 = save_compressed(huffman_codes_img2, compressed_bytes_img2, "img2_HA+bwt+mtf_e.bin")
loaded_codes_img2, loaded_data_img2 = load_compressed("img2_HA+bwt+mtf_e.bin")
decompressed_img2 = huffman_decompress(loaded_data_img2, loaded_codes_img2)
mtf_decoded_img2 = move_to_front_decode(decompressed_img2)
write_to_file('img2_mtf_decoded.txt', mtf_decoded_img2)
restore_bwt_blocks("img2_mtf_decoded.txt", "decompressed_img2.txt")
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", 'img2_HA+bwt+mtf_e.bin')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")==read_file("decompressed_img2.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw") == read_file("decompressed_img2.txt"):
    counter += 1
# ----------------------------------------------------------------------------------------------------------------------------------------------
print("TEST 6 IMAGE 3")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", "img3_bwte.bin")
mtf_encoded_img3 = move_to_front_encode(read_file("img3_bwte.bin"))
write_to_file('img3_bwt+mtf_encoded.txt', mtf_encoded_img3)
compressed_bytes_img3, huffman_codes_img3 = huffman_compress(read_file('img3_bwt+mtf_encoded.txt'))
codes_size_img3, data_size_img3 = save_compressed(huffman_codes_img3, compressed_bytes_img3, "img3_HA+bwt+mtf_e.bin")
loaded_codes_img3, loaded_data_img3 = load_compressed("img3_HA+bwt+mtf_e.bin")
decompressed_img3 = huffman_decompress(loaded_data_img3, loaded_codes_img3)
mtf_decoded_img3 = move_to_front_decode(decompressed_img3)
write_to_file('img3_mtf_decoded.txt', mtf_decoded_img3)
restore_bwt_blocks("img3_mtf_decoded.txt", "decompressed_img3.txt")
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", 'img3_HA+bwt+mtf_e.bin')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")==read_file("decompressed_img3.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw") == read_file("decompressed_img3.txt"):
    counter += 1
    print('айлялюлю, все круто')
else:
    print("расстреливаем всех")


