"""Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.

For example:
Test 	Result

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())
0

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))
100

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))
200"""

class Account:

    def __init__(self, account_id: str):
        self.account_id = account_id
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount
        return self.balance
    
    def get_balance(self):
        return self.balance
    
class Bank:

    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id): #crea un nuovo account con l'ID specificato e un saldo pari a 0.
        if self.accounts.get(account_id):
            print("Account with this ID already exists")
        else:
            account = Account(account_id)
            self.accounts[account_id] = account
            return account
    
    def deposit(self, account_id, amount): #deposita l'importo specificato sul conto con l'ID fornito.
        if self.accounts.get(account_id):
            return self.accounts[account_id].deposit(amount)
            
    def get_balance(self, account_id): #restituisce il saldo del conto con l'ID specificato.
        if self.accounts.get(account_id):
            return self.accounts[account_id].get_balance()
        else:
            print("Account not found")


bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())
#0

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))
#100

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))
#200

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""Progettare un sistema di videonoleggio con i seguenti requisiti:

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
    get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.
"""

class Movie:

    def __init__(self, movie_id, title, director):
        self.movie_id: str = movie_id #Identificatore di un film.
        self.title: str = title #Titolo del film.
        self.director: str = director # Regista del film.
        self.is_rented: bool = False # Booleano che indica se il film è noleggiato o meno.

    def rent(self):
        if self.is_rented == False:
            self.is_rented = True
            return
        else:
            print (f"Il filmn '{self.title}' è già noleggiato.")

    def return_movie(self):
        if self.is_rented:
            self.is_rented = False
            return
        else:
            print (f"Il filmn '{self.title}' non è stato noleggiato da questo cliente.")


class Customer:

    def __init__(self, customer_id, name):
        self.customer_id: str = customer_id # Identificativo del cliente.
        self.name: str = name # Nome del cliente.
        self.rented_movies: list[Movie] = [] # Lista dei film noleggiati.

    def rent_movie(self, movie: Movie): 
        """Aggiunge il film nella lista rented_movies se non è già stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già noleggiato."""
        if movie not in self.rented_movies:
            movie.rent()
            self.rented_movies.append(movie)
            return
        else:
            print(f"Il film '{movie.title}' è già noleggiato.")
    
    def return_movie(self, movie: Movie): 
        """Rimuove il film dalla lista rented_movies se già presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato noleggiato da questo cliente."""
        if movie  in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
            return
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")


class VideoRentalStore:

    def __init__(self):
        self.movies: dict = {}
        self.customers: dict = {}

    def add_movie(self, movie_id: str, title: str, director: str): 
        """Aggiunge un nuovo film nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con ID '{movie_id}' esiste già."""
        if not self.movies.get(movie_id):
            movie = Movie(movie_id,title,director)
            self.movies[movie_id] = movie
        else:
            print(f"Il film con ID '{movie_id}' esiste già.")

    def register_customer(self, customer_id: str, name: str): 
        """Iscrive un nuovo cliente nel videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente con ID '{customer_id}' è già registrato."""
        if not self.customers.get(customer_id):
            customer = Customer(customer_id, name)
            self.customers[customer_id] = customer
        else:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")

    def rent_movie(self, customer_id: str, movie_id: str): 
        """Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."""
        if self.customers.get(customer_id) and self.movies.get(movie_id):
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.rent_movie(movie)
            return
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str): 
        """Permette al cliente di restituire un film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio "Cliente o film non trovato."""
        if self.customers.get(customer_id) and self.movies.get(movie_id):
            customer = self.customers[customer_id]
            movie = self.movies[movie_id]
            customer.return_movie(movie)
            return
        else:
            print("Cliente o film non trovato.")
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]: 
        """Restituisce la lista dei film noleggiati dal client (customer.rented_movies) se il cliente esiste nel videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota."""
        if self.customers.get(customer_id):
            customer = self.customers[customer_id]
            return customer.rented_movies

        
# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")
videonoleggio.register_customer("102", "Bob")

# Noleggio di film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("102", "2")

# Tentativo di noleggiare un film già noleggiato
videonoleggio.rent_movie("101", "1")

# Restituzione di film
videonoleggio.return_movie("101", "1")

# Tentativo di restituire un film non noleggiato
videonoleggio.return_movie("101", "1")

# Ottenere la lista dei film noleggiati da un cliente
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

rented_movies_bob = videonoleggio.get_rented_movies("102")
print(f"Film noleggiati da Bob: {[movie.title for movie in rented_movies_bob]}")

# Creazione di un nuovo videonoleggio
videonoleggio = VideoRentalStore()

