from interfaces import ICipherConverter
from utils.permutator import Permutator
from utils.sbox_converter import SboxConverter
from tables import EXPANSION_TABLE, SBOX, P
from utils.bytes_xor import xor_bytes


class CipherConverter(ICipherConverter):

    async def convert(self, block: bytearray | bytes, round_key: bytearray | bytes) -> bytes:
        expanded_block = await Permutator.permutate(block, EXPANSION_TABLE)

        expanded_block_xor_key = xor_bytes(expanded_block, round_key)

        substituted_block = await SboxConverter.convert_with_sblock(expanded_block_xor_key, 6, SBOX)

        return substituted_block
