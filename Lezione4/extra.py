"""1. Create a funcion that takes a students name and their score in different subjects as input. The funcition calculates the average score and prints the sudents name, average, and a message indicating wheter the student passed the exame (average >= 60) or failed. Create a for loop to iterate over a list of students and scores, calling the function for each student."""

def promoted_or_not(student_name: str, **kwargs: dict) -> str:
    """ Funcion that takes a students name and their score as input, calculates the average score and prints the sudents name, average, and a message indicating wheter the student passed the exame (average >= 60) or failed."""
    summed_scores: int = sum(kwargs.values())
    count_subject: int = len(kwargs)
    average: float = summed_scores / count_subject
    if average >= 60:
        return f"Congratulattion, {student_name.title()}! Your average score is {average} and you passed the exam!"
    else:
        return f"You failed, {student_name.title()}! Your average score is {average} and you did not passed the exam!"

students_list = [
    {"Joao": {"Biology": 100, "History": 100, "Chemistry": 90, "Math": 70}},
    {"Michele": {"Biology": 40, "History": 45, "Chemistry": 50, "Math": 70}}
    ]

for student_data in students_list:
    student_name = list(student_data.keys())[0]  # Ottieni il nome dello studente
    subjects_scores = student_data[student_name]  # Ottieni i voti dello studente
    print(promoted_or_not(student_name, **subjects_scores))  # Passa i voti come argomenti

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")    

"""2. Guess the Number Game: Create a function that generates a random number within a range specified by the user. Prompt the user to guess the number within a specified maximum number of attempts. Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct. Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts."""

#import random
#random.seed(1)
#counter: int = 0

#number_message: str = input("I will create a random number within a range specified. Please write a number: ")
#generated_number: int = random.randint(1, int(number_message))

#while counter < 3:
#    guessed_number: str = input("Now try to to guess the number. What number did I create? You have 3 guesses: ")
#    if int(guessed_number) == generated_number:
#        print("You are correct!!!")
#        break
#    else:
#        counter += 1
#        if counter == 3:
#            print(f"You failed! The number I created was {generated_number}.")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""3. E-commerce Shopping Cart: Create a function that defines a product with a name, price, and quantity. Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart. The function should calculate the cart total and apply any discounts or taxes. Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total."""

def define_product(product_name: str, product_price: float, product_quantity: int) -> dict:
    """ Function that takes a product with a name, price, and quantity, and output as dictionary"""
    final_dict: dict = {product_name:{"price": product_price, "quantity":product_quantity}}
    return final_dict

monitor: dict = define_product("Monitor", 99.99, 12)
TV: dict = define_product("TV", 1_000.00, 1)
printer: dict = define_product("printer", 200.50, 3)

shopping_cart = []
discount_percent = 0

def add_product(*args: dict):
    """ Function that adds products in the shopping_cart"""
    for product in args:
        shopping_cart.append(product)
    return shopping_cart
    
def remove_product(*args: str):
    """ Function that removes products from the shopping_cart"""
    for product in args:
        if product in shopping_cart:
            shopping_cart.remove(product)
    return shopping_cart
    
def view_cart():
    """ Function that allows user to see the shopping_cart"""

def apply_discount(coupon: str) -> float:
    if discount_percent <= 0.30:
        if coupon == "BIRTHDAY10":
            discount_percent += 0.10
        elif coupon == "SALES15":
            discount_percent += 0.15
        else:
            return f"Your coupon is not valid!"
    else:
        return f"You have reached the maximum discount percentage"

#def apply_taxes():

""". Text Analysis: Create a function that reads a text file and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
    Implement error handling to handle missing files or other input issues."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""5. Inventory Management System: Create a function that defines an item with a code, name, quantity, and price.
     Create a database or dictionary to store the items in inventory.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops and conditional statements to manage the various inventory operations."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""6. Password Generator: Create a function that generates a random password with a specified length and desired character types (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""7. Roman Numeral Conversion: Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""8. ATM Machine Simulator: Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
     Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9. Caesar Cipher Encryption/Decryption Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
     Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""10. Anagram Checker: Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""11. Word Search Puzzle Solver: Create a function that solves a word search puzzle.
    Provide a 2D grid representing the puzzle and a list of words to find.
    Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
    Output the locations of the found words within the grid."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""12. Sieve of Eratosthenes Prime Number Generator: Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
    Initialize an array of all numbers up to the limit, marking each number as prime initially.
    Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
    The remaining unmarked numbers are the prime numbers within the limit.
    Return the list of prime numbers.
"""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""13. Fractal Tree Generator: Create a function that generates a fractal tree using recursion.
    Specify the starting trunk length and branching angle.
    Draw the trunk and then recursively call the function to draw two branches at the specified angle, each with a shorter length.
    Repeat the branching process until a desired level of detail is reached."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""14. Sudoku Solver: Create a function that solves a Sudoku puzzle using backtracking.
    Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank.
    Implement a backtracking algorithm to check for valid placements in empty cells, ensuring no row, column, or 3x3 subgrid contains duplicates.
    Solve the puzzle by filling in the remaining empty cells with valid numbers."""

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""15. Text Editor with Basic Functionality: Create a simple text editor that allows the user to open, edit, and save text files.
    Implement basic functionality such as inserting, deleting, and copying text.
    Provide undo/redo functionality to allow users to reverse actions.
    Save the edited text to a file when the user chooses to save."""
