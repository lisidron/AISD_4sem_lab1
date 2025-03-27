import math
import os
from collections import Counter
import numpy as np
from PIL import Image
def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()
def write_to_file(filename, data_array: bytes):
    with open(filename, "wb") as file:
        file.write(data_array)
    print(f"Данные записаны в файл {filename}")
def calculate_compression_ratio(original_size: int, compressed_size: int) -> float:
    return original_size / compressed_size
def calculate_entropy(data: bytes) -> float:
    if not data:
        return 0.0

    # Считаем частоту каждого символа
    frequency = Counter(data)
    total_symbols = len(data)

    # Рассчитываем энтропию
    entropy = 0.0
    for count in frequency.values():
        probability = count / total_symbols
        entropy -= probability * math.log2(probability)

    return entropy
def analyze_file(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    file_size = len(data)
    entropy = calculate_entropy(data)
    return file_size, entropy
def analyze_compression(input_file: str, compressed_file: str):
    original_size, original_entropy = analyze_file(input_file)
    compressed_size, compressed_entropy = analyze_file(compressed_file)
    compression_ratio = calculate_compression_ratio(original_size, compressed_size)
    print(f"Файл: {input_file}")
    print(f"Размер исходного файла: {original_size} байт")
    print(f"Размер сжатого файла: {compressed_size} байт")
    print(f"Коэффициент сжатия: {compression_ratio:.3f}")
    print(f"Энтропия исходного файла: {original_entropy:.2f} бит/символ")
    print(f"Энтропия сжатого файла: {compressed_entropy:.2f} бит/символ")
    print("-" * 40)
def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)
        print(f"Размер файла '{file_path}': {size} байт")
        return size
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
def png_to_raw(input_path: str, output_path: str) -> None:
    """
    Конвертирует PNG в RAW-формат (пиксельные данные без сжатия)

    Параметры:
    input_path (str): Путь к исходному PNG-файлу
    output_path (str): Путь для сохранения RAW-файла

    Возвращает:
    None. Результат записывается в output_path
    """
    try:
        with Image.open(input_path) as img:
            # Конвертируем в RGB/RGBA
            if img.mode == 'P':
                img = img.convert('RGBA')
            elif img.mode == 'L':
                img = img.convert('RGB')

            # Сохраняем RAW
            np.array(img).tofile(output_path)

            # Выводим информацию
            print(f"Конвертация успешна\n"
                  f"Размер: {img.width}x{img.height}\n"
                  f"Каналы: {len(img.getbands())}\n"
                  f"Размер файла: {img.width * img.height * len(img.getbands())} байт")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
        raise



