import os
import hashlib

password_hash = os.environ.get('PASSWORD_HASH')


def verify_password(password):
    password_bytes = password.encode('utf-8')
    password_hash_bytes = hashlib.sha256(password_bytes).digest()
    password_hash_hex = password_hash_bytes.hex()
    return password_hash_hex == password_hash

password = input('Enter your password: ')

if verify_password(password):
    print('Access granted!')
else:
    print('Access denied!')
