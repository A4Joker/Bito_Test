from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

import sys

class AESHandler:
    @classmethod
    def generate_random(cls):
        key = get_random_bytes(32)
        key_hex = binascii.hexlify(key).decode('utf-8')
        return cls(key_hex)

    def get_key(self):
        return self.aes_key

    def __init__(self, aes_key):
        self.aes_key = aes_key

    def encrypt_file(self, input_file_path, output_file_path):
        # Convert the hexadecimal key to bytes
        key = binascii.unhexlify(self.aes_key)
        
        # Generate a random 16-byte IV
        iv = get_random_bytes(16)
        
        # Create AES cipher in CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        with open(input_file_path, 'rb') as input_file:
            plaintext = input_file.read()
        
        # Pad the plaintext to be a multiple of the block size (16 bytes)
        padded_plaintext = pad(plaintext, AES.block_size)
        
        # Encrypt the padded plaintext
        ciphertext = cipher.encrypt(padded_plaintext)
        
        # Write the IV followed by the ciphertext to the output file
        with open(output_file_path, 'wb') as output_file:
            output_file.write(iv + ciphertext)
    
    def decrypt_file(self, input_file_path, output_file_path):
        # Convert the hexadecimal key to bytes
        key = binascii.unhexlify(self.aes_key)
        
        with open(input_file_path, 'rb') as input_file:
            # Read the IV from the beginning of the file
            iv = input_file.read(16)
            # Read the rest of the file as the ciphertext
            ciphertext = input_file.read()
        
        # Create AES cipher in CBC mode
        cipher = AES.new(key, AES.MODE_CBC, iv)
        
        # Decrypt and unpad the plaintext
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext, AES.block_size)
        
        # Write the plaintext to the output file
        with open(output_file_path, 'wb') as output_file:
            output_file.write(plaintext)


def main():
    command = command = sys.argv[1]
    if command == "generate":
        handler = AESHandler.generate_random()
        print(handler.get_key())
        return
    if command == "encrypt":
        key = sys.argv[2]
        handler = AESHandler(key)
        input_file = sys.argv[3]
        output_file = input_file + ".enc"
        decrypted_file = input_file + ".dec"
        handler.encrypt_file(input_file, output_file)
        handler.decrypt_file(output_file, decrypted_file)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()

# python3 aes.py generate
# python3 aes.py encrypt <key> input.txt