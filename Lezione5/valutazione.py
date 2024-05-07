"""1. Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
For example:
Test 	Result
print(remove_duplicates([1, 2, 3, 1, 2, 4]))
[1, 2, 3, 4]
print(remove_duplicates([4, 5, 'a', 4, 6]))
[4, 5, 'a', 6]"""

def remove_duplicates(insieme) -> list:
    risult: list = []

    for item in insieme:
        if item not in risult:
            risult.append(item)
        if item in risult:
            continue
    
    return risult

print(remove_duplicates([1, 2, 3, 1, 2, 4])) #[1, 2, 3, 4]

print(remove_duplicates([4, 5, 'a', 4, 6])) #[4, 5, 'a', 6]

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

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA is True:
        return "Operazione permessa"
    elif conditionA is False and conditionB is True and conditionC is True:
        return "Operazione permessa"
    else:
        return "Operazione negata"

print(check_combination(True, False, True)) #Operazione permessa
print(check_combination(False, True, False)) #Operazione negata


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""4. Scrivi una funzione che calcola la media di una lista di numeri e ritorna il valore arrotondato all'intero più vicino.
For example:
Test 	Result
print(rounded_average([1, 1, 2, 2]))
2"""

def rounded_average(numbers: list[int]) -> int:
    import math
    total_sum = sum(number for number in numbers)
    divisore = len(numbers)
    return int(math.ceil(total_sum / divisore))

print(rounded_average([1, 1, 2, 2])) #2
print(rounded_average([1, 2, 3, 4, 5])) #3

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
    while n >= 0:
        print(n)
        n = n -1

countdown(5)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""6. Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.

For example:
Test 	Result
print(list_statistics([1, 2, 3, 4, 5])) 
(5, 1, 3.0)"""

def list_statistics(numbers: list[int]) -> tuple:
    media: float = sum(number for number in numbers) / len(numbers)
    max_value: int = max(numbers)
    min_value: int = min(numbers)

    return (max_value, min_value, media)

print(list_statistics([1, 2, 3, 4, 5]))  #(5, 1, 3.0)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""7.  Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

For example:
Test 	Result
print(check_parentheses("()()"))
True
print(check_parentheses("(()))("))
False"""

def check_parentheses(expression: str) -> bool:
    
    control_open: int = 0
    control_closed: int = 0
    bad_chars = ['\'', '\"']

    for char in bad_chars:
        expression = expression.replace(char, ' ')    
    expression_list = list(expression)

    for element in expression_list:
        if element == ")":
            control_closed += 1
        if element == "(":
            control_open += 1

    if  control_open == control_closed:
        if expression_list[-1] == '(':
            return False
        else:
            return True
    else:
        return False


print(check_parentheses("()()")) #True
print(check_parentheses("(()))")) #False
print(check_parentheses("())(()")) #False



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""8. Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.

For example:
Test 	Result
print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
2
print(count_isolated([1, 2, 3, 4, 5]))
5"""

def count_isolated(insieme: list) -> int:
    counter: int = 0

    if len(insieme) == 0:
        return 0
    
    for i in range(len(insieme) - 1):
        if insieme[i] != insieme[i + 1]:
            if insieme[i] != insieme[i - 1]:
                counter += 1
    if insieme[-1] != insieme[-2]:
        counter += 1
    
    return counter

print(count_isolated([1, 2, 2, 3, 3, 3, 4])) #2
print(count_isolated([1, 2, 3, 4, 5])) #5

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9. Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.

For example:
Test 	Result
print(remove_elements({5, 6, 7}, [7, 8, 9]))
{5, 6}"""

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    risult: set = set()
    for element in original_set:
        if element not in elements_to_remove:
            risult.add(element)
    return risult


print(remove_elements({5, 6, 7}, [7, 8, 9])) #{5, 6}

"""10. Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

For example:
Test 	Result
print(merge_dictionaries({'x': 5}, {'x': -5}))
{'x': 0}"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:

    merged_dict: dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        if key not in merged_dict:
            merged_dict[key] = value

    return merged_dict
            
print(merge_dictionaries({'x': 5}, {'x': -5})) #{'x': 0}