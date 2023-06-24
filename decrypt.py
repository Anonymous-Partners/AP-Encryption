from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

def decrypt_file(private_key_path, encrypted_file_path, output_path):
    with open(private_key_path, 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None
        )

    with open(encrypted_file_path, 'rb') as file:
        ciphertext = file.read()

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_path, 'wb') as file:
        file.write(plaintext)

if __name__ == '__main__':
    private_key_path = 'private_key.pem'
    encrypted_file_path = 'encrypted_file.txt'
    output_path = 'decrypted_file.txt'

    decrypt_file(private_key_path, encrypted_file_path, output_path)
