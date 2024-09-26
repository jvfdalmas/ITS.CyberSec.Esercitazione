
# creazione environment, per evitare che ubuntu non vi faccia installare la libreria di crittografia
# python -m venv .venv
# e poi:
# . .venv/bin/activate
# e poi fare pip install pycryptodome
#

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


# # Per importare una chiave pubblica
# keyDER = base64.b64decode(pubkey)
# seq = base64.asn1.DerSequence()
# seq.decode(keyDER)
# keyPub = RSA.construct((seq[0], seq[1]))

# # Per iniziare generiamo una coppia di chiavi e le stampiamo
# # Generating RSA Key Pair
# # Una volta stampate, non serve più
# key_pair = RSA.generate(2048)
# print(key_pair.export_key())
# public_key = key_pair.publickey()
# print(public_key.export_key())
# exit(0)

sPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAyTGzV5s15h+J8+XVJOHLUdmErSnQwWM7K6BCv6IvodsdvSMV\nQBsYndOsV1wFWPGBN3q1tk+FcxGFMJPPMjIvS4g684EUzo0J+6gf5TAYrqpgCYF2\nOQYk6KXXbEsR3CTqhMvjqiXhgOOECMNBQRkDQCED2yJbQ23uSWxVAjXM4ZmUfvH/\nYjc3KJL0zP0E7LAPJDJN80/hskbwtckhxIUMRECQl5SvoHW9CqZHSHLH0gMsSGxG\nmFqIfdlLw7dSYiB9rziLvJboxR7KDsvLYzEQ7GQ7xEwXfqUZrZHtHVFwj41MNzNX\nUzxVFreFzaUtrnKgqAcA9B2sRdf31Xs9NyFuVwIDAQABAoIBACHmuQSDB8L9/33U\ndWTgkyT4lQ2kpSNg+CBywayOxJ3uUQWEutjxd+VoPHr/63rAPvi9OY89uQvZoOq9\njUU1BZkhnGVZk8r2Iv9/pdg1kYMk/Ee9w9D6AxAcmb8KqzjAE7BKttL9zRCtxZrA\nY+d3MoAE0CSFloE3Lda7ZVuY+yvsKwiMud22Qiv4KodSYdA2wJIFF2psS+bOp33W\nfosjJsU3a5RSTgynf0wxKfYtMbmPPfcrk08zS3i1YD+M6lmCAmJNz6esuL9YBAXN\ndvUPlivzuSNvdteuFoquwHbpJb4yyuJ8cBCuNiNJ5xO0iSpXUuxEc0ej9SQNke5x\nQ5QSXHECgYEAympi913n7ZXZ/zG9zF2XB4Ayy017tccJcdo9+3VgU1PoeoCsREjb\nxDdw2Cpc6scBw6IqOnyQtvQ+MCloS4n6kDdNZ/zY8mI49UBuUzhPzg1QaB/AVmSf\nZVx921+QFGapx8rLwIi8yHaChcrr3cJyvZPr5PdjFTUth4xVU1e1368CgYEA/nSJ\nyFNPuwVlg/TZDePck28at0469BgPwBSkM16FL2/vGWkXVM9k1vaS7IZa2w4W6Nww\nsirL3bsyKdaZ//7salHrI/4juNwHn05XnCJKOXJs4+m1FODhR7a/kS5cG8xVVukX\n/fjJV5jDvznKVLNC+Ey1PAXVfIV2xByoOD5gHdkCgYBmB+ho/onpJc8kJuOgP1Dg\n9AsmlaEVSQYGwNbbiRgMCNC352JubTdyGewk2n3JzpSiE30rzBx6THWIe2baJOwL\nhATdtQN6cm55mYfDJTB9EhME2XRvV/tM8alzSiFrVzCfyCaan5JhjfNPE7F/MAP8\ncbLH0Le+OfcAS4m7IAxKewKBgEu++0kD6+cbayXF3FszKnVFDKnmgswo4X9nZZ3Z\nFEKTypRA4W4gsr7+9autLxyobA9zhJd0/+0IjZ1AweUfyNa5fgrf21hrP2Wf15ql\n5nyFYH7UElCdxNIpR4t7RnYL9JeDmd3DkoQd+J9TH7TpDBWIGCc/AVcpD7q/YSAl\nCU25AoGAB+O875LYDv9AxupzTIASSob/BwmyTVXT/b7pfJkxd4hqsDhl0BlK6wkQ\nhDpPpFaAEzKfjhtyKpLTCfAAWQuxZphIqlfGwET+FWlF0j6vJU3upHIEAGDts4Tv\nDZiuGtUexlfCcYWGOXxj1aeYU1bNJfLNEvyhT+KPHbLVEjkFal8=\n-----END RSA PRIVATE KEY-----"

