import queue
import struct
import numpy as np
from Reader import read_file, get_file_size, write_to_file, calculate_compression_ratio, analyze_compression, png_to_raw
from PIL import Image
class Node():
    def __init__(self, symbol=None, counter=None, left=None, right=None, parent=None):  # Было init → стало __init__
        self.symbol = symbol
        self.counter = counter
        self.left = left
        self.right = right
        self.parent = parent

    def __lt__(self, other):  
        return self.counter < other.counter
def count_symb(data: bytes) -> np.ndarray:
    counter = np.zeros(256, dtype=int)
    for byte in data:
        counter[byte] += 1
    return counter
def huffman_compress(data: bytes) -> bytes:
    C = count_symb(data)
    list_of_leafs = []
    Q = queue.PriorityQueue()

    for i in range(256):
        if C[i] != 0:
            leaf = Node(symbol=i, counter=C[i])
            list_of_leafs.append(leaf)
            Q.put(leaf)

    while Q.qsize() >= 2:
        left_node = Q.get()
        right_node = Q.get()
        parent_node = Node(left=left_node, right=right_node)
        left_node.parent = parent_node
        right_node.parent = parent_node
        parent_node.counter = left_node.counter + right_node.counter
        Q.put(parent_node)

    codes = {}
    for leaf in list_of_leafs:
        node = leaf
        code = ""
        while node.parent is not None:
            if node.parent.left == node:
                code = "0" + code
            else:
                code = "1" + code
            node = node.parent
        codes[leaf.symbol] = code

    coded_message = ""
    for byte in data:
        coded_message += codes[byte]
    padding = 8 - len(coded_message) % 8
    coded_message += '0' * padding
    coded_message = f"{padding:08b}" + coded_message 
    bytes_string = bytearray()
    for i in range(0, len(coded_message), 8):
        byte = coded_message[i:i+8]
        bytes_string.append(int(byte, 2))

    return bytes(bytes_string), codes
def huffman_decompress(compressed_data: bytes, huffman_codes: dict) -> bytes:
    padding = compressed_data[0]
    coded_message = ""
    for byte in compressed_data[1:]:
        coded_message += f"{byte:08b}"

    if padding > 0:
        coded_message = coded_message[:-padding]
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    current_code = ""
    decoded_data = bytearray()

    for bit in coded_message:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ""

    return bytes(decoded_data)
def read_huffman_codes(codes_file):
    huffman_codes = {}
    with open(codes_file, 'r') as f:
        for line in f:
            symbol, code = line.strip().split(':')
            huffman_codes[int(symbol)] = code
    return huffman_codes
def write_huffman_codes(huffman_codes, file_path):
    with open(file_path, 'w') as code_file:
        for symbol, code in huffman_codes.items():
            code_file.write(f"{symbol}:{code}\n")
