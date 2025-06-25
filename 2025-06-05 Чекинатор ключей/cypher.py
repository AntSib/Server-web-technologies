from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def encrypt_rsa(message: bytes, public_key_pem: bytes) -> bytes:
    public_key = RSA.import_key(public_key_pem)
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message)
    return encrypted


def decrypt_rsa(encrypted: bytes, private_key_pem: bytes) -> str:
    private_key = RSA.import_key(private_key_pem)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(encrypted)
    return decrypted.decode('utf-8')
