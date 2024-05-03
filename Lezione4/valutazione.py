"""1. Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento. Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano."""

def blackjack_hand_total(cards: list[int]) -> int:
    count_card_ace: int = cards.count(1) + cards.count(11)
    summ_no_ace: int = sum(card for card in cards if card not in [1, 11])
    possible_sums: list = [summ_no_ace + count_card_ace + 10 * i for i in range(count_card_ace + 1)]
    valid_sums: list = [s for s in possible_sums if s <= 21]
    return max(valid_sums) if valid_sums else False

print(blackjack_hand_total([2, 3, 5])) # 10
print(blackjack_hand_total([11, 5, 5])) # 21
print(blackjack_hand_total([1, 10, 11])) # 12
print(blackjack_hand_total([11, 11, 11])) # 13

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""2. Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

Esempio:
construct_rectangle(4)
L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.

print(construct_rectangle(4)) -> [2, 2]"""

def construct_rectangle(area: float) -> list[float]:
    larghezza_w: float = 1
    lunghezza_l: float = area

    for fattore in range(2, int(area**0.5) + 1):
        if area % fattore == 0:
            if fattore <= area // fattore and area // fattore - fattore < lunghezza_l - larghezza_w:
                lunghezza_l = area // fattore
                larghezza_w = fattore

    return [int(lunghezza_l), int(larghezza_w)]

print(construct_rectangle(122122)) # [286, 427]
print(construct_rectangle(4)) # [2,2]

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""3. Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words e restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente (ignorando la distinzione tra maiuscole e minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

For example:
Test 	Result
stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
print(word_frequency(text, stopwords))
{'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}"""

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    word_count: dict = {}
    bad_chars = [';', ':', '!', "*", " ", ",", ".", "?"]

    for word in bad_chars:
        text = text.replace(word, ' ')
    
    word_list_no_alphanum: list = text.split()

    for word in word_list_no_alphanum:
        word = word.lower()
        if word not in stopwords:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
    
    return word_count

def word_frequency(text, stopwords):
    words = ''.join(char.lower() if char.isalnum() else ' ' for char in text).split()
    words = [word for word in words if word not in stopwords]
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text = "The quick brown fox jumps over the lazy dog. The dog is very lazy."
print(word_frequency(text, stopwords)) # {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 2, 'dog': 2, 'very': 1}"""

stopwords = ['the', 'and', 'is', 'in', 'on', 'of']
text3 = "I am I because I think I am. If I am not I, who am I?"
print(word_frequency(text3, stopwords)) # {'i': 7, 'am': 4, 'because': 1, 'think': 1, 'if': 1, 'not': 1, 'who': 1}

stopwords = ['be']
text4 = "To be, or not to be, that is the question."
print(word_frequency(text4, stopwords)) # {'to': 2, 'or': 1, 'not': 1, 'that': 1, 'is': 1, 'the': 1, 'question': 1}

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""4. Hai il compito di indagare su un caso di numeri mancanti! Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, dove n è la lunghezza dell'elenco. Sembra però che ci sia un problema: mancano alcuni numeri!
La tua missione è scrivere una funzione che prenda come input questo elenco di numeri (nums) potenzialmente incompleti. Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.
La funzione restituisce una nuova lista contenente tutti i numeri mancanti da 1 a n che non sono presenti nella lista originale. 

For example:
Test 	Result
print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

[5, 6]"""

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    missing_num: list = []
    for number in range(1, len(nums)+1):
        if number in nums:
            continue
        if number not in nums:
            missing_num.append(number)
    return missing_num

print(find_disappeared_numbers([4,3,2,7,8,2,3,1])) #[5, 6]

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""5. Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i tuoi sospettati. La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!
Qual è il problema?
Non puoi semplicemente confrontare le stringhe lettera per lettera. Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t). Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).
Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e t (la folla) come input. Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. Altrimenti restituisce False. Dimostra le tue abilità da detective e svela la verità nascosta!

For example:
Test 	Result
print(is_subsequence("abc", "ahbgdc"))
True
print(is_subsequence("axc", "ahbgdc"))
False"""

def is_subsequence(s: str, t: str) -> bool:
    s_lista: list = list(s)
    t_lista: list = list(t)
    support_list: list = []
    for letter in t_lista:
        if letter in s_lista:
            support_list.append(letter)
    if support_list == s_lista:
        return True
    else:
        return False

print(is_subsequence("abc", "cab")) #False


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""6. Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. Restituisce l'elenco riorganizzato.

For example:
Test 	Result
print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
[6, 8, 4, 3, 1, 7]"""

def even_odd_pattern(nums: list[int]) -> list[int]: 
    lista_pari: list = []
    lista_dispari: list = []

    for numero in nums:
        if numero % 2 == 0:
            lista_pari.append(numero)
        else:    
            lista_dispari.append(numero)

    mixed_list: list = lista_pari + lista_dispari
    return mixed_list

print(even_odd_pattern([3, 6, 1, 8, 4, 7])) #[6, 8, 4, 3, 1, 7]

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""7. Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

For example:
Test 	Result

print(prime_factors(4))
[2, 2]"""

def prime_factors(n: int) -> list[int]:
    fattori: list = []
    divisore: int = 2
    while divisore <= n:
        if n % divisore == 0:
            fattori.append(divisore)
            n: int = n // divisore
        else:
            divisore += 1
    return fattori

