def set_taxpayers_id(nome, cognome, data_di_nascita, genere, comune_di_nascita):
    nome = nome.upper()
    cognome = cognome.upper()
    consoanti: list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    mesi: dict = {'01': 'A', '02': 'B', '03': 'C', '04': 'D', '05': 'E', '06': 'H', '07': 'L', '08': 'M', '09': 'P', '10': 'R', '11': 'S', '12': 'T'}
    place_of_birth: dict = {"Roma": "H501", "Sora": "I838", "Milano": "F205", "Estero": "Z602"}

    # 3 caratteri alfabetici per il cognome
    three_consoanti_cognome = [letter for letter in cognome if letter in consoanti][:3] 
    while len(three_consoanti_cognome) != 3:
        for letter in nome:
            if letter not in consoanti:
                three_consoanti_cognome += letter
    three_consoanti_cognome = "".join(three_consoanti_cognome)

    # 3 caratteri alfabetici per il nome
    three_consoanti_nome = [letter for letter in nome if letter in consoanti][:3]
    while len(three_consoanti_nome) != 3:
        for letter in nome:
            if letter not in consoanti:
                three_consoanti_nome += letter
    three_consoanti_nome = "".join(three_consoanti_nome)

    # 2 caratteri numerici per l'anno di nascita;
    two_numbers_year: str = data_di_nascita[-2:]

    # 1 carattere alfabetico per il mese di nascita;
    one_char_month: str = data_di_nascita[-7:-5]
    one_char_month: str = mesi[one_char_month]

    # 2 caratteri numerici per il giorno di nascita ed il sesso;
    two_char_day_of_birth: str = data_di_nascita[0:2]
    if genere.upper() == "WOMAN":
        two_char_day_of_birth = int(two_char_day_of_birth)
        two_char_day_of_birth += 30
        two_char_day_of_birth = str(two_char_day_of_birth)

    # 4 caratteri associati al Comune oppure allo Stato estero di nascita.
    if comune_di_nascita in place_of_birth: 
        four_char_place_of_birth: str = place_of_birth[comune_di_nascita]
    else:
        four_char_place_of_birth: str = place_of_birth["Estero"]

    # 1 carattere alfabetico usato come carattere di controllo"""
    from calcola_carattere_controllo import calcola_carattere_controllo
    codice_fiscale_senza_controll = three_consoanti_cognome + three_consoanti_nome + two_numbers_year + one_char_month + two_char_day_of_birth + four_char_place_of_birth
    char_control = calcola_carattere_controllo(codice_fiscale_senza_controll)
    codice_fiscale = three_consoanti_cognome + three_consoanti_nome + two_numbers_year + one_char_month + two_char_day_of_birth + four_char_place_of_birth + char_control

    return codice_fiscale

CF_Michele = set_taxpayers_id(nome = "Michele", cognome = "Fontevecchia", data_di_nascita = "06/10/1967", genere = "Man", comune_di_nascita="Sora")
