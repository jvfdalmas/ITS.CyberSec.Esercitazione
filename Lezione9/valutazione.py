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

class BinaryTree:
    
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def setNodeValue(self,value):
        self.val = value
    
    def getNodeValue(self):
        return self.val
    
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

def buildTree(values):
    if not values:
        return None
    nodes = [BinaryTree(val) if val is not None else None for val in values]
    for i, node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            node.left = nodes[left_index]
        if right_index < len(nodes):
            node.right = nodes[right_index]
    return nodes[0]

def isSymmetricHelper(left: BinaryTree, right: BinaryTree) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)

def symmetric(tree: list[int]) -> bool:
    binaryTree = buildTree(tree)
    if binaryTree is None:
        return True
    return isSymmetricHelper(binaryTree.left, binaryTree.right)

# Test
print(symmetric([1,2,2,3,4,4,3]))  # True


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

def valid_sudoku(board: list[list[str]]) -> bool:
    n = len(board)

    def valid_row(row: list[str]) -> bool:
        control = ["1","2","3","4","5","6","7","8","9"]
        for char in row:
            if char in control:
                control.remove(char)
            elif char == ".":
                continue
            else:
                return False
        return True
    
    # CONTROL ROW    
    for row in board:
        if valid_row(row):
            continue
        else:
            return False

    # CONTROL COLUMN
    for i in range(n):
        column: list = []
        for j in range(n):
            column.append(board[j][i])
        if valid_row(row):
            continue
        else:
            return False

    # CREATE SMALLER BOARDS
    table1 = board[0:3][0:3]
    table2 = board[3:6][0:3]
    table3 = board[6:9][0:3]

    table4 = board[0:3][3:6]
    table5 = board[3:6][3:6]
    table6 = board[6:9][3:6]

    table7 = board[0:3][6:9]
    table8 = board[3:6][6:9]
    table9 = board[6:9][6:9]


    def smaller_board(board):
        n_row = len(board)
        n_column = len(board[0])

        row_chunk_n = 3
        column_chunk_n = 3

        sub_tables_1d = []

        for i in range(0,n_column, column_chunk_n):
            for j in range(0, n_row, row_chunk_n):
                smaller_table = [row[i:column_chunk_n] for row in board[j:column_chunk_n]]





board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print("is valid sodoku board?", valid_sudoku(board)) # True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] 
print("is valid sodoku board?", valid_sudoku(board)) # FALSE


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

def word_break(s: str, wordDict: list[str]) -> bool:
    # Create a set for faster lookup
    word_set = set(wordDict)
    # Create a boolean array to store whether s[:i] can be segmented
    dp = [False] * (len(s) + 1)
    dp[0] = True  # An empty string can always be segmented

    for i in range(1, len(s) + 1):
        for j in range(i):
            # Check if s[:j] can be segmented and if s[j:i] is in wordDict
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to continue checking further if already found

    return dp[len(s)]

print(word_break("leetcode",["leet","code"])) #True
print(word_break("applepenapple", ["apple","pen"])) #True
print(word_break("catsandog",["cats","dog","sand","and","cat"])) #False
print(word_break("catsanddog",["dog","sand","cat"])) #True


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

class Account:

    def __init__(self, account_id: str, balance: float = 0) -> None:
        self.account_id: str = account_id
        self.balance: float = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount
    
    def get_balance(self) -> float:
        return self.balance
    

class Bank:

    def __init__(self) -> None:
        self.accounts: dict[str, Account] = {}

    def create_account(self, account_id):
        if self.accounts.get(account_id) is None:
            account = Account(account_id)
            self.accounts[account_id] = account
            return account
        else:
            print("Account with this ID already exists")

    def deposit(self, account_id, amount):
        self.accounts[account_id].deposit(amount)

    def get_balance(self, account_id):
        if self.accounts.get(account_id) is not None:
            return self.accounts[account_id].get_balance()
        else:
            print("Account not found")
    
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456",200)
print(bank.get_balance("456"))

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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    current = head
    risult = []
    risult.append(current.val)
    while current.next is not None:
        current = current.next
        risult.append(current.val)
    
    risult.reverse()
    return risult

head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head)) # expected: [5, 4, 3, 2, 1]

head = ListNode(val=1, next=ListNode(val=2))
print(reverse_list(head)) # expected: [2, 1]

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

class Book:

    def __init__(self, book_id: str, title: str, author: str) -> None:
        self.book_id:str = book_id
        self.title: str = title
        self.author: str = author
        self.is_borrowed: bool = False

    def borrow(self) -> bool:
        if self.is_borrowed == False:
            self.is_borrowed = True

    def return_book(self) -> bool:
        if self.is_borrowed == True:
            self.is_borrowed = False


class Member:
        
        def __init__(self, member_id: str, name: str) -> None:
            self.member_id: str = member_id
            self. name: str = name
            self.borrowed_books: list[Book] = []

        def borrow(self, book: Book) -> None:
            self.borrowed_books.append(book)

        def return_book(self, book: Book) -> None:
            self.borrowed_books.remove(book)


class Library:

    def __init__(self) -> None:
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {} 
    
    def add_book(self, book_id: str, title: str, author: str) -> None:
        book = Book(book_id, title, author)
        self.books[book_id] = book
        return book

    def register_member(self, member_id:str, name: str) -> None:
        member = Member(member_id, name)
        self.members[member_id] = member
        return member
    
    def borrow_book(self, member_id: str, book_id: str) -> None:
        if self.members.get(member_id) is not None:
            if self.books.get(book_id) is not None:
                if self.books[book_id].is_borrowed == False:
                    self.books[book_id].borrow()
                    self.members[member_id].borrow(self.books[book_id])
                else:
                    raise ValueError("Book is already borrowed")
            else:
                raise ValueError("Book not found")
        else:
            raise ValueError("Member not found")

    def return_book(self, member_id: str, book_id: str) -> None:
        if self.books[book_id] in self.members[member_id].borrowed_books:
            self.books[book_id].return_book()
            self.members[member_id].return_book(self.books[book_id])
        else:
            raise ValueError("Book not borrowed by this member")

    def get_borrowed_books(self, member_id) -> list[Book]:
        return [book.title for book in self.members[member_id].borrowed_books]

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.

For example:
Test 	Result

print(anagram("anagram","nagaram"))
True"""

def anagram(s: str, t: str) -> bool:
    if sorted(list(s.lower())) == sorted(list(t.lower())):
        return True
    else:
        return False
    

