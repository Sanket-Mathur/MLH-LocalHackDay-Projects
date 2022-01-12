# Encrypt a Password

A script to encrypt a password by reversing the string and shifting the characters by an entered key.

# Steps to execute
- Ensure a python installation in the system
- Execute the encrypt.py script and enter the key and message to encrypt
  ```
  python encrypt.py
  ```
- Execute the decrypt.py script and enter the key and message to decrypt
  ```
  python decrypt.py
  ```

# Sample Output
- Encrypting the message
  ```
  Enter an integer key: 8
  Enter a message to encrypt: SuperSecretPassword
  Encrypted Message:
  lzw{{iX|mzkm[zmx}[
  ```
- Decrypting the message
  ```
  Enter an integer key: 8
  Enter a encrypted message: lzw{{iX|mzkm[zmx}[
  Decrypted Message:
  SuperSecretPassord
  ```