# Aggiunta di nuovi film
videonoleggio.add_movie("1", "Inception", "Christopher Nolan")
videonoleggio.add_movie("2", "The Matrix", "Wachowski Brothers")
videonoleggio.add_movie("3", "Interstellar", "Christopher Nolan")

# Registrazione di nuovi clienti
videonoleggio.register_customer("101", "Alice")

# Noleggio di più film
videonoleggio.rent_movie("101", "1")
videonoleggio.rent_movie("101", "2")

# Verifica dei film noleggiati da Alice
rented_movies_alice = videonoleggio.get_rented_movies("101")
print(f"Film noleggiati da Alice: {[movie.title for movie in rented_movies_alice]}")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente."""

class RecipeManager:

    def __init__(self):
        self.receituario: dict = {}

    def create_recipe(self, name, ingredients): 
       """ Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già."""
       if not self.receituario.get(name):
           self.receituario[name] = ingredients
           return self.receituario

    def add_ingredient(self, recipe_name, ingredient): 
        """Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste."""
        if self.receituario.get(recipe_name):
            if ingredient not in self.receituario[recipe_name]:
                self.receituario[recipe_name].append(ingredient)
                return self.receituario

    def remove_ingredient(self, recipe_name, ingredient): 
        """Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste."""
        if self.receituario.get(recipe_name):
            if ingredient in self.receituario[recipe_name]:
                self.receituario[recipe_name].remove(ingredient)
                return self.receituario

    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient): 
        """Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste."""
        if self.receituario.get(recipe_name):
            for index, ingredient in enumerate(self.receituario[recipe_name]):
                if old_ingredient == ingredient:
                    self.receituario[recipe_name][index] = new_ingredient
                    return self.receituario
                
    def list_recipes(self): 
        """Elenca tutte le ricette esistenti."""
        res = []
        for key in self.receituario.keys():
            res.append(key)
        return res

    def list_ingredients(self, recipe_name):
        """Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste."""
        if self.receituario.get(recipe_name):
            return self.receituario[recipe_name]

        
    def search_recipe_by_ingredient(self, ingredient): 
        """Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente."""
        res = {}
        counter = 0
        for key, value in self.receituario.items():
            if ingredient in value:
                res[key] = value
                counter += 1
        if counter == 0:
            print("None")
        else:
            return res

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di veicoli.
 
1. Classe Base: Veicolo
Crea una classe base chiamata Veicolo con i seguenti attributi e metodi:
 
Attributi:
- marca (stringa)
- modello (stringa)
- anno (intero)

Metodi:
- __init__(self, marca, modello, anno): metodo costruttore che inizializza gli attributi marca, modello e anno.
- descrivi_veicolo(self): metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".

2. Classe Derivata: Auto
Crea una classe derivata chiamata Auto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
- numero_porte (intero)

Metodi:
- __init__(self, marca, modello, anno, numero_porte): metodo costruttore che inizializza gli attributi della classe base e numero_porte.
- descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il - numero di porte nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Numero di porte: [numero_porte]".

3. Classe Derivata: Moto
Crea una classe derivata chiamata Moto che eredita dalla classe Veicolo e aggiunge i seguenti attributi e metodi:
 
Attributi:
- tipo (stringa, ad esempio "sportiva", "cruiser", ecc.)

Metodi:
- __init__(self, marca, modello, anno, tipo): metodo costruttore che inizializza gli attributi della classe base e tipo.
- descrivi_veicolo(self): metodo che sovrascrive quello della classe base per includere anche il tipo di moto nella descrizione, nel formato "Marca: [marca], Modello: [modello], Anno: [anno], Tipo: [tipo]"."""

class Veicolo:
    
    def __init__(self, marca, modello, anno): # metodo costruttore che inizializza gli attributi marca, modello e anno.
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi_veicolo(self): #metodo che stampa una descrizione del veicolo nel formato "Marca: [marca], Modello: [modello], Anno: [anno]".
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
    
class Auto(Veicolo):

    def __init__(self, marca, modello, anno, numero_porte): 
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte
    
    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno},  Numero di porte: {self.numero_porte}")

class Moto(Veicolo):

    def __init__(self, marca, modello, anno, tipo): 
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno},  Tipo: {self.tipo}")



veicolo = Veicolo("Generic", "Model", 2020)  # Crea un'istanza della classe Veicolo
auto = Auto("Toyota", "Corolla", 2021, 4)  # Crea un'istanza della classe Auto
moto = Moto("Yamaha", "R1", 2022, "sportiva")  # Crea un'istanza della classe Moto

veicolo.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Veicolo
auto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Auto
moto.descrivi_veicolo()  # Test del metodo descrivi_veicolo per Moto