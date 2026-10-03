import os
import base64

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def get_encryption_key():
    key = base64.b64decode(
        os.environ["AES_256_KEY_B64"],
        validate=True
    )

    if len(key) != 32:
        raise ValueError(
            "AES-256 requires a 32-byte key"
        )

    return key


def encrypt_sensitive_data(plaintext):
    key = get_encryption_key()

    aesgcm = AESGCM(key)

    nonce = os.urandom(12)

    ciphertext = aesgcm.encrypt(
        nonce,
        plaintext.encode("utf-8"),
        None
    )

    return base64.b64encode(
        nonce + ciphertext
    ).decode("ascii")


def decrypt_sensitive_data(encrypted_value):
    key = get_encryption_key()

    encrypted_bytes = base64.b64decode(
        encrypted_value,
        validate=True
    )

    nonce = encrypted_bytes[:12]
    ciphertext = encrypted_bytes[12:]

    aesgcm = AESGCM(key)

    plaintext = aesgcm.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode("utf-8")
