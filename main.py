import asyncio

import uvloop

from utils.key_expander import KeyExpander
from utils.cipher_converter import CipherConverter
from contexts.cipher_contexts import SymmetricCipherContext

async def main():
    iv = b'1234567812345678123456781234567812345678123456781234567812345678'
    scc = SymmetricCipherContext('hellokey', 'ECB',
                                 key_expander=KeyExpander(),
                                 cipher_converter=CipherConverter())
    await scc.encrypt_file('testfiles/text.txt', 'testfiles/result.txt')
    await scc.decrypt_file('testfiles/result.txt', 'testfiles/iresult.txt')


with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
    runner.run(main())