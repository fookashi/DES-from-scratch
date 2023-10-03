class Reader:

    @staticmethod
    def print_bytes(byteobj: bytes | bytearray, newline: bool = False):
        for byte in byteobj:
            for pos in range(8):
                bit = byte >> (7 - pos) & 0b1
                print(bit, end='')
        if newline:
            print()

    @staticmethod
    def print_bits(bits: int, length: int, newline: bool = False):
        for i in range(length):
            print(bits >> (length - 1 - i) & 1, end='')
        if newline:
            print()
