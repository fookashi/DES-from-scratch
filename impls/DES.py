from impls.feistel import FeistelNetworkSolver
from tables import IP, FP
from utils.permutator import Permutator
from padding.pkcs7 import PkssPadder

class DES(FeistelNetworkSolver):
    async def encrypt(self, block: bytes):
        permuted_block = await Permutator.permutate(block, IP)
        result = await super().encrypt(permuted_block)
        final_perm = await Permutator.permutate(result, FP)
        return final_perm

    async def decrypt(self, block: bytes):
        permuted_block = await Permutator.permutate(block, IP)
        result = await super().decrypt(permuted_block)
        final_perm = await Permutator.permutate(result, FP)
        return final_perm
