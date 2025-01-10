
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = kdf.derive(password.encode())
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted_data = encryptor.update(data) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encrypted_data)

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        data = f.read()

    salt = data[:16]
    iv = data[16:32]
    encrypted_data = data[32:]

    kdf = PBKDF2HMAC(algorithm=SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = kdf.derive(password.encode())

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    with open(file_path[:-4], 'wb') as f:
        f.write(decrypted_data)
