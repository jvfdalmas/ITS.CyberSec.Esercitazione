# Sistema di Gestione Biblioteca

print("Sistema di Gestione Biblioteca - Soluzione: \n")

"""Sistema Avanzato di Gestione Biblioteca. Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.

Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore. """

class Book:

    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow(self) -> bool:
        if self.is_borrowed == False:
            self.is_borrowed = True

    def return_book(self) -> bool:
        if self.is_borrowed == True:
            self.is_borrowed = False


class Library:

    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
    
    def add_book(self, title: str, author: str) -> None:
        book = Book(title, author)
        self.books[title] = book
        return book
    
    def borrow_book(self, book_title: str) -> None:
        if self.books.get(book_title) is not None:
            if self.books[book_title].is_borrowed == False:
                self.books[book_title].borrow()
            else:
                raise ValueError("Book is already borrowed")
        else:
            raise ValueError("Book not found")

    def return_book(self, book_title: str) -> None:
        if self.books[book_title].is_borrowed == True:
            self.books[book_title].return_book()
        else:
            raise ValueError("Book not borrowed")

    def show_available_books(self) -> list[str]:
        available_books: list = [book.title for book in self.books.values() if book.is_borrowed == False]
        if not available_books:
            raise ValueError("There are no books available")
        else:
            return f"available books: {available_books}"

    
""""Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito."""

library = Library()

library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

library.borrow_book("1984")
library.borrow_book("The Great Gatsby")
library.return_book("The Great Gatsby")


print(library.show_available_books())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 
# Catalogo Film
print("Catalogo Film - Soluzione: \n")

"""Catalogo Film. Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere, rimuovere e cercare film di un particolare regista. Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog(): Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo. Se il regista non esiste, viene creato un nuovo record. Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista. Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la parola cercata nel titolo."""

class MovieCatalog:

    def __init__(self) -> None:
        self.catalog: dict = {}

    def add_movie(self, movie_title: str, movie_director: str) -> None:
        if movie_director not in self.catalog:
            self.catalog[movie_director] = [movie_title]
        else:
            if movie_title not in self.catalog[movie_director]:
                self.catalog[movie_director].append(movie_title)
            else:
                raise ValueError("this movie is already in the catalog")

    def remove_movie(self, movie_title: str, movie_director: str) -> None:
        if movie_title in self.catalog[movie_director]:
            self.catalog[movie_director].remove(movie_title)
            if self.catalog[movie_director] == []:
                del self.catalog[movie_director]

    def list_directors(self):
        list_directors: list[str] = [director_name for director_name in self.catalog.keys()]
        return list_directors
    
    def get_movies_by_director(self, director_name: str) -> list:
        if self.catalog.get(director_name):
            return self.catalog[director_name]
        
    def search_movies_by_title(self, title) -> str:
        risult = {}

        for director_name, movies_list in self.catalog.items():
            for movie in movies_list:
                if title.lower() in movie.lower():
                    if director_name not in risult:
                        risult[director_name] = [movie]
                    else:
                        risult[director_name].append(movie)
        
        if risult == []:
            raise ValueError("No movie found with this word")
        else:
            return risult
    
movie_catalog = MovieCatalog()
movie_catalog.add_movie("Apocalypse Now", "Francis Ford Coppola")
movie_catalog.add_movie("The Godfather", "Francis Ford Coppola")
movie_catalog.add_movie("Pulp Fiction", "Quentin Tarantino")
movie_catalog.add_movie("Jaws", "Steven Spielberg")
movie_catalog.add_movie("E.T. the Extra-Terrestrial", "Steven Spielberg")
movie_catalog.add_movie("Schindler\'s List", "Steven Spielberg")
print("print movie director - Coppola:\n", movie_catalog.get_movies_by_director("Francis Ford Coppola"))
print("")
print("print movie director - Tarantino:\n", movie_catalog.get_movies_by_director("Quentin Tarantino"))
print("")
print("print movie director - Spielberg:\n",movie_catalog.get_movies_by_director("Steven Spielberg"))
print("")
movie_catalog.remove_movie("Apocalypse Now", "Francis Ford Coppola")
print("print movie director - Coppola (after del 1 movie):\n",movie_catalog.get_movies_by_director("Francis Ford Coppola"))
print("")
print(movie_catalog.list_directors())
print("")
print("search movies: A \n", movie_catalog.search_movies_by_title("A"))
print("")
print("search movies: fiction \n", movie_catalog.search_movies_by_title("fiction"))
print("")
#print("search movies: brasil \n", movie_catalog.search_movies_by_title("brasil"))
#movie_catalog.add_movie("Jaws", "Steven Spielberg")



