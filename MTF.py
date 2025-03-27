def move_to_front_encode(data: bytes) -> bytes:
    alphabet = list(range(256))
    encoded_data = bytearray()
    for byte in data:
        index = alphabet.index(byte)
        encoded_data.append(index)
        alphabet.pop(index)
        alphabet.insert(0, byte)
    return bytes(encoded_data)
    return encoded_output


def move_to_front_decode(encoded_data: bytes) -> bytes:

    alphabet = list(range(256))
    decoded_data = bytearray()

    for index in encoded_data:

        byte = alphabet[index]
        decoded_data.append(byte)

        alphabet.pop(index)
        alphabet.insert(0, byte)

    return bytes(decoded_data)
