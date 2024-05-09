def calcola_carattere_controllo(codice_fiscale: str) -> str:
   
    conversione_pari: dict = {
    'A': 0, 'F': 5, 'K': 10, 'P': 15, 'U': 20,
    'B': 1, 'G': 6, 'L': 11, 'Q': 16, 'V': 21,
    'C': 2, 'H': 7, 'M': 12, 'R': 17, 'W': 22,
    'D': 3, 'I': 8, 'N': 13, 'S': 18, 'X': 23,
    'E': 4, 'J': 9, 'O': 14, 'T': 19, 'Y': 24,
    'Z': 25, "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9 }

    conversione_dispari: dict = {
    'A': 1, 'F': 13, 'K': 2, 'P': 3, 'U': 16,
    'B': 0, 'G': 15, 'L': 4, 'Q': 6, 'V': 10,
    'C': 5, 'H': 17, 'M': 18, 'R': 8, 'W': 22,
    'D': 7, 'I': 19, 'N': 20, 'S': 12, 'X': 25,
    'E': 9, 'J': 21, 'O': 11, 'T': 14, 'Y': 24,
    'Z': 23, "0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, 
    "6": 15, "7": 17, "8": 19, "9": 21 }

    conversione_check_digit: dict = {
    0: 'A', 5: 'F', 10: 'K', 15: 'P', 20: 'U',
    1: 'B', 6: 'G', 11: 'L', 16: 'Q', 21: 'V',
    2: 'C', 7: 'H', 12: 'M', 17: 'R', 22: 'W',
    3: 'D', 8: 'I', 13: 'N', 18: 'S', 23: 'X',
    4: 'E', 9: 'J', 14: 'O', 19: 'T', 24: 'Y',
    25: 'Z'}

    calculum_list_pari: list = [conversione_pari[char] for i, char in enumerate(list(codice_fiscale))if i in [1, 3, 5, 7, 9, 11, 13]]
    calculum_list_dispari: list = [conversione_dispari[char] for i, char in enumerate(list(codice_fiscale)) if i in [0, 2, 4, 6, 8, 10, 12, 14]]

    char_controllo: str = conversione_check_digit[sum(calculum_list_dispari + calculum_list_pari) % 26]

    return char_controllo