def save_compressed(huffman_codes: dict, compressed_data: bytes, filename: str) -> tuple[int, int]:
    with open(filename, 'wb') as f:
        num_codes = len(huffman_codes)
        f.write(struct.pack('>H', num_codes))
        codes_size = f.tell()
        for symbol, code in huffman_codes.items():
            code_length = len(code)
            code_bytes = int(code, 2).to_bytes((code_length + 7) // 8, 'big')
            f.write(struct.pack('>BB', symbol, code_length))
            f.write(code_bytes)

        codes_total_size = f.tell()
        f.write(compressed_data)
        total_size = f.tell()

    return codes_total_size - codes_size, total_size - codes_total_size
def load_compressed(filename: str) -> tuple[dict, bytes]:
    with open(filename, 'rb') as f:
        num_codes = struct.unpack('>H', f.read(2))[0]

        huffman_codes = {}
        for _ in range(num_codes):
            symbol, code_length = struct.unpack('>BB', f.read(2))
            bytes_needed = (code_length + 7) // 8
            code_bytes = f.read(bytes_needed)
            code = bin(int.from_bytes(code_bytes, 'big'))[2:].zfill(code_length)
            huffman_codes[symbol] = code

        compressed_data = f.read()

    return huffman_codes, compressed_data

counter = 0
print("test1 enwik7.txt")
text_enwik7 = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt")
compressed_bytes_enwik7, huffman_codes_enwik7 = huffman_compress(text_enwik7)
codes_size_enwik7, data_size_enwik7 = save_compressed(huffman_codes_enwik7, compressed_bytes_enwik7, "compressed.bin")
loaded_codes_enwik7, loaded_data_enwik7 = load_compressed("compressed.bin")
decompressed_enwik7 = huffman_decompress(loaded_data_enwik7, loaded_codes_enwik7)
write_to_file('decompressed_enwik.txt',decompressed_enwik7)
print("Размер финального файла после декомпрессии: ", get_file_size("decompressed_enwik.txt"))
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/enwik7.txt", 'compressed.bin')
print("Правильность декдирования: ", text_enwik7==decompressed_enwik7)
print("test2 book.txt")
text_book = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
original_size_book = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt")
compressed_bytes_book, huffman_codes_book = huffman_compress(text_book)
codes_size_book, data_size_book = save_compressed(huffman_codes_book, compressed_bytes_book, "compressed_book.bin")
loaded_codes_book, loaded_data_book = load_compressed("compressed_book.bin")
decompressed_book = huffman_decompress(loaded_data_book, loaded_codes_book)
compressed_size_book = get_file_size('compressed_book.bin')
ratio_book = calculate_compression_ratio(original_size_book, compressed_size_book)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/book.txt", 'compressed_book.bin')
print("Правильность декдирования: ", text_book==decompressed_book)
print("test3 b.bin")
text_bin = read_file("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
original_size_bin = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin")
compressed_bytes_bin, huffman_codes_bin = huffman_compress(text_bin)
codes_size_bin, data_size_bin = save_compressed(huffman_codes_bin, compressed_bytes_bin, "compressed_b.bin")
loaded_codes_bin, loaded_data_bin = load_compressed("compressed_b.bin")
decompressed_bin = huffman_decompress(loaded_data_bin, loaded_codes_bin)
compressed_size_bin = get_file_size('compressed_b.bin')
ratio_bin = calculate_compression_ratio(original_size_bin, compressed_size_bin)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/test3_bin.bin", 'compressed_b.bin')
print("Правильность декдирования: ", text_book==decompressed_book)
print("test4 img1.png")
png_to_raw('C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.png', 'C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw')
original_data_img1 = read_file('C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw')
original_size_img1 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw")
compressed_bytes_img1, huffman_codes_img1 = huffman_compress(original_data_img1)
codes_size_img1, data_size_img1 = save_compressed(huffman_codes_img1, compressed_bytes_img1, "compressed_img1.bin")
loaded_codes_img1, loaded_data_img1 = load_compressed("compressed_img1.bin")
decompressed_img1 = huffman_decompress(loaded_data_img1, loaded_codes_img1)
compressed_size_img1 = get_file_size('compressed_img1.bin')
ratio_img1 = calculate_compression_ratio(original_size_img1, compressed_size_img1)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img1.raw", 'compressed_img1.bin')
print("Правильность декдирования: ", original_data_img1==decompressed_img1)
print("test5 img2.png")
png_to_raw('C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.png', 'C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw')
original_data_img2 = read_file('C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw')
original_size_img2 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw")
compressed_bytes_img2, huffman_codes_img2 = huffman_compress(original_data_img2)
codes_size_img2, data_size_img2 = save_compressed(huffman_codes_img2, compressed_bytes_img2, "compressed_img2.bin")
loaded_codes_img2, loaded_data_img2 = load_compressed("compressed_img2.bin")
decompressed_img2 = huffman_decompress(loaded_data_img2, loaded_codes_img2)
compressed_size_img2 = get_file_size('compressed_img2.bin')
ratio_img2 = calculate_compression_ratio(original_size_img2, compressed_size_img2)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img2.raw", 'compressed_img2.bin')
print("Правильность декдирования: ", original_data_img2==decompressed_img2)
print("test6 img3.png")
png_to_raw('C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.png', 'C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw')
original_data_img3 = read_file('C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw')
original_size_img3 = get_file_size("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw")
compressed_bytes_img3, huffman_codes_img3 = huffman_compress(original_data_img3)
codes_size_img3, data_size_img3 = save_compressed(huffman_codes_img3, compressed_bytes_img3, "compressed_img3.bin")
loaded_codes_img3, loaded_data_img3 = load_compressed("compressed_img3.bin")
decompressed_img3 = huffman_decompress(loaded_data_img3, loaded_codes_img3)
compressed_size_img3 = get_file_size('compressed_img3.bin')
ratio_img3 = calculate_compression_ratio(original_size_img3, compressed_size_img3)
analyze_compression("C:/Users/Elisabeth/PycharmProjects/lab1_AISD/material/img3.raw", 'compressed_img3.bin')
print("Правильность декдирования: ", original_data_img3==decompressed_img3)
