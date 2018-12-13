import unittest
from pyDcCrypto.crypto import PyDcCrypto


class TestCrypto(unittest.TestCase):

    def test_decrypt(self):
        crypto = PyDcCrypto("Bar")
        crypted = "raSRtH1uOS8gzlT/lfyLSA82rn/aFPrzHDmJBg1OyqaHnKgYhHr+4VmE2PmF+bBSBbxZDyJH/w=="
        expected = "Long input with more than 16 characters"
        result = crypto.decrypt(crypted)
        self.assertEqual(expected, result)

    def test_encrypt(self):
        crypto = PyDcCrypto("Bar")
        msg = "Long input with more than 16 characters"
        result = crypto.encrypt(msg)
        print crypto.decrypt(result)
        self.assertEqual(msg,  crypto.decrypt(result))


if __name__ == '__main__':
    unittest.main()
