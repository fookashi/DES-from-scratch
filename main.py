import asyncio
import sys
from time import time

from utils.key_expander import KeyExpander
from utils.cipher_converter import CipherConverter
from contexts.cipher_contexts import SymmetricCipherContext

import secrets

async def main():
    iv = secrets.token_bytes(64)
    scc = SymmetricCipherContext('hellokey', 'CBC',
                                 iv=iv,
                                 key_expander=KeyExpander(),
                                 cipher_converter=CipherConverter())
    t1 = time()
    # crypted = await scc.encrypt(b'HELLO WORLD GOODBYE OKAY HELLO WORLD'
    #                             b' GOODBYE OKAY HELLO WORLD GOODBYE '
    #                             b'OKAY HELLO WORLD GOODBYE OKAY HELLO '
    #                             b'WORLD GOODBYE OKAY')
    # decrypted = await scc.decrypt(crypted)
    # print(decrypted)
    await scc.encrypt_file('testfiles/text.txt', 'testfiles/result.txt')
    await scc.decrypt_file('testfiles/result.txt', 'testfiles/iresult.txt')
    t2 = time()
    print(t2-t1)

if sys.version_info > (3, 11):
    import uvloop
    print('Uvloop integrated! Hoorey')
    with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
        runner.run(main())
else:
    print('No uvloop today')
    asyncio.run(main())