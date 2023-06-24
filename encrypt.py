from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def encrypt_file(public_key_path, file_path, output_path):
    with open(public_key_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_path, 'wb') as file:
        file.write(ciphertext)

def generate_key_pair(private_key_path, public_key_path):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=8192
    )

    with open(private_key_path, 'wb') as key_file:
        key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    public_key = private_key.public_key()

    with open(public_key_path, 'wb') as key_file:
        key_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    return private_key, public_key

if __name__ == '__main__':
    private_key_path = 'private_key.pem'
    public_key_path = 'public_key.pem'

    private_key, public_key = generate_key_pair(private_key_path, public_key_path)
    
    file_path = 'must_encrypt.txt'
    output_path = 'encrypted_file.txt'
    encrypt_file(public_key_path, file_path, output_path)
