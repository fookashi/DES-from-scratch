from impls.DES import DES
from impls.CBC import CBC

ciphers = {
    'ECB': DES,
    'CBC': CBC,
    'PCBC': None,
    'CFB': None,
    'OFB': None,
    'CTR': None,
    'RandomDelta': None
}
