"""1. Scrivi una funzione che prenda un dizionario e un valore, e ritorni una lista con tutte le chiavi che corrispondono a quel valore, o una lista vuota se il valore non è presente.
For example:

Test	Result
print(trova_tutte_chiavi({'a': 1, 'b': 2, 'c': 1}, 1))
['a', 'c']
print(trova_tutte_chiavi({}, 1))
[]"""

def trova_tutte_chiavi(dizionario: dict[str: int], valore: int) -> str:
    res = []
    for key, value in dizionario.items():
        if value == valore:
            res.append(key)
    return res

"""2.Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
For example:

Test	Result
print(transform(4))
2
print(transform(-10))
-5"""

def transform(x: int) -> int:
    if x % 2 == 0:
        return x/2
    else:
        return x*3-1

"""3. Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, moltiplica i loro valori.
For example:

Test	Result
print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  
{'a': 1, 'b': 6, 'c': 4}
print(merge_dictionaries({'x': 5}, {'x': -5}))                 
{'x': -25}"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] *= value
        else:
            dict1[key] = value
    return dict1

"""4. Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa" oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.
For example:

Test	Result
print(verifica_condizioni(True, False, True))
Azione permessa
print(verifica_condizioni(True, False, False))
Azione negata"""

def verifica_condizioni(X: bool, Y: bool, Z: bool) -> str:
    if X and (Y or Z):
        return "Azione permessa"
    else:
        return "Azione negata"

"""5. Scrivi una funzione che, data una lista di parole, ritorni un dizionario che mappa ogni parola alla sua lunghezza.
For example:

Test	Result
print(mappa_parole_a_lunghezza(["apple", "banana", "cherry"]))
{'apple': 5, 'banana': 6, 'cherry': 6}
print(mappa_parole_a_lunghezza(["elephant"]))
{'elephant': 8}"""

def mappa_parole_a_lunghezza(words: list) -> dict:
    res = {}
    for word in words:
        res[word] = len(word)
    return res

"""6. Sviluppare una funzione in Python per calcolare lo stipendio lordo di ciascuno dei diversi impiegati. L'azienda paga 10 dollari all'ora per le prime 40 ore di lavoro e paga "una volta e mezza" la paga oraria per tutte le ore di lavoro oltre le 40 ore.
 
Per ogni operaio, viene fornito il numero di ore che tale impiegato ha lavorato durante la settimana.
La vostra funzione deve ricevere questa informazione per ogni impiegato e determinare e stampare lo stipendio lordo.
For example:

Test	Result
print(calcola_stipendio(40))
400.0
print(calcola_stipendio(0))
0.0"""

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        return float(10 * ore_lavorate)
    else:
        return float(400 + 15*(ore_lavorate - 40))
    
"""7. Scrivere un frammento di codice che modifichi il valore intero memorizzato nella variabile n nel seguente modo:
se n è pari, deve essere incrementato di 10;
se n è dispari, deve essere decrementato di 5.
For example:

Test	Result
n1 = 8
print(modifica_valore(n1))
18
n4 = -4
print(modifica_valore(n4))
6"""

def modifica_valore(n: int) -> int:
    if n % 2 == 0:
        return n + 10
    else:
        return n - 5
    
"""8. Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che classifichi i numeri in liste separate per numeri positivi e negativi.

For example:

