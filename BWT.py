import sys
from Reader import read_file, get_file_size, calculate_compression_ratio, analyze_compression
def generate_bwt_suffix_array(data: bytes) -> tuple[bytes, int]:
    if not data:
        return b'', 0
    doubled_data = data + data
    length = len(data)
    suffix_array = sorted(range(length), key=lambda i: doubled_data[i:i + length])
    transformed_bwt = bytearray()
    original_position = -1
    for i, index in enumerate(suffix_array):
        if index == 0:
            transformed_bwt.append(data[-1])
            original_position = i
        else:
            transformed_bwt.append(data[index - 1])
    return bytes(transformed_bwt), original_position
def revert_bwt(encoded_data: bytes, position: int) -> bytes:
    if not encoded_data:
        return b''
    frequency = {}
    ranks = []
    for char in encoded_data:
        frequency[char] = frequency.get(char, 0) + 1
        ranks.append(frequency[char] - 1)
    first_index = {}
    sorted_chars = sorted(frequency.keys())
    total = 0
    for char in sorted_chars:
        first_index[char] = total
        total += frequency[char]
    output = bytearray()
    current = position
    for _ in range(len(encoded_data)):
        char = encoded_data[current]
        output.append(char)
        current = first_index[char] + ranks[current]
    return bytes(reversed(output))
def process_bwt_blocks(input_path: str, output_path: str, block_size: int = 10000):
    with open(input_path, 'rb') as src, open(output_path, 'wb') as tgt:
        while True:
            chunk = src.read(block_size)
            if not chunk:
                break
            encoded_data, position = generate_bwt_suffix_array(chunk)
            tgt.write(position.to_bytes(4, sys.byteorder))
            tgt.write(encoded_data)

def restore_bwt_blocks(input_path: str, output_path: str, block_size: int = 10000):
    with open(input_path, 'rb') as src, open(output_path, 'wb') as tgt:
        while True:
            position_bytes = src.read(4)
            if not position_bytes:
                break
            position = int.from_bytes(position_bytes, sys.byteorder)
            encoded_data = src.read(block_size)
            if not encoded_data:
                break
            decoded_data = revert_bwt(encoded_data, position)
            tgt.write(decoded_data)
