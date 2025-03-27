import sys
from collections import deque
from BWT.BWT import generate_bwt_suffix_array,revert_bwt, process_bwt_blocks, restore_bwt_blocks
from Reader import get_file_size, calculate_compression_ratio, read_file, write_to_file, analyze_file, analyze_compression, png_to_raw
from RLE import rle_encode, rle_decode
counter = 0
print("test1 enwik7.txt")
original_size_enwik7 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", "bin_enwik7.bin")
text_bwt_enwik7_en = read_file("bin_enwik7.bin")
rle_encoded_enwik7 = rle_encode(text_bwt_enwik7_en)
write_to_file('enwik7_bwt+rle_encoded.txt', rle_encoded_enwik7)
rle_decoded_enwik7 = rle_decode(rle_encoded_enwik7)
write_to_file('enwik7_rle_decoded.txt', rle_decoded_enwik7)
restore_bwt_blocks("enwik7_rle_decoded.txt", "decompressed_enwik7.txt")
compressed_size_enwik7 = get_file_size("decompressed_enwik7.txt")
ratio_enwik7 = calculate_compression_ratio(original_size_enwik7, compressed_size_enwik7)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'enwik7_bwt+rle_encoded.txt')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")==read_file("decompressed_enwik7.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt") == read_file("decompressed_enwik7.txt"):
    counter += 1
# ---------------------------------------------------------------------------------------------------------------------------------------------------
print("test2 book.txt")
original_size_book = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", "bin_book.bin")
text_bwt_book_en = read_file('bin_book.bin')
rle_encoded_book = rle_encode(text_bwt_book_en)
write_to_file('book_bwt+rle_encoded.txt', rle_encoded_book)
rle_decoded_book = rle_decode(rle_encoded_book)
write_to_file('book_rle_decoded.txt', rle_decoded_book)
restore_bwt_blocks("book_rle_decoded.txt", "decompressed_book.txt")
compressed_size_book = get_file_size("decompressed_book.txt")
ratio_book = calculate_compression_ratio(original_size_book, compressed_size_book)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'book_bwt+rle_encoded.txt')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")==read_file("decompressed_book.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt") == read_file("decompressed_book.txt"):
    counter += 1
# ---------------------------------------------------------------------------------------------------------------------------------------------------
print("test3 bin.bin")
original_size_bin = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", "bin_bin.bin")
text_bwt_bin_en = read_file('bin_bin.bin')
rle_encoded_bin = rle_encode(text_bwt_bin_en)
write_to_file('bin_bwt+rle_encoded.txt', rle_encoded_bin)
rle_decoded_bin = rle_decode(rle_encoded_bin)
write_to_file('bin_rle_decoded.txt', rle_decoded_bin)
restore_bwt_blocks("bin_rle_decoded.txt", "decompressed_bin.txt")
compressed_size_bin = get_file_size("decompressed_bin.txt")
ratio_bin = calculate_compression_ratio(original_size_bin, compressed_size_bin)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'bin_bwt+rle_encoded.txt')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")==read_file("decompressed_bin.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin") == read_file("decompressed_bin.txt"):
    counter += 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------
print("test4 img1.png")
original_size_img1 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", "bin_img1.bin")
text_bwt_img1_en = read_file('bin_img1.bin')
rle_encoded_img1 = rle_encode(text_bwt_img1_en)
write_to_file('img1_bwt+rle_encoded.txt', rle_encoded_img1)
rle_decoded_img1 = rle_decode(rle_encoded_img1)
write_to_file('img1_rle_decoded.txt', rle_decoded_img1)
restore_bwt_blocks("img1_rle_decoded.txt", "decompressed_img1.txt")
compressed_size_img1 = get_file_size("decompressed_img1.txt")
ratio_img1 = calculate_compression_ratio(original_size_img1, compressed_size_img1)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", 'img1_bwt+rle_encoded.txt')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")==read_file("decompressed_img1.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw") == read_file("decompressed_img1.txt"):
    counter += 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------
print("test5 img2.png")
original_size_img2 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", "bin_img2.bin")
text_bwt_img2_en = read_file('bin_img2.bin')
rle_encoded_img2 = rle_encode(text_bwt_img2_en)
write_to_file('img2_bwt+rle_encoded.txt', rle_encoded_img2)
rle_decoded_img2 = rle_decode(rle_encoded_img2)
write_to_file('img2_rle_decoded.txt', rle_decoded_img2)
restore_bwt_blocks("img2_rle_decoded.txt", "decompressed_img2.txt")
compressed_size_img2 = get_file_size("decompressed_img2.txt")
ratio_img2 = calculate_compression_ratio(original_size_img2, compressed_size_img2)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", 'img2_bwt+rle_encoded.txt')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")==read_file("decompressed_img2.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw") == read_file("decompressed_img2.txt"):
    counter += 1
# ----------------------------------------------------------------------------------------------------------------------------------------------------
print("test6 img3.png")
original_size_img3 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")
process_bwt_blocks("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", "bin_img3.bin")
text_bwt_img3_en = read_file('bin_img3.bin')
rle_encoded_img3 = rle_encode(text_bwt_img3_en)
write_to_file('img3_bwt+rle_encoded.txt', rle_encoded_img3)
rle_decoded_img3 = rle_decode(rle_encoded_img3)
write_to_file('img3_rle_decoded.txt', rle_decoded_img3)
restore_bwt_blocks("img3_rle_decoded.txt", "decompressed_img3.txt")
compressed_size_img3 = get_file_size("decompressed_img3.txt")
ratio_img3 = calculate_compression_ratio(original_size_img3, compressed_size_img3)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", 'img3_bwt+rle_encoded.txt')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")==read_file("decompressed_img3.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw") == read_file("decompressed_img3.txt"):
    counter += 1
if counter == 6:
    print('айлялюлю, все круто')
else:
    print("расстреливаем всех")