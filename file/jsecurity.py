# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Secure encryption,
a cryptographic operation for a password.
"""
__author__ = "jeremyjone"
__datetime__ = "2019/1/2 12:01"
__all__ = ["__version__", "Prpcrypt"]
__version__ = "1.0.0"

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from Crypto.Hash import MD5


class Prpcrypt():

    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        '''
        Encrypt emthod.

        The encrypt key must be 16(AES-128) / 24(AES-192) / 32(AES-256) bytes.
        If text not the multiplier of 16, must be complemented.
        After encrypt, change to Hexadecimal.
        '''
        cryptor = AES.new(self.key, self.mode, self.key)
        text = text.encode("utf-8")
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + (b'\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext).decode("ASCII")

    def decrypt(self, text):
        '''
        Decrypt method.
        After decrypt, use strip() cut blanks.
        '''
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip(b'\0').decode("utf-8")

    @classmethod
    def loop_encrypt(cls, pwd, n=10, salt=""):
        # Salt encrypt and recursion 10 times.
        s = salt
        md5_obj = MD5.new()
        md5_obj.update((pwd + s).encode())
        # print(n, md5_obj.hexdigest())
        if n == 1:
            return md5_obj.hexdigest()
        return cls.loop_encrypt(md5_obj.hexdigest(), n - 1)




if __name__ == '__main__':
    pc = Prpcrypt('keyskeyskeyskeys')  # 初始化密钥,16位
    e = pc.encrypt("my book is free")
    d = pc.decrypt(e)
    print(e, d)
    e = pc.encrypt(u"我来加密!!!!!")
    d = pc.decrypt(e)
    print(e, d)
    l = pc.loop_encrypt("123", 5)
    print(l)
