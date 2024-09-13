"""Sapendo che la chiave di cifra è: XXXXIsASecretKey

(non conoscete i primi 4 caratteri della chiave)

e che il messaggio cifrato è: OgJuOYJZT0FDb47DBOkNgA==

NB: la parte ignota delle chiave contiene esclusivamente maiuscole e minuscole

Trovare la decodifica del messaggio."""

from Crypto.Cipher import AES
import base64
import string

# Function to pad the message to be multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

partial_key = "IsASecretKey"
encrypted_text = "OgJuOYJZT0FDb47DBOkNgA=="
decrypted_text = ""

ascii = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
res = []
for p1 in ascii:
    for p2 in ascii:
        for p3 in ascii:
            for p4 in ascii:
                key = p1 + p2 + p3 + p4 + partial_key
                try:
                    decrypt(encrypted_text, key)
                except:
                    continue
                else:
                    str = decrypt(encrypted_text, key)
                    res.append(str)
                    print(str)
print(res)