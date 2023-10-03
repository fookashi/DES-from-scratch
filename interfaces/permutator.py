from abc import ABC, abstractmethod


class IPermutator(ABC):

    @staticmethod
    @abstractmethod
    async def permutate(bytes_block: bytearray | bytes, permutation_rule: tuple[int]) -> bytearray:
        raise NotImplementedError
