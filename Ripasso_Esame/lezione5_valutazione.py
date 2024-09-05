"""1. Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
For example:
Test 	Result
print(remove_duplicates([1, 2, 3, 1, 2, 4]))
[1, 2, 3, 4]
print(remove_duplicates([4, 5, 'a', 4, 6]))
[4, 5, 'a', 6]"""

def remove_duplicates(array: list):
    res = []
    for item in array:
        if item not in res:
            res.append(item)
    return res

print(remove_duplicates([1, 2, 3, 1, 2, 4]))
#[1, 2, 3, 4]
print(remove_duplicates([4, 5, 'a', 4, 6]))
#[4, 5, 'a', 6]

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""2. Il codice dovrebbe stampare i numeri all'interno di una lista. TROVA L'ERRORE E CORREGGI IL CODICE"""


numbers: list[int] = [1, 2, 3, 4, 5]

for number in numbers:
    print(f"Number: {number}")


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""3. Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.

For example:
Test 	Result
print(check_combination(True, False, True))
Operazione permessa
print(check_combination(False, True, False))
Operazione negata"""

def check_combination (a: bool, b: bool, c:bool) -> str:
    if a == True or b == True and c == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"

print(check_combination(True, False, True))
#Operazione permessa
print(check_combination(False, True, False))
#Operazione negata
print(check_combination(False, True, True))
#Operazione permessa

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""4. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
For example:
Test 	Result
print(rounded_average([1, 1, 2, 2]))
2"""

def rounded_average(arr: list[int]) -> int:
    somma = round(sum(arr) / len(arr))
    return somma

print(rounded_average([1, 1, 2, 2]))
#2

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""5. Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
For example:
Test 	Result
countdown(5)
5
4
3
2
1
0
"""
def countdown(n: int) -> int:
    while n != -1:
        print(n)
        n -= 1

countdown(5)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""6. Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

For example:
Test 	Result
print(list_statistics([1, 2, 3, 4, 5])) 
(5, 1, 3.0)"""

def list_statistics(arr: list[int]):
    return (max(arr), min(arr), sum(arr) / len(arr))

print(list_statistics([1, 2, 3, 4, 5])) 
#(5, 1, 3.0)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""7.  Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

For example:
Test 	Result
print(check_parentheses("()()"))
True
print(check_parentheses("(()))("))
False"""

def check_parentheses(stringa: str) -> bool:
    control = []

    for item in stringa:
        if item == "(":
            control.append(item)
        else:
            if control:
                control.pop(-1)
            else:
                return False
    
    return len(control) == 0

print(check_parentheses("()()"))
print(check_parentheses("(()))("))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""8. Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

For example:
Test 	Result
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
2
print(count_isolated([1, 2, 3, 4, 5]))
5"""

def count_isolated(arr: list[int]) -> int:
    counter = 0

    if len(arr) == 0:
        return counter
    if len(arr) == 1:
        return counter + 1
    
    if arr[0] != arr[1]: #control first element
        counter += 1

    for i in range(1,len(arr)-1):
        if arr[i-1] != arr[i] and arr[1+i] != arr[i]:
            counter += 1
    
    if arr[-1] != arr[-2]: #control last element
        counter += 1
    
    return counter


print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
#2
print(count_isolated([1, 2, 3, 4, 5]))
#5


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9. Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.

For example:
Test 	Result
print(remove_elements({5, 6, 7}, [7, 8, 9]))
{5, 6}"""

def remove_elements(arr: set[int], remove: list[int]) -> set[int]:
    arr = arr - set(remove)
    return arr

print(remove_elements({5, 6, 7}, [7, 8, 9]))
#{5, 6}

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""10. Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

For example:
Test 	Result
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for key, value in dict2.items():
        if dict1.get(key):
            dict1[key] += value
        else:
            dict1[key] = value
    return dict1

print(merge_dictionaries({'x': 5}, {'x': -2, "y": 2}))
#{'x': 3, 'y': 2}