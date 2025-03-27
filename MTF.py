def move_to_front_encode(data: bytes) -> bytes:
    # Инициализация алфавита (все возможные байты 0-255)
    alphabet = list(range(256))
    encoded_data = bytearray()

    for byte in data:
        # Находим индекс текущего байта в алфавите
        index = alphabet.index(byte)
        encoded_data.append(index)

        # Обновляем алфавит: перемещаем использованный байт в начало
        alphabet.pop(index)
        alphabet.insert(0, byte)

    return bytes(encoded_data)

    return encoded_output


def move_to_front_decode(encoded_data: bytes) -> bytes:

    # Инициализация алфавита (все возможные байты 0-255)
    alphabet = list(range(256))
    decoded_data = bytearray()

    for index in encoded_data:
        # Получаем байт по индексу из текущего алфавита
        byte = alphabet[index]
        decoded_data.append(byte)

        # Обновляем алфавит: перемещаем использованный байт в начало
        alphabet.pop(index)
        alphabet.insert(0, byte)

    return bytes(decoded_data)