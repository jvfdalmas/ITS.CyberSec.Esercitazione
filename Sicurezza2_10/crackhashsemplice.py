import hashlib
from itertools import product

def verifica_hash(hash_target, lunghezza):
    """
    Tenta un attacco a forza bruta per trovare una stringa che corrisponde all'hash SHA-256.
    
    Args:
        hash_target (str): L'hash SHA-256 da verificare
        lunghezza (int): Lunghezza delle stringhe da generare
        
    Returns:
        None: Stampa il risultato se trova una corrispondenza
    """
    caratteri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    print(f"Verifica di stringhe di lunghezza {lunghezza}...")
    trovato = False
    
    # Genera tutte le possibili combinazioni di caratteri di lunghezza specificata
    for combinazione in product(caratteri, repeat=lunghezza):
        stringa_candidata = ''.join(combinazione)
        
        # Calcola l'hash SHA-256 della stringa candidata
        hash_calcolato = hashlib.sha256(stringa_candidata.encode('utf-8')).hexdigest()
        
        # Verifica se questa stringa corrisponde all'hash target
        if hash_calcolato == hash_target:
            print(f"Trovato! La stringa originale è: '{stringa_candidata}'")
            trovato = True
            break
    
    if not trovato:
        print("Nessuna corrispondenza trovata nelle stringhe testate.")

if __name__ == "__main__":
    # L'hash target da verificare
    hash_target = "43238848111bee151a4bb951be3e9d5b57fa023e6d65ce4f72f9cf021cae5412"
    
    # Esegui l'attacco a forza bruta
    verifica_hash(hash_target, 12)
