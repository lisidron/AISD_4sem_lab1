import subprocess
import os
from Reader import read_file, get_file_size, analyze_file, analyze_compression, calculate_compression_ratio, png_to_raw

def run_lz77(mode, input_file, output_file, window_size, max_lengthmatch):
    try:
        result = subprocess.run(
            ['java', 'LZ77', mode, input_file, output_file, str(window_size), str(max_lengthmatch)],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e.stderr}")
def run_lz78(mode, input_file, output_file):
    try:
        result = subprocess.run(
            ['java', 'LZ78', mode, input_file, output_file],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e.stderr}")

counter = 0
print("test1 enwik7.txt")
path_to_input_file_enwik77 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt"
original_size_enwik7 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
run_lz77("compress", path_to_input_file_enwik77, "compressed_enwik77.lz77", 16384, 255)
compressed_size_enwik77 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_enwik77.lz77")
run_lz77("decompress", "compressed_enwik77.lz77", "output_enwik77.txt", 16384, 255)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'compressed_enwik77.lz77')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")==read_file("output_enwik77.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")==read_file("output_enwik77.txt"):
    counter += 1
print("test2 book.txt")
path_to_input_file_book77 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt"
original_size_book77 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
run_lz77("compress", path_to_input_file_book77, "compressed_book77.lz77", 16384, 255)
compressed_size_book77 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_book77.lz77")
run_lz77("decompress", "compressed_book77.lz77", "output_book77.txt", 16384, 255)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'compressed_book77.lz77')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")==read_file("output_book77.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")==read_file("output_book77.txt"):
    counter += 1
print("test3 binfile.bin")
path_to_input_file_bin77 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin"
original_size_bin77 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
run_lz77("compress", path_to_input_file_bin77, "compressed_bin77.lz77", 16384, 255)
compressed_size_bin77 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_bin77.lz77")
run_lz77("decompress", "compressed_bin77.lz77", "output_bin77.txt", 16384, 255)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'compressed_bin77.lz77')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")==read_file("output_bin77.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")==read_file("output_bin77.txt"):
    counter += 1
print("test4 img1.png")
path_to_input_file_img177 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw"
original_size_img177 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")
run_lz77("compress", path_to_input_file_img177, "compressed_img177.lz77", 16384, 255)
compressed_size_img177 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_img177.lz77")
run_lz77("decompress", "compressed_img177.lz77", "output_img177.txt", 16384, 255)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", 'compressed_img177.lz77')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")==read_file("output_img177.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")==read_file("output_img177.txt"):
    counter += 1
print("test5 img2.png")
path_to_input_file_img277 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw"
original_size_img277 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")
run_lz77("compress", path_to_input_file_img277, "compressed_img277.lz77", 16384, 255)
compressed_size_img277 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_img277.lz77")
run_lz77("decompress", "compressed_img277.lz77", "output_img277.txt", 16384, 255)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", 'compressed_img277.lz77')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")==read_file("output_img277.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")==read_file("output_img277.txt"):
    counter += 1
print("test6 img3.png")
path_to_input_file_img377 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw"
original_size_img377 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.png")
run_lz77("compress", path_to_input_file_img377, "compressed_img377.lz77", 16384, 255)
compressed_size_img377 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_img377.lz77")
run_lz77("decompress", "compressed_img377.lz77", "output_img377.txt", 16384, 255)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", 'compressed_img377.lz77')
print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")==read_file("output_img377.txt"))
if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")==read_file("output_img377.txt"):
    counter += 1
if counter == 6:
    print('айлялюлю, все круто')
else:
    print("расстериливаем всех")
# counter78 = 0
# print(" 78 test1 enwik7.txt")
# path_to_input_file_enwik78 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt"
# original_size_enwik78 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
# run_lz78("compress", path_to_input_file_enwik78, "compressed_enwik78.lz78")
# compressed_size_enwik78 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_enwik78.lz78")
# run_lz78("decompress", "compressed_enwik78.lz78", "output_enwik78.txt")
# analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'compressed_enwik78.lz78')
# print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")==read_file("output_enwik78.txt"))
# if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")==read_file("output_enwik78.txt"):
#     counter78 += 1
# print("78 test2 book.txt")
# path_to_input_file_book78 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt"
# original_size_book78 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
# run_lz78("compress", path_to_input_file_book78, "compressed_book78.lz78")
# compressed_size_book78 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_book78.lz78")
# run_lz78("decompress", "compressed_book78.lz78", "output_book78.txt")
# analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'compressed_book78.lz78')
# print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")==read_file("output_book78.txt"))
# if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")==read_file("output_book78.txt"):
#     counter78 += 1
# print("78 test3 binfile.bin")
# path_to_input_file_bin78 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin"
# original_size_bin78 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
# run_lz78("compress", path_to_input_file_bin78, "compressed_bin78.lz78")
# compressed_size_bin78 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_bin78.lz78")
# run_lz78("decompress", "compressed_bin78.lz78", "output_bin78.txt")
# analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'compressed_bin78.lz78')
# print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")==read_file("output_bin78.txt"))
# if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")==read_file("output_bin78.txt"):
#     counter78 += 1
# print("78 test4 img1.png")
# path_to_input_file_img178 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw"
# original_size_img178 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")
# run_lz78("compress", path_to_input_file_img178, "compressed_img178.lz78")
# compressed_size_img178 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_img178.lz78")
# run_lz78("decompress", "compressed_img178.lz78", "output_img178.txt")
# analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", 'compressed_img178.lz78')
# print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")==read_file("output_img178.txt"))
# if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")==read_file("output_img178.txt"):
#     counter78 += 1
# print("78 test5 img2.png")
# path_to_input_file_img278 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw"
# original_size_img278 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")
# run_lz78("compress", path_to_input_file_img278, "compressed_img278.lz78")
# compressed_size_img278 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_img278.lz78")
# run_lz78("decompress", "compressed_img278.lz78", "output_img278.txt")
# analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", 'compressed_img278.lz78')
# print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")==read_file("output_img278.txt"))
# if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")==read_file("output_img278.txt"):
#     counter78 += 1
# print("78 test6 img3.png")
# path_to_input_file_img378 = "C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw"
# original_size_img378 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")
# run_lz78("compress", path_to_input_file_img378, "compressed_img378.lz78")
# compressed_size_img378 = os.path.getsize("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/LZ/compressed_img378.lz78")
# run_lz78("decompress", "compressed_img378.lz78", "output_img378.txt")
# analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", 'compressed_img378.lz78')
# print("Правильность декдирования: ", read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")==read_file("output_img378.txt"))
# if read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")==read_file("output_img378.txt"):
#     counter78 += 1
# if counter78 == 6:
#     print('айлялюлю, все круто')
# else:
#     print("расстериливаем всех")