import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random



"""
Cipher is a class which creates a cipher object
The cipher object is responsible for encrypting
and decrypting messages

@Author Gabriel Ciolac
"""
class Cipher:
    def __init__(self):
        self.__privateKey = self.__generateKeys()


    """
        Generates a public private key pair using a randomly seeded key

        @Author Gabriel Ciolac
    """
    def __generateKeys(self):
        key = RSA.generate(1024) 
        return key
    
    """
        Encrypt a message against a public key
        self: instance of cipher running
        key: public key which will be used for encryption
        msg: message to be encrypted

        @Author Gabriel Ciolac
    """
    def encrypt(self,key,msg):
        return key.encrypt(msg)

    def returnPublicKey(self):
        return self.__privateKey.publickey()
    
    def decrypt(self,msg):
        return self.__privateKey.decrypt(msg)
    
