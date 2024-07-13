"""1. Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono essere rimossi come valori.

For example:
Test 	Result
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
[1, 3, 4]
print(rimuovi_elementi([], {2: 1})) 
[]"""



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""2. Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

For example:
Test 	Result
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
{'Alice': [90, 85], 'Bob': [75]}
print(aggrega_voti([])) 
{}"""


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

""" 3. Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo superiore a 20, scontati del 10%.

For example:
Test 	Result
print(filtra_e_mappa({'Penna': 15.0, 'Zaino': 50.0, 'Quaderno': 22.0}))

{'Zaino': 45.0, 'Quaderno': 19.8}
print(filtra_e_mappa({'Gomma': 2.0, 'Matita': 1.0})) 
{}"""


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
