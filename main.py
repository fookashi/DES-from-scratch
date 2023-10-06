import asyncio
import os.path
import sys
from time import time

from utils.key_expander import KeyExpander
from utils.cipher_converter import CipherConverter
from contexts.cipher_contexts import SymmetricCipherContext
from contexts.cipher_contexts import SymmetricCipherContext
import pathlib
import secrets


async def read_bytes(init_block: bytes, mode: str, key:str, **kwargs) -> bytes:
    cryptor = SymmetricCipherContext(key, mode,
                                     key_expander=KeyExpander(),
                                     cipher_converter=CipherConverter(),
                                     **kwargs)
    print(f"Initial bytes: {init_block}")
    crypted = await cryptor.encrypt(init_block)
    print(f"Ciphered bytes: {crypted}")
    decrypted = await cryptor.decrypt(crypted)
    print(f"Decrypted bytes: {decrypted}")
    return decrypted


async def read_file(input_file_path: str, output_file_path: str, mode: str, key: str, **kwargs) -> str:
    cryptor = SymmetricCipherContext(key, mode,
                                     key_expander=KeyExpander(),
                                     cipher_converter=CipherConverter(),
                                     **kwargs)
    await cryptor.encrypt_file(input_file_path, output_file_path)
    filename, file_ext = os.path.splitext(output_file_path)
    decrypted_path = f"{filename}_decrypted{file_ext}"
    await cryptor.decrypt_file(output_file_path, decrypted_path)
    return decrypted_path


async def main():
    iv = secrets.token_bytes(64)
    t1 = time()
    key = 'verysecretkey!!!'
    bytes_ = b'HELLO WORLD GOODBYE OKAY HELLO WORLD GOODBYE OKAY HELLO WORLD OKAY HELLO WORLD GOODBYE OKAY HELLO'
    await read_bytes(bytes_, 'ECB', key)
    input_path = 'testfiles/img.png'
    output_path = 'testfiles/crypted.png'
    await read_file(input_path, output_path, 'CBC',key, iv=iv)
    t2 = time()
    print(t2 - t1)


if sys.version_info > (3, 11):
    import uvloop

    print('Uvloop integrated! Hoorey')
    with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
        runner.run(main())
else:
    print('No uvloop today')
    asyncio.run(main())
