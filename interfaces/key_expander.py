from abc import ABC, abstractmethod


class IKeyExpander(ABC):

    @abstractmethod
    async def expand_key(self, original_key: bytes | bytearray) -> tuple[bytes]:
        raise NotImplementedError
