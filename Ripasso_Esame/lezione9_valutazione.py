"""Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.

La lista di interi è formata così:

    L'elemento in posizione 0 corrisponde alla radice
    Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
    Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
    Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che corrisponde a quell'indice è una foglia.

Potete utilizzare la classe TreeNode per crearvi prima l'albero - anziché usare la lista tree - e poi visitare l'albero sfruttando gli oggetti di tipo TreeNode.

For example:
Test 	Result
print(symmetric([1,2,2,3,4,4,3]))
True"""



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 
print("Determina se una tavola Sudoku 9 x 9 è valida:\n")
"""Determina se una tavola Sudoku 9 x 9 è valida. Solo le celle compilate devono essere convalidate secondo le seguenti regole:

    Ogni riga deve contenere le cifre 1-9 senza ripetizioni.
    Ciascuna colonna deve contenere le cifre da 1 a 9 senza ripetizioni.
    Ciascuno dei nove sottoriquadri 3 x 3 della griglia deve contenere le cifre 1-9 senza ripetizione.

Nota:

    Una tavola Sudoku (parzialmente riempita) potrebbe essere valida ma non è necessariamente risolvibile.
    Solo le celle riempite devono essere convalidate secondo le regole menzionate.

Test 	Result
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))
True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board))
False"""

def valid_sudoku(board: list[list]):
    pass

# ------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.
Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
For example:
Test 	Result
print(word_break("leetcode",["leet","code"]))
True
print(word_break("applepenapple", ["apple","pen"]))
True
print(word_break("catsandog",["cats","dog","sand","and","cat"]))
False"""

def word_break_memo(word: str, wordDict: list[str]) -> bool:
    memo={}
    if word in memo: return memo[word]
    if word in wordDict:
        memo[word] = True
        return True

    for i in range(1, len(word)):
        prefix, suffix = word[:i], word[i:]
        if prefix in wordDict and word_break_memo(suffix, wordDict, memo):
            memo[word] = True
            return True

    memo[word] = False
    return False

print(word_break_memo("leetcode",["leet","code"]))
#True
print(word_break_memo("applepenapple", ["apple","pen"]))
#True
print(word_break_memo("catsandog",["cats","dog","sand","and","cat"]))
#False
# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str:identificatore univoco per l'account.
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
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato."""



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.

For example:
Test 	Result

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))
[5, 4, 3, 2, 1]

head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head))
[2, 1]"""

class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, head = None):
        self.head = head

    def insertNode(self, value):
        node = Node(value)

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
    
    def printLL(self):
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next
            if current:
                print(" -> ", end= "")

    def reverse_list(self):
        current = self.head
        res = []
        while current:
            res.append(current.value)
            current = current.next
        while res:
            if len(res)> 1:
                print(res.pop(), " -> ", end= "")
            else:
                print(res.pop())

llist = LinkedList()
llist.insertNode(1)
llist.insertNode(2)
llist.insertNode(3)
llist.insertNode(4)
llist.reverse_list()




# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna 8il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro."""


# library = Library()

# library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
# library.add_book("B002", "1984", "George Orwell")
# library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# # Register members
# library.register_member("M001", "Alice")
# library.register_member("M002", "Bob")
# library.register_member("M003", "Charlie")

# # Borrow books
# library.borrow_book("M001", "B001")
# library.borrow_book("M002", "B002")

# print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
# print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

For example:
Test 	Result

print(anagram("anagram","nagaram"))
True"""

def anagram(word1, word2) -> bool:
    return sorted(list(word1)) == sorted(list(word2))

    
print(anagram("anagram","nagaram"))
