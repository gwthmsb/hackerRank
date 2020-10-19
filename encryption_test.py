from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from os import environ

PADDING = '{'


def pbswencrypt(plaintext):
    """Encrypt plaintext using predefined key"""
    #the_key = '336e437259707431306e4b457946307250625357757343306e747230314d306e'
    the_key=environ["KEY"]
    blocksize = 256

    padded = plaintext + (blocksize - len(plaintext) % blocksize) * PADDING
    print("Hex decode: {}".format(the_key.decode('hex')))
    cipher = AES.new(the_key.decode('hex'))
    ciphertext = b64encode(cipher.encrypt(padded))

    return ciphertext



def pbswdecrypt(ciphertext):
    """Decypt ciphertext using predefined key"""

    #the_key = '336e437259707431306e4b457946307250625357757343306e747230314d306e'
    the_key = environ["KEY"]
    cipher = AES.new(the_key.decode('hex'))
    plaintext = cipher.decrypt(b64decode(ciphertext)).rstrip(PADDING)

    return plaintext

def pbswencrypt1(plaintext):
    """Encrypt plaintext using predefined key"""
    the_key = '1234567891012134'
    blocksize = 256

    padded = plaintext + (blocksize - len(plaintext) % blocksize) * PADDING
    cipher = AES.new(the_key)
    ciphertext = b64encode(cipher.encrypt(padded))

    return ciphertext



password = "pbsworks@123"
enc_pass = pbswencrypt(password)
dec_pass = pbswdecrypt(enc_pass)

print("Encrypted pass: {}".format(enc_pass))
print("Decrypted pass: {}".format(dec_pass))