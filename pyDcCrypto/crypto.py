import base64
import binascii
import hashlib
import M2Crypto
import string
import random

IV_SIZE = 16
BS_SIZE = 16


class PyDcCryptoError(Exception):
    pass


class PyDcCrypto(object):

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, text):

        iv = ''.join(random.choice(string.digits + string.ascii_letters) for _ in range(IV_SIZE))
        try:
            cipher = M2Crypto.EVP.Cipher('aes_256_cfb', self.key, iv, 1)
            return base64.b64encode(iv + cipher.update(text))
        except Exception as e:
            raise PyDcCryptoError("error will encrypt", e)

    def decrypt(self, crypto_text):

        try:
            crypto_byte = base64.b64decode(crypto_text)
        except binascii:
            raise PyDcCryptoError("not a valid encrypted string")

        iv = crypto_byte[:IV_SIZE]
        try:
            cipher = M2Crypto.EVP.Cipher('aes_256_cfb', self.key, iv, 0)
            return cipher.update(crypto_byte[IV_SIZE:])
        except Exception as e:
            raise PyDcCryptoError("error will decrypt", e)
