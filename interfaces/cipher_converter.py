from abc import ABC, abstractmethod


class ICipherConverter(ABC):

    @abstractmethod
    async def convert(self, block: bytearray, round_key: bytearray | bytes) -> bytearray:
        raise NotImplementedError