print(prime_factors(33))
print(prime_factors(99999999999999999999)) # [3, 3, 11, 41, 101, 271, 3541, 9091, 27961]


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""8. Immagina di avere uno scrigno pieno di gioielli (rappresentati da una lista di numeri interi). Questi gioielli hanno vari valori, alcuni più preziosi di altri. Il tuo compito è trovare il terzo gioiello distinto più prezioso nello scrigno.
Qual è la svolta?
Nello scrigno possono esserci gioielli duplicati (numeri con lo stesso valore). A noi però interessano solo valori distinti, ovvero gioielli con valori unici.
Scrivi una funzione che prenda come input questo array di valori di gioielli (numeri). Se nello scrigno sono presenti almeno tre valori distinti, la funzione dovrebbe restituire il valore del terzo gioiello distinto di maggior valore.
Ma c'è un problema!
Se non ci sono tre valori distinti (ad esempio, solo due valori univoci o tutti i valori sono uguali), la funzione dovrebbe restituire il valore del gioiello più prezioso nello scrigno.
For example:
Test 	Result
print(third_max([3, 2, 1])) #1
print(third_max([1, 2])) #2
print(third_max([2, 2, 3, 1])) #1"""

def third_max(nums: list[int]) -> int:
    number_count = {}

    for numero in nums:
        if numero not in number_count.keys():
            number_count[numero] = 1
        else:
            number_count[numero] += 1
    
    for numero in number_count.keys():
        while number_count[numero] != 1:
            number_count[numero] -= 1
            nums.remove(numero)
    
    nums.sort()


    if len(nums) >= 3:
        return nums[-3]
    else:
        return max(nums)

print(third_max([3, 2, 1])) #1
print(third_max([1, 2])) #2
print(third_max([2, 2, 3, 1])) #1
print(third_max([2, 2, 3, 2, 2])) #3

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Bonus 1. Immaginiamo di avere un tipo speciale di sistema numerico in cui gli unici elementi costitutivi sono i numeri 2, 3 e 5. Chiamiamo questi elementi costitutivi "fattori primi" perché non possono essere ulteriormente scomposti. Un "numero brutto" in questo sistema è un numero costruito utilizzando solo questi fattori primi (2, 3 o 5). Ad esempio, 6 (che può essere costruito come 2 x 3) è un numero brutto, ma 7 (che ha un fattore primo pari a 7) non lo è.

For example:
print(ugly_number(6))
True
print(ugly_number(1))
True
print(ugly_number(14))
False"""



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Bonus 2.Immagina di avere una raccolta di note musicali rappresentate da una serie di numeri interi. Queste note possono avere altezze (valori) diversi. Una sequenza armoniosa è come una melodia piacevole in cui la differenza di altezza tra la nota massimale e quella minimale è uguale a 1. Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, perché la differenza fra 3 e 2 è 1.
Trovare l'armonia perfetta:
Il tuo compito è scrivere una funzione che prenda come input questa serie di note musicali (numeri). La funzione dovrebbe trovare la sequenza armoniosa più lunga che puoi creare da queste note. Ricorda, una sottosequenza è una selezione di note dalla lista originale che mantiene l'ordine degli elementi.
Colpire le note giuste:
Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza)."""

def find_lhs(nums: list[int]) -> int:
    num_counts = {}
    max_length = 0

    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    for num in num_counts:
        if num + 1 in num_counts:
            max_length = max(max_length, num_counts[num] + num_counts[num + 1])

    return num_counts, max_length

print(find_lhs([1, 3, 2, 2, 5, 2, 3, 7])) # 5
print("\n") 
print(find_lhs([1,1,1,1])) #0
print("\n") 
print(find_lhs([1,1,2,2,3,3,4,4,5,5]))

"""Bonus 3. Date due stringhe note e magazine, restituisci true se note può essere costruita utilizzando le lettere di magazine e false in caso contrario. Ogni lettera nella magazine può essere utilizzata solo una volta in note.

For example:

print(ransom("a","b"))
False

print(ransom("aa", "ab"))
False

print(ransom("aa","aab"))
True"""

def ransom(note: str, magazine: str) -> bool:
    note: list = [letter for letter in note]
    magazine: list = [letter for letter in magazine]

    if len(note) > len(magazine):
        return False

    for letter in magazine:
        if letter in note:
            note.remove(letter)
            
    if note:
        return False
    else:
        return True


print(ransom("a","b")) #False

print(ransom("aa", "ab")) #False

print(ransom("aa","aab")) #True

"""Bonus 4. Dato un numero intero, restituisce una stringa che ne rappresenta la rappresentazione esadecimale. Per gli interi negativi viene utilizzato il metodo del complemento a due.

Tutte le lettere nella stringa di risposta dovrebbero essere caratteri minuscoli e non dovrebbero esserci zeri iniziali nella risposta tranne lo zero stesso.

Nota: non è consentito utilizzare alcun metodo di libreria integrato per risolvere direttamente questo problema.

For example:
print(to_hex(26))
1a

print(to_hex(-1))
ffffffff"""

def to_hex(num: int) -> str:
    decimal_to_hex = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
    }
    
    remainder_list = []

    if num == 0:
        return 0
    
    elif num >= 0:
        while num > 0:
            remainder = num % 16
            remainder_list.append(remainder)
            num = num // 16
        for index, item in enumerate(remainder_list):
            if item in decimal_to_hex:
                remainder_list[index] = decimal_to_hex[item]
        return "".join(remainder_list)
    
    else:
        print("banana")
        


print(to_hex(26))
print(to_hex(0))
print(to_hex(-1))
