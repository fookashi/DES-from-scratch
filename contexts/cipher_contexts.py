import asyncio


from padding.pkcs7 import PkssPadder
from contexts.modes import ciphers
from utils.cipher_converter import CipherConverter
from utils.key_expander import KeyExpander


class SymmetricCipherContext:
    def __init__(self, key: str, mode: str, **kwargs):
        self.key = bytes(key, 'utf-8')
        self.mode = mode
        self.kwargs = kwargs
        self.cipher = ciphers[mode]
    async def encrypt(self, data: bytes) -> bytearray:
        cryptor = self.cipher(self.key, **self.kwargs)
        crypted_data = bytearray()
        for i in range(0, len(data), 8):
            chunk = PkssPadder.add_padding(data[i:i+8], 8)
            crypted_chunk = await cryptor.encrypt(chunk)
            crypted_data += crypted_chunk
        return crypted_data

    async def decrypt(self, data: bytes) -> bytearray:
        cryptor = self.cipher(self.key, **self.kwargs)
        decrypted_data = bytearray()
        for i in range(0, len(data)-8, 8):
            chunk = data[i:i+8]
            decrypted_chunk = await cryptor.decrypt(chunk)
            decrypted_data += decrypted_chunk
        last_bytes = data[-8:]
        decrypted_data += PkssPadder.remove_padding(await cryptor.decrypt(last_bytes), 8)
        return decrypted_data

    async def encrypt_file(self, input_file_path: str, output_file_path: str):
        cryptor = self.cipher(self.key, **self.kwargs)
        data = list()
        output_file = open(output_file_path, 'wb')
        with open(input_file_path, "rb") as input_file:
            while block := input_file.read(8):
                block = await cryptor.encrypt(PkssPadder.add_padding(block, 8))
                output_file.write(block)
        output_file.close()

    async def decrypt_file(self, input_file_path: str, output_file_path: str):
        cryptor = self.cipher(self.key, **self.kwargs)
        data = list()
        with open(input_file_path, "rb") as input_file:
            while block := input_file.read(8):
                block = await cryptor.decrypt(block)
                data.append(block)

        with open(output_file_path, 'wb') as output_file:
            for d in data[:len(data) - 1:]:
                output_file.write(d)
            output_file.write(PkssPadder.remove_padding(data[-1], 8))


