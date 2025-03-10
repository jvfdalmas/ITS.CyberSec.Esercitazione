def trova_trasposizione(stringa_codificata, output_atteso):
    """
    Analizza diversi metodi di trasposizione per trovare quello che produce l'output atteso.
    """
    # Rimuoviamo gli spazi dagli input
    codificata_pulita = stringa_codificata.replace(" ", "")
    atteso_pulito = output_atteso.replace(" ", "")
    
    print(f"Lunghezza stringa codificata: {len(codificata_pulita)}")
    print(f"Lunghezza output atteso: {len(atteso_pulito)}")
    
    # Dividiamo in gruppi come mostrato
    gruppi = stringa_codificata.split()
    print(f"Gruppi: {gruppi}")
    print(f"Numero di gruppi: {len(gruppi)}")
    
    # Proviamo a leggere in colonne (verticalmente)
    colonne = []
    max_len = max(len(gruppo) for gruppo in gruppi)
    
    for i in range(max_len):
        colonna = ""
        for gruppo in gruppi:
            if i < len(gruppo):
                colonna += gruppo[i]
        colonne.append(colonna)
    
    decodifica_verticale = "".join(colonne)
    print(f"Decodifica verticale (leggendo per colonne): {decodifica_verticale}")
    
    # Proviamo a riorganizzare i caratteri in una matrice e leggerli in diversi modi
    
    # Metodo 1: Riempiamo una matrice per righe e leggiamo per colonne
    righe = len(gruppi)
    colonne = max_len
    
    matrice = []
    for i in range(righe):
        riga = []
        for j in range(colonne):
            if j < len(gruppi[i]):
                riga.append(gruppi[i][j])
            else:
                riga.append('')
        matrice.append(riga)
    
    # Stampiamo la matrice
    print("\nMatrice creata dai gruppi:")
    for riga in matrice:
        print(riga)
    
    # Leggiamo la matrice per colonne
    risultato_per_colonne = ""
    for j in range(colonne):
        for i in range(righe):
            if matrice[i][j] != '':
                risultato_per_colonne += matrice[i][j]
    
    print(f"\nLettura per colonne: {risultato_per_colonne}")
    
    # Proviamo altri metodi di decodifica
    
    # Metodo 2: Trasposizione a spirale
    print("\nProviamo metodi alternativi:")
    
    # Stringa completa senza spazi
    stringa_completa = codificata_pulita
    
    # Ricreiamo la matrice in un modo diverso
    num_righe = 5  # Prova con diverse dimensioni
    num_colonne = (len(stringa_completa) + num_righe - 1) // num_righe
    
    matrice_alt = [['' for _ in range(num_colonne)] for _ in range(num_righe)]
    
    # Riempiamo la matrice per righe
    indice = 0
    for i in range(num_righe):
        for j in range(num_colonne):
            if indice < len(stringa_completa):
                matrice_alt[i][j] = stringa_completa[indice]
                indice += 1
    
    print("\nMatrice alternativa (5x7):")
    for riga in matrice_alt:
        print(riga)
    
    # Leggiamo per colonne
    risultato_alt = ""
    for j in range(num_colonne):
        for i in range(num_righe):
            if matrice_alt[i][j] != '':
                risultato_alt += matrice_alt[i][j]
    
    print(f"Lettura per colonne (matrice 5x7): {risultato_alt}")
    
    # Proviamo con dimensioni diverse
    num_righe = 6
    num_colonne = (len(stringa_completa) + num_righe - 1) // num_righe
    
    matrice_alt2 = [['' for _ in range(num_colonne)] for _ in range(num_righe)]
    
    # Riempiamo la matrice per righe
    indice = 0
    for i in range(num_righe):
        for j in range(num_colonne):
            if indice < len(stringa_completa):
                matrice_alt2[i][j] = stringa_completa[indice]
                indice += 1
    
    print("\nMatrice alternativa (6x6):")
    for riga in matrice_alt2:
        print(riga)
    
    # Leggiamo per colonne
    risultato_alt2 = ""
    for j in range(num_colonne):
        for i in range(num_righe):
            if matrice_alt2[i][j] != '':
                risultato_alt2 += matrice_alt2[i][j]
    
    print(f"Lettura per colonne (matrice 6x6): {risultato_alt2}")
    
    # Ricreiamo la matrice in un altro modo ancora
    # Proviamo con dimensioni 4x9
    num_righe = 4
    num_colonne = (len(stringa_completa) + num_righe - 1) // num_righe
    
    matrice_alt3 = [['' for _ in range(num_colonne)] for _ in range(num_righe)]
    
    # Riempiamo la matrice per righe
    indice = 0
    for i in range(num_righe):
        for j in range(num_colonne):
            if indice < len(stringa_completa):
                matrice_alt3[i][j] = stringa_completa[indice]
                indice += 1
    
    print("\nMatrice alternativa (4x9):")
    for riga in matrice_alt3:
        print(riga)
    
    # Leggiamo per colonne
    risultato_alt3 = ""
    for j in range(num_colonne):
        for i in range(num_righe):
            if matrice_alt3[i][j] != '':
                risultato_alt3 += matrice_alt3[i][j]
    
    print(f"Lettura per colonne (matrice 4x9): {risultato_alt3}")
    
    # Verifico se corrisponde all'output atteso
    if risultato_per_colonne.replace(" ", "") == atteso_pulito:
        print("\nIl metodo di lettura per colonne della matrice originale corrisponde all'output atteso!")
    elif risultato_alt.replace(" ", "") == atteso_pulito:
        print("\nIl metodo di lettura per colonne della matrice 5x7 corrisponde all'output atteso!")
    elif risultato_alt2.replace(" ", "") == atteso_pulito:
        print("\nIl metodo di lettura per colonne della matrice 6x6 corrisponde all'output atteso!")
    elif risultato_alt3.replace(" ", "") == atteso_pulito:
        print("\nIl metodo di lettura per colonne della matrice 4x9 corrisponde all'output atteso!")
    else:
        print("\nNessuno dei metodi testati corrisponde esattamente all'output atteso.")
        
        # Confronto con l'output atteso
        print("\nConfrontiamo le lettere tra l'output atteso e i nostri risultati:")
        print(f"Output atteso (senza spazi): {atteso_pulito}")
        
        # Confrontiamo con ogni risultato
        print("\nConfrontando con risultato_per_colonne:")
        for i, (a, b) in enumerate(zip(atteso_pulito, risultato_per_colonne.replace(" ", ""))):
            if a != b:
                print(f"Posizione {i}: Atteso '{a}', Ottenuto '{b}'")
        
        # Proviamo a manipolare direttamente la stringa originale
        print("\nProviamo un'ultima cosa: visualizziamo la stringa senza spazi come matrice 6x6:")
        matrice_diretta = []
        for i in range(0, len(codificata_pulita), 6):
            matrice_diretta.append(codificata_pulita[i:i+6])
        
        for riga in matrice_diretta:
            print(riga)
        
        # Leggiamo per colonne
        risultato_diretto = ""
        for j in range(6):  # 6 colonne
            for i in range(len(matrice_diretta)):
                if j < len(matrice_diretta[i]):
                    risultato_diretto += matrice_diretta[i][j]
        
        print(f"Lettura per colonne della matrice diretta: {risultato_diretto}")
        
        if risultato_diretto.replace(" ", "") == atteso_pulito:
            print("Il metodo di lettura per colonne della matrice diretta corrisponde all'output atteso!")

# Stringa codificata fornita
stringa_codificata = "STRIL EIAOI IASNC DDPEE AUOSV NSEAA IMNTZ P"
output_atteso = "DISPONIAMO DI CINQUE AIUTI SENZA P"

# Eseguire l'analisi
trova_trasposizione(stringa_codificata, output_atteso)