Test	Result
print(classifica_numeri([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
{'positivi': [1, 3, 5, 7, 9], 'negativi': [-2, -4, -6, -8, -10]}
print(classifica_numeri([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
{'positivi': [], 'negativi': [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]}"""

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    res = {'positivi': [], 'negativi': []}
    for n in lista:
        if n > 0:
            res['positivi'].append(n)
        else:
            res['negativi'].append(n)
    return res

"""9. Si scriva una funzione in Python che simuli una palla che rimbalza calcolando la sua altezza da terra in centimetri per ogni secondo, a mano a mano che il tempo passa su un orologio simulato.

Al tempo zero la palla comincia ad altezza zero e ha una velocità iniziale di 100 cm/s.

Dopo ogni secondo, il valore dell'altezza cambia, aggiungendo al valore corrente dell'altezza il valore della velocità corrente; poi, il valore della velocità viene modificato, sottraendo 96 al valore della velocità corrente.
Dunque, dopo ogni secondo, si ha che
altezza = altezza + velocità
velocità = velocità - 96.
 
Se il nuovo valore che si ottiene per l'altezza è inferiore a 0, si deve moltiplicare altezza e velocità per -0.5 per simulare il rimbalzo. Dunque, per il rimbalzo, si avrà che
altezza= altezza*-0,5 
velocità=velocità*-0,5.

Ci si fermi al quinto rimbalzo.
 
Per ogni secondo, la funzione deve stampare il tempo trascorso e l'altezza a cui si trova la palla in quel determinato secondo.
Ad esempio, se al tempo 0, la palla si trova ad altezza 0 cm, allora la funzione stamperà:
 
"Tempo: 0 Altezza: 0"
 
Se avviene il rimbalzo, la funzione deve stampare il tempo trascorso e la parola "Rimbalzo!".
Ad esempio, se il rimbalzo avviene al tempo 4, allora la funzione stamperà:
 
"Tempo: 4 Rimbalzo!"
For example:

Test	Result
rimbalzo()
Tempo: 0 Altezza: 0.0
Tempo: 1 Altezza: 100.0
Tempo: 2 Altezza: 104.0
Tempo: 3 Altezza: 12.0
Tempo: 4 Rimbalzo!
Tempo: 5 Altezza: 88.0
Tempo: 6 Altezza: 230.0
Tempo: 7 Altezza: 276.0
Tempo: 8 Altezza: 226.0
Tempo: 9 Altezza: 80.0
Tempo: 10 Rimbalzo!
Tempo: 11 Altezza: 81.0
Tempo: 12 Altezza: 250.0
Tempo: 13 Altezza: 323.0
Tempo: 14 Altezza: 300.0
Tempo: 15 Altezza: 181.0
Tempo: 16 Rimbalzo!
Tempo: 17 Altezza: 17.0
Tempo: 18 Altezza: 172.5
Tempo: 19 Altezza: 232.0
Tempo: 20 Altezza: 195.5
Tempo: 21 Altezza: 63.0
Tempo: 22 Rimbalzo!
Tempo: 23 Altezza: 82.75
Tempo: 24 Altezza: 245.0
Tempo: 25 Altezza: 311.25
Tempo: 26 Altezza: 281.5
Tempo: 27 Altezza: 155.75
Tempo: 28 Rimbalzo!"""

def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while rimbalzi != 5:
        print(f"Tempo: {tempo} Altezza: {altezza}")
        tempo += 1
        altezza += velocita
        velocita -= 96   
        if altezza <= 0:
            rimbalzi += 1
            print(f"Tempo: {tempo} Rimbalzo!")
            altezza = altezza * -0.5 
            velocita = velocita * -0.5
            tempo += 1

"""10.  Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un dato valore intero definito threshold.
For example:

Test	Result
print(moltiplica_numeri([15, 5, 25], 20))
75"""

def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
    res = 1
    for n in numbers:
        if n < threshold:
            res *= n
    return res

"""11. Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.
1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.
 
Attributi:
contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per valore una lista di numeri di telefono. I numeri di telefono sono espressi sottoforma di stringa.
Metodi:
create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.
add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero di telefono è già presente per il contatto specificato.
remove_phone_number(contact_name: str, phone_number: str): Rimuove un numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
update_phone_number(contact_name: str, old_phone_number: str, new_phone_number: str): Sostituisce un numero di telefono con un altro nel contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.
list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di errore "Errore: il contatto non esiste." se il contatto non esiste.
search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i contatti che contengono un determinato numero di telefono. Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono." se nessun contatto contiene il numero di telefono."""

class ContactManager:

    def __init__(self):
        self.contacts: dict[str, list[str]] = {} # Dizionario che ha per chiave il nome del contatto e per valore una lista di numeri di telefono. I numeri di telefono sono espressi sottoforma di stringa.
    
    def create_contact(self, name: str, phone_numbers: list[str]): 
        """Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già."""
        if name not in self.contacts:
            res = {}
            self.contacts[name] = phone_numbers
            res[name] = phone_numbers
            return res
        else:
            return "Errore: il contatto esiste già."
        
    def add_phone_number(self, contact_name: str, phone_number: str): 
        """Aggiunge un numero di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero di telefono è già presente per il contatto specificato."""
        if contact_name in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                res = {}
                self.contacts[contact_name].append(phone_number)
                res[contact_name] = self.contacts[contact_name]
                return res
            else:
                return "Errore: il numero di telefono esiste già."
        else:
            return "Errore: il contatto non esiste."
    
    def remove_phone_number(self, contact_name: str, phone_number: str): 
        """Rimuove un numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato."""
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                res = {}
                self.contacts[contact_name].remove(phone_number)
                res[contact_name] = self.contacts[contact_name]
                return res
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str): 
        """Sostituisce un numero di telefono con un altro nel contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato."""
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                res = {}
                for index, item in enumerate(self.contacts[contact_name]):
                    if item == old_phone_number:
                        self.contacts[contact_name][index] = new_phone_number
                        res[contact_name] = self.contacts[contact_name]
                        return res
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."

    def list_contacts(self): 
        """Ritorna una lista di tutte le chiavi all'interno del dizionario contacts."""
        res = [key for key in self.contacts.keys()]
        return res


    def list_phone_numbers(self, contact_name: str): 
        """Mostra i numeri di telefono di un contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di errore "Errore: il contatto non esiste." se il contatto non esiste."""
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return "Errore: il contatto non esiste."

    def search_contact_by_phone_number(self, phone_number: str): 
        """Trova e restituisce tutti i contatti che contengono un determinato numero di telefono. Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono." se nessun contatto contiene il numero di telefono."""
        res = []
        for key, value in self.contacts.items():
            if phone_number in value:
                res.append(key)
        return res

"""12. Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 4"""

def print_seq(): 
    
    print("Sequenza a):")
    for n in range(2,16,2):
        print(n)
    print("\n")

    print("Sequenza b):")
    for n in range(1,14,3):
        print(n)
    print("\n")

    print("Sequenza c):")
    for n in range(30, -1, -5):
        print(n)
    print("\n")

    print("Sequenza d):")
    for n in range(5, 46, 10):
        print(n)
    print("\n")
    
    return

"""13. Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.

Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.

For example:

Test	Result
print(hypotenuse(3.0, 4.0))
5.0
print(hypotenuse(8.0, 15.0))
17.0"""

import math

def hypotenuse(lato1: float, lato2: float) -> float:
    return math.sqrt(lato1**2 + lato2**2)

"""14. Obiettivo
L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale. Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- n quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche
1. Classe Specie

- Attributi:
nome (str): Nome della specie.
popolazione (int): Popolazione iniziale.
tasso_crescita (float): Tasso di crescita annuo percentuale.
- Metodi:
__init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float): Costruttore per inizializzare gli attributi della classe.
cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².
 
2. Sottoclassi BufaloKlingon e Elefante

Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:
Aggiornamento della popolazione per l'anno successivo:
Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)
Calcolo della densità di popolazione:
Formula: popolazione / area_kmq
Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²
Calcolo degli anni necessari per superare la popolazione di un'altra specie:
Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di questa specie non supera quella dell'altra. Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000."""

class Specie:

    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome: str = nome  # Nome della specie.
        self.tasso_crescita: float = tasso_crescita  # Tasso di crescita annuo percentuale.
        self.popolazione_attuale: float = popolazione_iniziale  # Popolazione iniziale.

    def cresci(self):  # Metodo per aggiornare la popolazione per l'anno successivo.
        self.popolazione_attuale = int(self.popolazione_attuale * (1 + self.tasso_crescita / 100))
        return self.popolazione_attuale

    def anni_per_superare(self, altra_specie: 'Specie') -> int:  # Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.
        anni_necessari: int = 0
        max_anni: int = 1000

        while self.popolazione_attuale < altra_specie.popolazione_attuale and anni_necessari < max_anni:
            anni_necessari += 1
            self.cresci()
            altra_specie.cresci()            
        
        if anni_necessari == max_anni:
            return f"Le popolazioni non si incontreranno in {max_anni} anni"
        
        anni_necessari = anni_necessari
        return anni_necessari

    def getDensita(self, area_kmq: float) -> int:  # Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km².
        anni_densita: int = 0
        densita: float = self.popolazione_attuale / area_kmq
        while self.popolazione_attuale / area_kmq < 1:
            anni_densita += 1
            self.cresci()

        anni_densita = anni_densita

        return anni_densita


class Elefante(Specie):

    def __init__(self, popolazione_iniziale: int, tasso_crescita: float, nome: str = "Elefante"):
        super().__init__(nome, popolazione_iniziale, tasso_crescita)


class BufaloKlingon(Specie):

    def __init__(self, popolazione_iniziale: int, tasso_crescita: float, nome: str = "Bufalo Klingon"):
        super().__init__(nome, popolazione_iniziale, tasso_crescita)


# Sottoclasse per Bufalo Klingon
class BufaloKlingon(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Bufalo Klingon", popolazione_iniziale, tasso_crescita)  # Inizializza la classe base

# Sottoclasse per Elefante
class Elefante(Specie):
    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)  # Inizializza la classe base

# Creazione delle istanze delle specie
bufalo_klingon = BufaloKlingon(100, 15)  # Crea un'istanza di BufaloKlingon con popolazione 100 e tasso di crescita 15%
elefante = Elefante(10, 35)  # Crea un'istanza di Elefante con popolazione 10 e tasso di crescita 35%

# Calcolo degli anni necessari per superare
anni_necessari = elefante.anni_per_superare(bufalo_klingon)  # Calcola gli anni necessari affinché gli elefanti superino i bufali Klingon
print(f"Anni necessari perché la popolazione di elefanti superi quella dei bufali Klingon: {anni_necessari}")

# Calcolo della densità di popolazione per i Bufali Klingon
anni_densita = bufalo_klingon.getDensita(1500)  # Calcola gli anni necessari per raggiungere una densità di 1 bufalo Klingon per km²
print(f"Anni necessari per raggiungere una densità di 1 Bufalo Klingon per km quadrato: {anni_densita}")

"""15. Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se la chiave è già presente, somma il valore al valore già associato alla chiave.

For example:

Test	Result
print(lista_a_dizionario([("a", 1), ("b", 2), ("c", 3)]))
{'a': 1, 'b': 2, 'c': 3}
print(lista_a_dizionario([("a", 1), ("a", 2), ("a", 3)]))
{'a': 6}"""

def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    res = {}
    for item in tuples:
        if item[0] not in res:
            res[item[0]] = item[1]
        else:
            res[item[0]] += item[1]
    return res

"""16. Progettare un sistema di videonoleggio con i seguenti requisiti:

1. Classe Movie:

Attributi:

movie_id: str - Identificatore di un film.
title: str - Titolo del film.
director: str - Regista del film.
is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
Metodi:

rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il film '{self.title}' è già noleggiato."
return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è stato noleggiato da questo cliente."
2. Classe Customer:

Attributi:

customer_id: str - Identificativo del cliente.
name: str - Nome del cliente.
rented_movies: list[Movie] - Lista dei film noleggiati.
Metodi:

rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già noleggiato."
return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato noleggiato da questo cliente."
3. Classe VideoRentalStore:

Attributi:

movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.
Metodi:

add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con ID '{movie_id}' esiste già."
register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente con ID '{customer_id}' è già registrato."
rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."
get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota."""

class Movie:
    def __init__(self, movie_id: str, title: str, director: str):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False
    
    def rent(self):
        if self.is_rented:
            print(f"Il film '{self.title}' è già noleggiato.")
        else:
            self.is_rented = True
    
    def return_movie(self):
        if not self.is_rented:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")
        else:
            self.is_rented = False

class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []
    
    def rent_movie(self, movie: Movie):
        if movie.is_rented:
            print(f"Il film '{movie.title}' è già noleggiato.")
        else:
            self.rented_movies.append(movie)
            movie.rent()
    
    def return_movie(self, movie: Movie):
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            movie.return_movie()
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    def __init__(self):
        self.movies = {}
        self.customers = {}
    
    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies:
            print(f"Il film con ID '{movie_id}' esiste già.")
        else:
            self.movies[movie_id] = Movie(movie_id, title, director)
    
    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")
        else:
            self.customers[customer_id] = Customer(customer_id, name)
    
    def rent_movie(self, customer_id: str, movie_id: str):
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)
        
        if customer and movie:
            customer.rent_movie(movie)
        else:
            print("Cliente o film non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str):
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)
        
        if customer and movie:
            customer.return_movie(movie)
        else:
            print("Cliente o film non trovato.")
    
    def get_rented_movies(self, customer_id: str):
        customer = self.customers.get(customer_id)
        
        if customer:
            return customer.rented_movies
        else:
            print("Cliente non trovato.")
            return []
        
"""17. Progettare un semplice sistema di gestione di studenti e corsi con i seguenti requisiti:
 
1. Classe Student:
Attributi:
student_id: str - identificatore univoco per lo studente.
courses: list[str] - la lista dei corsi ai quali lo studente è iscritto.
Metodi:
enroll(course: str) - aggiunge il corso specificato alla lista dei corsi dello studente oppure stampa il messaggio "Lo studente è già iscritto al corso {course}."
get_courses(): restituisce la lista dei corsi ai quali lo studente è iscritto.
Classe School:
Attributi:
students: dict[str, Student] - un dizionario per memorizzare gli studenti, in cui la chiave è una stringa ID mentre il valore è un oggetto di tipo Studente.
Metodi:
create_student(student_id: str): crea un nuovo studente con l'ID specificato e una lista di corsi vuota oppure stampa il messaggio "Lo studente con ID {student_id} esiste già."
enroll_student(student_id: str, course: str): se lo studente esiste viene iscritto al corso specificato, altrimenti  stampa il messaggio "Studente non trovato."
get_student_courses(student_id: str): se lo studente esiste restituisce la lista dei corsi dello studente con l'ID specificato, altrimenti ritorna il messaggio "Studente non trovato."
get_stundent_list(): Ritorna una lista di tutte le chiavi all'interno del dizionario students.
search_by_course(self, course: str): Trova e restituisce tutti gli ID degli studenti iscritti ad un determinato corso. Restituisce una lista di tutte le chiavi all'interno del dizionario students che hanno il corso specificato tra i valori oppure il messaggio di errore "Nessuno studente è iscritto al corso {course}." se non ci sono studenti che frequentano il corso specificato."""

class Student:
    def __init__(self, student_id: str):
        self.student_id = student_id
        self.courses = []
    
    def enroll(self, course: str):
        if course in self.courses:
            print(f"Lo studente è già iscritto al corso {course}.")
        else:
            self.courses.append(course)
    
    def get_courses(self):
        return self.courses

class School:
    def __init__(self):
        self.students = {}
    
    def create_student(self, student_id: str):
        if student_id in self.students:
            print(f"Lo studente con ID {student_id} esiste già.")
        else:
            self.students[student_id] = Student(student_id)
    
    def enroll_student(self, student_id: str, course: str):
        if student_id in self.students:
            self.students[student_id].enroll(course)
        else:
            print("Studente non trovato.")
    
    def get_student_courses(self, student_id: str):
        if student_id in self.students:
            return self.students[student_id].get_courses()
        else:
            return "Studente non trovato."
    
    def get_student_list(self):
        return list(self.students.keys())
    
    def search_by_course(self, course: str):
        enrolled_students = [student_id for student_id, student in self.students.items() if course in student.get_courses()]
        if enrolled_students:
            return enrolled_students
        else:
            return f"Nessuno studente è iscritto al corso {course}."

"""18. Si immagini una funzione che comprime i file all'80% e li salva su un supporto di memorizzazione. Prima che il file compresso venga memorizzato, deve essere diviso in blocchi da 512 byte ciascuno.
 
Si sviluppi in Python un algoritmo per questa funzione che prende in input una lista di valori interi, dove ogni valore intero della lista rappresenta la dimensione non compressa di un singolo file espressa in byte.
 
Tale funzione deve utilizzare un ciclo per iterare la lista e, per ogni dimensione non compressa, deve calcolare la dimensione compressa di tale file espressa come float (ovvero deve calcolare l' 80% della dimensione non compressa), calcolare il numero di blocchi (arrotondato al numero intero più vicino) da 512 byte necessari per la memorizzazione, al fine di determinare se il file compresso può essere salvato nello spazio rimanente nel supporto di memorizzazione o meno.
 
In caso affermativo, il programma memorizza il file. In tal caso, la funzione deve stampare la dimensione originale del file, la dimensione compressa, i blocchi utilizzati per memorizzare il file in questione e i blocchi disponibili rimasti sul supporto di memorizzazione. 
Ad esempio, se è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1100 byte, la funzione stamperà:
 
"File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998."
 
Il ciclo continua finché non viene riscontrato un file della lista la cui dimensione compressa occupa un numero di blocchi più grande di quelli rimasti disponibili sul supporto di memorizzazione. In tal caso, la funzione deve avvisare l'utente che lo spazio disponibile sul supporto di memorizzazione non è sufficiente per salvare il file. 
Ad esempio, se non è possibile salvare sul supporto di memorizzazione un file avente dimensione pari a 1048576 byte, la funzione stamperà:
 
"Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."
Inizialmente, il numero totale di blocchi disponibili sul supporto di memorizzazione per il salvataggio dei file è un numero intero pari a 1000 blocchi. 

For example:

Test	Result
memorizza_file([1100, 20000, 1048576, 512, 5000])
File di 1100 byte compresso in 880.0 byte e memorizzato. Blocchi usati: 2. Blocchi rimanenti: 998.
File di 20000 byte compresso in 16000.0 byte e memorizzato. Blocchi usati: 31. Blocchi rimanenti: 967.
Non è possibile memorizzare il file di 1048576 byte. Spazio insufficiente."""

def memorizza_file(file_sizes):
    blocchi_totali = 1000  # Numero totale di blocchi disponibili
    blocco_dimensione = 512  # Dimensione di un singolo blocco in byte
    
    for file_size in file_sizes:
        # Calcola la dimensione compressa (80% della dimensione originale)
        compressed_size = file_size * 0.8
        
        # Calcola il numero di blocchi necessari per memorizzare il file compresso
        blocchi_necessari = int(round(compressed_size / blocco_dimensione))
        
        # Verifica se ci sono abbastanza blocchi disponibili per memorizzare il file
        if blocchi_necessari <= blocchi_totali:
            # Aggiorna il numero di blocchi disponibili
            blocchi_totali -= blocchi_necessari
            print(f"File di {file_size} byte compresso in {compressed_size} byte e memorizzato. "
                  f"Blocchi usati: {blocchi_necessari}. Blocchi rimanenti: {blocchi_totali}.")
        else:
            # Non ci sono abbastanza blocchi per memorizzare il file
            print(f"Non è possibile memorizzare il file di {file_size} byte. Spazio insufficiente.")
            break

"""19. Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
For example:

Test	Result
print(filtra_e_mappa({"prodotto1": 30.0, "prodotto2": 60.0, "prodotto3": 45.0}))
{'prodotto1': 33.0, 'prodotto3': 49.5}
print(filtra_e_mappa({"prodotto1": 55.0, "prodotto2": 70.0, "prodotto3": 80.0}))
{}"""

def filtra_e_mappa(prodotti_prezzi):
    prodotti_filtrati = {
        prodotto: round(prezzo * 1.1, 2) 
        for prodotto, prezzo in prodotti_prezzi.items()
        if prezzo < 50}
    return prodotti_filtrati

"""20. Scrivi una funzione che accetti tre parametri: user, passw e stato dell'account (attivo/non attivo). L'accesso è consentito solo se il nome utente è "manager", la password corrisponde a "67890" e l'account è attivo (True). La funzione ritorna "Ingresso consentito" oppure "Ingresso negato".
For example:

Test	Result
print(verifica_accesso("manager", "67890", True))
Ingresso consentito
print(verifica_accesso("manager", "wrongpassword", True))
Ingresso negato"""

def verifica_accesso(user, passw, account_attivo):
    if user == "manager" and passw == "67890" and account_attivo:
        return "Ingresso consentito"
    else:
        return "Ingresso negato"