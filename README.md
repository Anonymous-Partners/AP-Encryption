# AP-Encryption
## Prereqs
You must have python installed on your computer with pip. The cryptography module should be included by default, but if it isn't run the following command:
```
python -m pip install cryptography
```
## Usage
Modify the must_encrypt.txt file to include whatever text you want to enecrypt. If you have another type of file (i.e. .png .pdf etc), change the path in encrypt.py to match whatever you want to encrypt. Once you have done this, run the following command:
```
python encrypt.py
```
This will generate your encrypted file for you along with a private_key.pem and public_key.pem. You must keep private_key.pem safe, otherwise anyone can read your file. You may share public_key.pem if you want to allow other users to encrypt files that only you have the key to read. This is the basis of how the internet works, by the way. Once you're ready to decrypt your file, modify the file paths in decrypt.py to match your own and run the following command:
```
python decrypt.py
```
This will return your decrypted file.
