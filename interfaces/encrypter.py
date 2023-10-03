from abc import ABC, abstractmethod


class IEncrypter(ABC):

    @abstractmethod
    async def encrypt(self, block: bytes):
        raise NotImplementedError

    @abstractmethod
    async def decrypt(self, block: bytes):
        raise NotImplementedError
