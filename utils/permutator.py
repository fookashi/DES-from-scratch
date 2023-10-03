from interfaces.permutator import IPermutator


class Permutator(IPermutator):

    @staticmethod
    async def permutate(bytes_block: bytearray | bytes, permutation_rule: tuple) -> bytearray:
        permuted_block = bytearray(len(permutation_rule)//8)
        for i, bit_position in enumerate(permutation_rule):
            byte_index, bit_index = divmod(bit_position, 8)
            byte_value = bytes_block[byte_index]
            permuted_bit = (byte_value >> (7 - bit_index)) & 1
            permuted_block[i//8] |= permuted_bit << (7 - (i % 8))
        return permuted_block
