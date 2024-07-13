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


    
""""Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.
- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.
- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.
- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito."""

# library = Library()

# library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
# library.add_book("1984", "George Orwell")
# library.add_book("To Kill a Mockingbird", "Harper Lee")

# library.borrow_book("1984")
# library.borrow_book("The Great Gatsby")
# library.return_book("The Great Gatsby")


# print(library.show_available_books())

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

    
# movie_catalog = MovieCatalog()
# movie_catalog.add_movie("Apocalypse Now", "Francis Ford Coppola")
# movie_catalog.add_movie("The Godfather", "Francis Ford Coppola")
# movie_catalog.add_movie("Pulp Fiction", "Quentin Tarantino")
# movie_catalog.add_movie("Jaws", "Steven Spielberg")
# movie_catalog.add_movie("E.T. the Extra-Terrestrial", "Steven Spielberg")
# movie_catalog.add_movie("Schindler\'s List", "Steven Spielberg")
# print("print movie director - Coppola:\n", movie_catalog.get_movies_by_director("Francis Ford Coppola"))
# print("")
# print("print movie director - Tarantino:\n", movie_catalog.get_movies_by_director("Quentin Tarantino"))
# print("")
# print("print movie director - Spielberg:\n",movie_catalog.get_movies_by_director("Steven Spielberg"))
# print("")
# movie_catalog.remove_movie("Apocalypse Now", "Francis Ford Coppola")
# print("print movie director - Coppola (after del 1 movie):\n",movie_catalog.get_movies_by_director("Francis Ford Coppola"))
# print("")
# print(movie_catalog.list_directors())
# print("")
# print("search movies: A \n", movie_catalog.search_movies_by_title("A"))
# print("")
# print("search movies: fiction \n", movie_catalog.search_movies_by_title("fiction"))
# print("")
# #print("search movies: brasil \n", movie_catalog.search_movies_by_title("brasil"))
# #movie_catalog.add_movie("Jaws", "Steven Spielberg")



