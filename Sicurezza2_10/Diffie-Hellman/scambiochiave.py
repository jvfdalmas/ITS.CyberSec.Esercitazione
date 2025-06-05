import random

def diffie_hellman_key_exchange():
    # Parametri pubblici (primo p e generatore g)
    p = 929  # Un numero primo
    g = 900  # Un generatore primitivo modulo p

    print(f"Parametri pubblici: p = {p}, g = {g}")

    # Parte Alice: sceglie una chiave privata casuale
    a = random.randint(1, p - 1)
    A = (g ** a) % p  # Calcola la chiave pubblica di Alice

    # Parte Bob: sceglie una chiave privata casuale
    b = random.randint(1, p - 1)
    B = (g ** b) % p  # Calcola la chiave pubblica di Bob

    print(f"Alice invia a Bob la sua chiave pubblica: A = {A}")
    print(f"Bob invia ad Alice la sua chiave pubblica: B = {B}")

    # Alice calcola la chiave condivisa
    shared_key_alice = (B ** a) % p
    print(f"Alice calcola la chiave condivisa: {shared_key_alice}")

    # Bob calcola la chiave condivisa
    shared_key_bob = (A ** b) % p
    print(f"Bob calcola la chiave condivisa: {shared_key_bob}")

    # Verifica che le chiavi condivise siano uguali
    assert shared_key_alice == shared_key_bob, "Le chiavi condivise non corrispondono!"
    print(f"Chiave condivisa: {shared_key_alice}")

if __name__ == "__main__":
    diffie_hellman_key_exchange()