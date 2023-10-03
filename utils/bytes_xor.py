def xor_bytes(byte_obj_1: bytes | bytearray, byte_obj_2: bytes | bytearray):
    result = bytearray(min(len(byte_obj_1), len(byte_obj_2)))
    for i in range(len(result) - 1, -1, -1):
        result[i] = byte_obj_1[i] ^ byte_obj_2[i]
    return result
