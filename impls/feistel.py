from interfaces import IEncrypter, IKeyExpander, ICipherConverter
from utils.bytes_xor import xor_bytes
from padding.pkcs7 import PkssPadder


class FeistelNetworkSolver(IEncrypter):
    def __init__(self, key: bytes, key_expander: IKeyExpander, cipher_converter: ICipherConverter):
        self.key = key
        self.key_expander = key_expander
        self.cipher_converter = cipher_converter
        self.round_keys = None

    async def generate_round_keys(self, key: bytes):
        self.round_keys = await self.key_expander.expand_key(key)

    async def encrypt(self, block: bytes):
        if self.round_keys is None:
            await self.generate_round_keys(self.key, 8)
        left_part = block[:len(block) // 2]
        right_part = block[len(block) // 2:]
        for round_key in self.round_keys:
            ciphered_part = await self.cipher_converter.convert(right_part, round_key)
            left_xor_ciphered = xor_bytes(left_part, ciphered_part)
            left_part = right_part
            right_part = left_xor_ciphered
        result = right_part + left_part

        return result

    async def decrypt(self, block: bytes):
        if self.round_keys is None:
            await self.generate_round_keys(self.key, 8)
        left_part = block[:len(block) // 2]
        right_part = block[len(block) // 2:]
        for round_key in self.round_keys[::-1]:
            ciphered_part = await self.cipher_converter.convert(right_part, round_key)
            left_xor_ciphered = xor_bytes(left_part, ciphered_part)
            left_part = right_part
            right_part = left_xor_ciphered
        result = right_part + left_part

        return result
