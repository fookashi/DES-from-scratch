class CircularShifter:

    @staticmethod
    def left_shift(bits: int, bits_length: int, shift: int = 1) -> int:
        mask = (1 << bits_length) - 1
        shifted = ((bits << shift) | (bits >> (bits_length - shift))) & mask
        return shifted
