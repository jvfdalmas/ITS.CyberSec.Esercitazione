def calcola_carattere_controllo(codice_fiscale):
    tabella_conversione = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    coefficienti = [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2, 4, 18, 20, 11, 3, 6, 8, 12, 14, 16, 10, 22, 25, 24, 23]
    
    codice_fiscale = codice_fiscale.upper()
    somma = 0
    
    for i, char in enumerate(codice_fiscale):
        if char.isalpha():
            somma += coefficienti[i] * (ord(char) - ord('A'))
        else:
            somma += coefficienti[i] * int(char)
    
    resto = somma % 26
    carattere_controllo = tabella_conversione[resto]
    
    return carattere_controllo

