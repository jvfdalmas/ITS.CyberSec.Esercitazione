"""1. Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

For example:
Test 	Result
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
[1, 3, 4]
print(rimuovi_elementi([], {2: 1})) 
[]"""

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    for elemento in lista:
        if elemento in da_rimuovere:
            if da_rimuovere[elemento] >=1:
                lista.remove(elemento)
                da_rimuovere[elemento] -= 1
    return lista


print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2})) #[1, 3, 4]
print(rimuovi_elementi([], {2: 1})) #[]

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""2. Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

For example:
Test 	Result
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
{'Alice': [90, 85], 'Bob': [75]}
print(aggrega_voti([])) 
{}"""

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    dict_finale: dict = {}
    
    if len(voti) == 0:
        return dict_finale
    else:
        for element in voti:
            for key, value in element.items():
                if key == "nome":
                    if value not in dict_finale:
                        dict_finale[value] = [element["voto"]]
                    elif value in dict_finale:
                        dict_finale[value].append(element["voto"])

    return dict_finale

# alternativa 1:

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    dict_finale: dict = {}
    
    if len(voti) == 0:
        return dict_finale
    else:
        for dizionario in voti:
            nome: str = dizionario['nome']
            voto: int = dizionario['voto']
            if nome not in dict_finale:
                dict_finale[nome] = [voto]
            elif nome in dict_finale:
                dict_finale[nome].append(voto)

    return dict_finale

# alternativa 2:

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    dict_finale: dict = {}
    
    if len(voti) == 0:
        return dict_finale
    else:
        for dizionario in voti:
            if dizionario['nome'] not in dict_finale:
                dict_finale[dizionario['nome']] = [dizionario['voto']]
            elif dizionario['nome'] in dict_finale:
                dict_finale[dizionario['nome']].append(dizionario['voto'])
                
    return dict_finale

print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}])) # {'Alice': [90, 85], 'Bob': [75]}
print(aggrega_voti([]))  #{}

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

""" 3. Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

For example:
Test 	Result
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

{'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
{}"""

def filtra_e_mappa(prodotti) -> dict:
    dict_risultato: dict = {} 
    for key, value in prodotti.items():
        if value > 20:
            scontato: float = value * 0.9
            dict_risultato[key] = scontato

    return dict_risultato

    pass

print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0})) # {'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) #{}

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

""" 4.
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

For example:
Test 	Result

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))"""

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    create_contact_list: dict = {'profile': name}

    if email != None:
        create_contact_list["email"] = email
    else:
        create_contact_list["email"] = None    

    if telefono != None:
        create_contact_list["telefono"] = telefono
    else:
        create_contact_list["telefono"] = None

    return create_contact_list


def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    updated_dictionary: dict = dictionary

    if email is not None:
        updated_dictionary["email"] = email
    if telefono is not None:
        updated_dictionary["telefono"] = telefono

    return updated_dictionary

contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)) # {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 788787}
print(update_contact(contact, "Mario Rossi", telefono=123456789)) # {'profile': 'Mario Rossi', 'email': 'mario.rossi@gmail.com', 'telefono': 123456789}