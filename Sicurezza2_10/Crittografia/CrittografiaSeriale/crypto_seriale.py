from Crypto.Cipher import AES
import base64
import random
import time

# Generazione della chiave basata su un seed
def generate_serial_keys(text_length):
    seed = int(time.time())  # Seed basato sul tempo attuale
    random.seed(seed)
    keys = [''.join(chr(random.randint(32, 126)) for _ in range(16)) for _ in range(text_length)]  # Genera una chiave diversa per ogni carattere
    return keys

# Crittografia seriale
def encrypt_serial(plain_text, keys):
    encrypted_chars = []
    for i, char in enumerate(plain_text):
        cipher = AES.new(keys[i].encode('utf-8'), AES.MODE_ECB)
        encrypted_char = cipher.b64decodeencrypt(char.ljust(16).encode('utf-8'))
        encrypted_chars.append(base64.b64encode(encrypted_char).decode('utf-8'))
    return encrypted_chars

# Decrittografia seriale
def decrypt_serial(encrypted_chars, keys):
    decrypted_chars = []
    for i, encrypted_char in enumerate(encrypted_chars):
        cipher = AES.new(keys[i].encode('utf-8'), AES.MODE_ECB)
        decrypted_char = cipher.decrypt(base64.b64decode(encrypted_char)).decode('utf-8').strip()
        decrypted_chars.append(decrypted_char)
    return ''.join(decrypted_chars)

# Esempio di utilizzo
plain_text = "Hello, World!"
keys = generate_serial_keys(len(plain_text))
encrypted_text = encrypt_serial(plain_text, keys)
decrypted_text = decrypt_serial(encrypted_text, keys)

print("Chiavi Serializzate:", keys)
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
