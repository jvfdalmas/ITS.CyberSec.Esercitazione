""" Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included). The numbers should be stored in a list and returned as output. """

def divisible7_notmultiple5(numbers: list[int]) -> list[int]:
    risult: list = []
    for number in numbers:
        if number % 7 == 0 and number % 5 != 0:
            risult.append(number)

    return risult

test_list = [7, 10, 14, 20, 21, 25, 28, 30, 35, 40, 42, 49, 50, 55, 56, 60, 63, 70, 77, 80, 84, 90, 91, 95, 98, 100]

print(divisible7_notmultiple5(test_list))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

""" Write a function to calculate the factorial of a number given as input. The number should be returned as output. For example:
Input: 8
Output: 40320"""

def calculate_factorial(number: int) -> int:
    fattoriale: int = number
    while number > 1:
        fattoriale = fattoriale * (number -1)
        number -= 1
    
    return fattoriale

print(calculate_factorial(8))


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. The list is given as input to the function. All factorials should be returned as output. For example:
Input: [2, 5, 8, 10]
Output: [2, 120, 40320, 3628800]"""

lista = [2, 5, 8, 10]
risult = [calculate_factorial(number) for number in lista]
print(risult)


# alternative using existing function: 

def calculate_factorial_list(numbers: list[int]) -> int:
    risult = [calculate_factorial(number) for number in numbers]
    return risult

print(calculate_factorial_list(lista))


# alternative building a new function: 

def calculate_factorial_list(numbers: list[int]) -> int:
    risult = []
    for number in numbers:
        fattoriale: int = number
        while number > 1:
            fattoriale = fattoriale * (number -1)
            number -= 1
        risult.append(fattoriale)
    
    return risult

print(calculate_factorial_list(lista))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) pairs such that i is an integer between 1 and n (both included). The function should return the dictionary as output. For example:
Input: 8
Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

def generate_dict(number: int) -> dict:
    dict = {i: i*i for i in range(1,number+1)}
    return dict

print(generate_dict(8))
print(generate_dict(20))


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Write a function that accepts a string with a comma-separated sequence of words as input and prints the words as a comma-separated sequence after sorting them alphabetically. For example:
Input: without,hello,bag,world
Output: bag,hello,without,world"""

def sorting_with_comma(s: str) -> str:
    s:list = s.split(",")
    s.sort()
    s: str = ",".join(s)

    return s

print(sorting_with_comma("without,hello,bag,world")) # expected: "bag,hello,without,world"
# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising all sentence characters. For example:
Input: Practice makes perfect
Output: PRACTICE MAKES PERFECT"""

def capitalise(s: str) -> str:
    return s.upper()

print(capitalise("Practice makes perfect"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""    Write a function accepting an input string defined with whitespace-separated words and returning it after removing all duplicates and sorting each word alphanumerically. For example:
Input: hello world and practice makes perfect and hello world again
Output: again and hello makes perfect practice world"""

def sorting_no_duplicates(s: str) -> str:
    s: list = s.split()
    s: set = set(s)
    s: list = list(s)
    s.sort()
    s: str = " ".join(s)
    return s

print(sorting_no_duplicates("hello world and practice makes perfect and hello world again")) # expected: "again and hello makes perfect practice world"

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Write a function to check whether a string is a pangram or not. Pangrams are words or sentences containing every letter of the alphabet at least once.
Input: The quick brown fox jumps over the lazy dog
Output: True"""

def check_abc(s: str) -> bool:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s: str = s.replace(" ", "")
    s: list = list(s.lower())

    for _ in s:
        if _ in alphabet:
            alphabet.remove(_)

    if alphabet == []:
        return True
    else:
        return False

print(check_abc("The quick brown fox jumps over the lazy dog"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Write a function to check whether a number is "Perfect" or not. In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself). For example:
Input: 6
Output: True"""

def is_perfect(n: int) -> bool:
    divisors_sum: int = sum([divisior for divisior in range(1,n) if n % divisior == 0])

    if divisors_sum == n:
        return True
    else:
        return False

print(is_perfect(6))


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Using the code implemented in Exercise 8, write a function that, given a number n as input, computes all "Perfect" numbers between 1 and n. For example:
Input: 500
Output: [6, 28, 496]"""

def is_perfect_list(n_list: list[int]) -> list:
    risult: list = [n for n in n_list if is_perfect(n) == True]

    return risult

lista: list = range(1, 501)

print(is_perfect_list(lista))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""Write a function to sort the (name, age, height) input list of tuples by ascending order where name is string, age and height are numbers. The function should return a list of tuples of strings. The priority is that name > age > score. Namely, the sort criteria are:
Sort based on name;
Then, sort based on age;
Then, sort by score.

Input: [('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]
Output:  [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')] """

def sort(array: list[tuple[str, int, int]]) -> list[tuple[str, str, str]]:
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    result = [(name, str(age), str(height)) for name, age, height in array]
    
    return result

lista: list = [('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85)]
print(sort(lista)) # expected:  [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]