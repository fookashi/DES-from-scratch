class SboxConverter:
    @staticmethod
    async def read_group(block: bytes, k: int):
        bit_group = 0
        bits_length = 0
        for i, byte in enumerate(block):
            for pos in range(8):
                bits_length += 1
                bit = byte >> (7 - pos) & 1
                bit_group = (bit_group << 1) | bit
                if bits_length % k == 0:
                    yield i, bit_group
                    bit_group = 0

    @staticmethod
    async def convert_with_sblock(block: bytes, k: int, sbox: tuple[tuple[tuple[int]]]) -> bytes:
        new_bits = 0
        if len(block) * 8 // k > len(sbox):
            raise AttributeError('Bytes more than can be replaced with S-BLOCK')
        bit_mask = (1 << k) - 1
        bit_groups = SboxConverter.read_group(block, k)
        tasks = []
        async for pos, bits in bit_groups:
            row = (((bits >> (k - 1)) & 0b1) << 1) | ((bits >> 0) & 0b1)
            column = (bits >> 1) & ((1 << (k - 2)) - 1)
            sbox_value = sbox[pos][row][column]
            new_bits <<= k
            new_bits |= (sbox_value & bit_mask)
        return new_bits.to_bytes(len(block), 'big')