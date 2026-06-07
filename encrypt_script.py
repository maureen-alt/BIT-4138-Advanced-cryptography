import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def encrypt_data(plaintext_bytes):
    # Generate a secure, random 256-bit AES key (32 bytes)
    key = os.urandom(32)
    # Generate a random 128-bit Initialization Vector (16 bytes)
    iv = os.urandom(16)
    
    # AES requires blocks to be exactly 128 bits. Pad the plaintext if it's not.
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext_bytes) + padder.finalize()
    
    # Set up the AES-CBC cipher
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    return key, iv, ciphertext

if __name__ == "__main__":
    print("\n[INFO] Initializing Local Encryption Script...")
    print("[INFO] Generating secure 256-bit AES key...")
    
    # The message you want to encrypt
    secret_message = "Confidential Project Blueprint 2026"
    print(f"[INFO] Target plaintext prepared.")
    
    print("\n" + "-"*50)
    print(f'Original Plaintext:  "{secret_message}"')
    print("-"*50)
    
    # Convert string to bytes and encrypt
    plaintext_bytes = secret_message.encode('utf-8')
    key, iv, ciphertext = encrypt_data(plaintext_bytes)
    
    # Convert ciphertext to a readable Hex string for display
    ciphertext_hex = ciphertext.hex()
    
    print("\n[SUCCESS] Encryption process complete.")
    print(f"[OUTPUT]  Ciphertext (Hex): {ciphertext_hex[:60]}...")
    
    # Save the ciphertext to a local file
    output_filename = "sensitive_data.enc"
    with open(output_filename, "wb") as f:
        f.write(ciphertext)
        
    print(f"[INFO] Encrypted data successfully saved to '{output_filename}'\n")