from Reader import read_file, write_to_file, get_file_size, calculate_compression_ratio, calculate_entropy, \
    analyze_file, analyze_compression
def rle_encode(data: bytes) -> bytes:
    compressed = bytearray()
    n = len(data)
    i = 0
    while i < n:
        current = data[i]
        count = 1
        while i + count < n and data[i + count] == current and count < 255:
            count += 1
        if count > 1:
            compressed.append(count)
            compressed.append(current)
            i += count
        else:
            non_repeating = bytearray()
            while i < n and (i + 1 >= n or data[i] != data[i + 1]):
                non_repeating.append(data[i])
                i += 1
                if len(non_repeating) == 255:
                    break
            compressed.append(0)
            compressed.append(len(non_repeating))
            compressed.extend(non_repeating)
    return bytes(compressed)


def rle_decode(compressed_data: bytes) -> bytes:
    result = bytearray()
    i = 0
    n = len(compressed_data)

    while i < n:
        count = compressed_data[i]

        if count == 0:
            length = compressed_data[i + 1]
            result.extend(compressed_data[i + 2: i + 2 + length])
            i += 2 + length
        else:
            byte = compressed_data[i + 1]
            result.extend([byte] * count)
            i += 2

    return bytes(result)

counter = 0
print("test1 enwik7.txt")
text_enwik7 = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
original_size_enwik7 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
text_enwik7_encoded = rle_encode(text_enwik7)
text_enwik7_decoded = rle_decode(text_enwik7_encoded)
write_to_file('RLE.txt', text_enwik7_encoded)
compressed_size_enwik7 = get_file_size('RLE.txt')
ratio_enwik7 = calculate_compression_ratio(original_size_enwik7, compressed_size_enwik7)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'RLE.txt')
print("Правильность декдирования: ", text_enwik7==text_enwik7_decoded)
print("test1 book.txt")
text_book = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
original_size_book = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
text_book_encoded = rle_encode(text_book)
text_book_decoded = rle_decode(text_book_encoded)
write_to_file('RLE_book.txt', text_book_encoded)
compressed_size_book = get_file_size('RLE_book.txt')
ratio_book = calculate_compression_ratio(original_size_book, compressed_size_book)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'RLE_book.txt')
print("Правильность декдирования: ", text_book==text_book_decoded)
print("test1 binfile.bin")
text_binfile = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
original_size_binfile = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
text_binfile_encoded = rle_encode(text_binfile)
text_binfile_decoded = rle_decode(text_binfile_encoded)
write_to_file('RLE_bin.txt', text_binfile_encoded)
compressed_size_binfile = get_file_size('RLE_bin.txt')
ratio_binfile = calculate_compression_ratio(original_size_binfile, compressed_size_binfile)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'RLE_bin.txt')
print("Правильность декдирования: ", text_binfile==text_binfile_decoded)
print("test1 img1.png")
text_img1 = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")
original_size_img1 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")
text_img1_encoded = rle_encode(text_img1)
text_img1_decoded = rle_decode(text_img1_encoded)
write_to_file('RLE_img1.txt', text_img1_encoded)
compressed_size_img1 = get_file_size('RLE_img1.txt')
ratio_img1 = calculate_compression_ratio(original_size_img1, compressed_size_img1)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", 'RLE_img1.txt')
print("Правильность декдирования: ", text_img1==text_img1_decoded)
print("test1 img2.png")
text_img2 = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")
original_size_img2 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")
text_img2_encoded = rle_encode(text_img2)
text_img2_decoded = rle_decode(text_img2_encoded)
write_to_file('RLE_img2.txt', text_img2_encoded)
compressed_size_img2 = get_file_size('RLE_img2.txt')
ratio_img2 = calculate_compression_ratio(original_size_img2, compressed_size_img2)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", 'RLE_img2.txt')
print("Правильность декдирования: ", text_img2==text_img2_decoded)
print("test1 img3.png")
text_img3 = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")
original_size_img3 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")
text_img3_encoded = rle_encode(text_img3)
text_img3_decoded = rle_decode(text_img3_encoded)
write_to_file('RLE_img3.txt', text_img3_encoded)
compressed_size_img3 = get_file_size('RLE_img3.txt')
ratio_img3 = calculate_compression_ratio(original_size_img3, compressed_size_img3)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", 'RLE_img3.txt')
print("Правильность декдирования: ", text_img3==text_img3_decoded)
