class PkssPadder():
    @staticmethod
    def add_padding(block: bytearray | bytes, n: int) -> bytes:
        if len(block) >= n:
            return block

        padding_size = n - len(block)
        padding = bytes([padding_size] * padding_size)
        padded_data = block + padding
        return padded_data

    @staticmethod
    def remove_padding(block: bytes, block_size):
        if not len(block) % block_size == 0:
            return block
        last_byte = block[-1]
        padding_size = int(last_byte)
        end = bytes([last_byte]) * padding_size
        if not block.endswith(end) or end == '':
            return block
        return block[:-padding_size]
