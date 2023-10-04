class CircularShifter:

    @staticmethod
    def left_shift(bits: int, bits_length: int, shift: int = 1) -> int:
        mask = (1 << bits_length) - 1
        shifted = ((bits << shift) | (bits >> (bits_length - shift))) & mask
        return shifted

    @staticmethod
    def left_shift_bytes(block: bytes | bytearray, shift: int) -> bytes:
        assert 0 < shift < 8, "Шифт должен быть в пределах 1-7"
        result = bytearray(len(block))
        for i in range(len(block)):
            result[i] = ((block[i] << shift) | (block[(i + 1) % len(block)] >> (8 - shift))) & 0xFF

        return bytes(result)




