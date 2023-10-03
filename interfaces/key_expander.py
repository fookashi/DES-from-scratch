from abc import ABC, abstractmethod


class IKeyExpander(ABC):

    @abstractmethod
    async def expand_key(self, original_key: bytes) -> tuple[bytes]:
        raise NotImplementedError