sPub = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyTGzV5s15h+J8+XVJOHL\nUdmErSnQwWM7K6BCv6IvodsdvSMVQBsYndOsV1wFWPGBN3q1tk+FcxGFMJPPMjIv\nS4g684EUzo0J+6gf5TAYrqpgCYF2OQYk6KXXbEsR3CTqhMvjqiXhgOOECMNBQRkD\nQCED2yJbQ23uSWxVAjXM4ZmUfvH/Yjc3KJL0zP0E7LAPJDJN80/hskbwtckhxIUM\nRECQl5SvoHW9CqZHSHLH0gMsSGxGmFqIfdlLw7dSYiB9rziLvJboxR7KDsvLYzEQ\n7GQ7xEwXfqUZrZHtHVFwj41MNzNXUzxVFreFzaUtrnKgqAcA9B2sRdf31Xs9NyFu\nVwIDAQAB\n-----END PUBLIC KEY-----"

sPub_Jordy = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2pTuat8TMyK3i5fmBqGC\nnnyFbE5XEIfb9eqqYdlrYykQYmWPPPev/sFE8dJPImRrKqO1PeinI8LMrU1P+zlb\nSzJQz4lO5akeZM5RXDcoFm1rMz2qLmbYPkR9QNziFWL6SSOwgdKfGT0FOnTrqU7R\nYEqRa6wzlBQ2Rzat2Vik6s6ejajQ6GVm5azAXM70/Dr4LBYJ1X74IWJn0b681E9M\n/V7CBOfRbkwtYCBPfAgjva4Rvs8fgMTFZ3ogaD/E1+boh+dIuwcmFyz6VxD9R4p1\nFFsSw/2Qkvgyv4DUPp5oJGXnPobMNcNJ6iTzqQSL9Neec4SZ3F5/iETzKU7mzF7U\nvQIDAQAB\n-----END PUBLIC KEY-----" # per criptare messagio a Jordy

# Ora dobbiamo ricreare le chiavi a partire da queste due stringhe
key_pair = RSA.import_key(sPriv)
public_key = RSA.import_key(sPub)
public_key_jordy= RSA.import_key(sPub_Jordy)


# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")


# Example usage
message = "This is NOT a secret message!!!!"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)
print("\n")
print("Original Message:", message, "\n")
print("Encrypted Message:", encrypted_message, "\n")
print("Decrypted Message:", decrypted_message, "\n")

encrypted_message_from_jordy = "vic5/tILVXa4Ejl5mwLQ7gQxyUXRGrNBiDv0rzfwvwoFSJsFnSnpmgxzl4U5n9gsHFWmweUHDyDLLAejCr9JYtkMzQgcu8AaW9PeXNAAPNqZgl5yL1MxsOErXt5NKJ2ogaz8kI2KueUKYwB2T4C5w0yRoKsVm3PmHJ/enLjYw0cZEr4XvJO1uCo+n6Fk2XWiEVBOpt1OjC+k0w8DGHOK5wlNuatUJ4Re2yFK/52XPNEXX+qhkBXcP/cvpRrTwziQ0ne5tc2puHDf+Aec6bGr1w6Zu1Tumf2h6wUDjW7WPlVVJ8TYU1wdZY7X7lkdNXYuD/06cudO0hanKOOxUy0kbg=="
decrypted_message_from_jordy = decrypt_message(encrypted_message_from_jordy, key_pair)
print("Encrypted Message from Jordy:", encrypted_message_from_jordy, "\n")
print("Decrypted Message from Jordy:", decrypted_message_from_jordy, "\n")

encrypted_message_to_jordy = encrypt_message("La guerra non è ancora finita!", public_key_jordy)
print("Encrypted Message to Jordy:", encrypted_message_to_jordy, "\n")