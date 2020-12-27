import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Wrapper:
    def gen_key():
        key = Fernet.generate_key()
        return key

    def key_from_pass(password, unique=False):
        password = bytes(password, 'utf-8')
        if unique:
            salt = os.urandom(16)
        else:
            salt = b'0\xc03T\xb8\x9a\xf9\xcb\xf4\xf8\xc7\x00a\xd6\xa7M'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def encrypt(data, key):
        f = Fernet(key)
        token = f.encrypt(bytes(data, 'utf-8'))
        return token

    def decrypt(token, key):
        f = Fernet(key)
        data = str(f.decrypt(token))
        if data[0:2] == "b'":
            data = data[2:-1]
        return data
