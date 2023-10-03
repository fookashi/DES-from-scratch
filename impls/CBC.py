from impls.DES import DES
from tables import IP, FP
from utils.permutator import Permutator
from utils.bytes_xor import xor_bytes


class CBC(DES):
    def __init__(self, key: bytes, iv:bytes, key_expander, cipher_converter):
        self.iv = iv
        super().__init__(key, key_expander, cipher_converter)

    async def encrypt(self, block: bytes):
        vectored_block = xor_bytes(block, self.iv)
        result = await super().encrypt(vectored_block)
        self.iv = result
        return result

    async def decrypt(self, block: bytes):
        v = self.iv
        self.iv = block
        result = await super().decrypt(block)
        vectored_result = xor_bytes(result, v)
        return vectored_result


