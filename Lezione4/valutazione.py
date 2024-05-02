"""1. Nel gioco del blackjack, il valore di una mano è determinato dalla somma dei valori delle carte. Ogni carta ha un valore compreso tra 2 e 11 compresi. Tuttavia, se una mano contiene un asso, il valore dell'asso può essere 1 o 11, a seconda di quale sia più favorevole al giocatore in quel momento. Dato un elenco di valori delle carte che rappresentano una mano di blackjack, scrivi una funzione per determinare il valore totale della mano."""

def blackjack_hand_total(cards: list[int]) -> int:
    count_card_ace: int = cards.count(1) + cards.count(11)
    summ_no_ace: int = 0
    hand: int = 0
    support_list: list = []

    for card in cards[:]:
        if  (card == 1) or (card == 11):
            cards.remove(card)
        else:
            summ_no_ace += card

    if count_card_ace == 0:
        hand = summ_no_ace
            
    elif count_card_ace == 1:
        one_ace_test1 = summ_no_ace + 1
        one_ace_test11 = summ_no_ace + 11
        if one_ace_test11 > 21:
            return one_ace_test1
        else:
            return one_ace_test11

    elif count_card_ace == 2:
        two_ace_test1 = summ_no_ace + 1 + 1
        two_ace_test2 = summ_no_ace + 11 + 1
        two_ace_test3 = summ_no_ace + 11 + 11
        if two_ace_test1 <= 21:
            support_list.append(two_ace_test1)
        elif two_ace_test2 <= 21:
                support_list.append(two_ace_test2)
        sorted_list = sorted(support_list)
        hand = sorted_list.pop()
            
    elif count_card_ace == 3:
        hand = 13
    return hand

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

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""7. Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

For example:
Test 	Result

print(prime_factors(4))
[2, 2]"""

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
print(third_max([3, 2, 1]))
1
print(third_max([1, 2]))
2
print(third_max([2, 2, 3, 1]))
1"""