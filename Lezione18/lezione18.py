# Safe Square Root

"""1. Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message."""

print("1. Safe Square Root - Soluzione: \n")

from math import sqrt

def safe_sqrt(number: int) -> int:
    try:
        risult = sqrt(number)
        return risult
    except:
        if number < 0:
            print(f"ERROR! number should be positive. {number = }")

print(safe_sqrt(-49))
    
    
# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Password Validation

"""2. Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords."""

print("2. Password Validation - Soluzione: \n")


def validate_password(password: str) -> str:
    upper_char: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    counter_upper_char: int = 0
    special_char: list[str] = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    counter_special_char: int = 0
    try:

        if len(password) >= 20:
            for char in password:
                if char in upper_char:
                    counter_upper_char += 1
        else:
            raise ValueError("ERRO! Minimum length of 20 characters!")
        
        if counter_upper_char >= 3:
            for char in password:
                if char in special_char:
                    counter_special_char += 1
        else:
            raise TypeError("ERRO! At least three uppercase characters!")  
          
        if counter_special_char >= 4:
            print("#alid password!!")
        else:
            raise NameError("ERRO! At least four special characters!")
        
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except NameError as ne:
        print(ne)

validate_password("da#aaf#ada#aDdaadaAddada#adaDdaaa")


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Context Managers for File Handling

"""3. Context Managers for File Handling: Use the with statement and context managers to open and close a file. Handle potential IOError within the with block for clean resource management."""

print("3. Context Managers for File Handling - Soluzione: \n")

try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except IOError as e:
    print(f"An error occurred while handling the file: {e}")



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Database of dates

"""4. Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; it must be instantiated from a string"""

print("4. Database of dates - Soluzione: \n")


from datetime import datetime

class DateDatabase:

    def __init__(self):
        self.dates = {}

    def add_date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, '%d.%m.%Y')
            if date_str in self.dates:
                print(f"Date {date_str} already exists in the database.")
            else:
                self.dates[date_str] = date_obj
                print(f"Date {date_str} added successfully.")
        except ValueError as e:
            print(f"Error: {e}. Date format must be gg.mm.aaaa")

    def delete_date(self, date_str):
        if date_str in self.dates:
            del self.dates[date_str]
            print(f"Date {date_str} deleted successfully.")
        else:
            print(f"Date {date_str} not found in the database.")

    def modify_date(self, old_date_str, new_date_str):
        try:
            new_date_obj = datetime.strptime(new_date_str, '%d.%m.%Y')
            if old_date_str in self.dates:
                self.dates[new_date_str] = new_date_obj
                del self.dates[old_date_str]
                print(f"Date {old_date_str} modified to {new_date_str} successfully.")
            else:
                print(f"Date {old_date_str} not found in the database.")
        except ValueError as e:
            print(f"Error: {e}. New date format must be gg.mm.aaaa")

    def query_date(self, date_str):
        if date_str in self.dates:
            return date_str
        else:
            print(f"Date {date_str} not found in the database.")
            return None

db = DateDatabase()
db.add_date('18.06.2024')
db.add_date('19.06.2024')
print(db.query_date('18.06.2024'))  #  '18.06.2024'
db.modify_date('18.06.2024', '20.06.2024')
db.delete_date('19.06.2024')
print(db.query_date('19.06.2024'))  #  not found message


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


#  An interactive calculator

"""5. An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
        If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
        Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
        If the second input is not '+' or '-', again raise a FormulaError.
        If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit."""

print("5. An interactive calculator - Soluzione: \n")

class FormulaError(Exception):
    """Exception raised for errors in the input formula."""
    pass

def calculate(formula):
    parts = formula.split()

    if len(parts) != 3:
        raise FormulaError("Input does not consist of three elements")

    num1_str, operator, num2_str = parts

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        raise FormulaError("The first and third elements must be numbers")

    if operator not in ('+', '-'):
        raise FormulaError("The operator must be '+' or '-'")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2

def interactive_calculator():
    while True:
        formula = input("Enter a formula (or 'quit' to exit): ")
        if formula.lower() == 'quit':
            break
        try:
            result = calculate(formula)
            print(f"Result: {result}")
        except FormulaError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    interactive_calculator()

import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("1 + 1"), 2)
        self.assertEqual(calculate("0 + 0"), 0)
        self.assertEqual(calculate("-1 + -1"), -2)
        self.assertEqual(calculate("3.5 + 2.5"), 6.0)

    def test_subtraction(self):
        self.assertEqual(calculate("5 - 3"), 2)
        self.assertEqual(calculate("0 - 0"), 0)
        self.assertEqual(calculate("-1 - -1"), 0)
        self.assertEqual(calculate("3.5 - 1.5"), 2.0)

    def test_invalid_input_length(self):
        with self.assertRaises(FormulaError):
            calculate("1 +")
        with self.assertRaises(FormulaError):
            calculate("1 1 + 1")
        with self.assertRaises(FormulaError):
            calculate("1")

    def test_invalid_numbers(self):
        with self.assertRaises(FormulaError):
            calculate("a + 1")
        with self.assertRaises(FormulaError):
            calculate("1 + b")
        with self.assertRaises(FormulaError):
            calculate("a + b")

    def test_invalid_operator(self):
        with self.assertRaises(FormulaError):
            calculate("1 * 1")
        with self.assertRaises(FormulaError):
            calculate("1 / 1")
        with self.assertRaises(FormulaError):
            calculate("1 ^ 1")

if __name__ == "__main__":
    unittest.main()


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

# Personalized math library

"""6. Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error handling. The library must include functions for the following operations:
        Create a fraction from the numerator and denominator.
        Collect the numerator and denominator of a fraction.
        Simplify a fraction.
        Add, subtract, multiply and divide fractions.
        Check whether one fraction is equivalent to another.
        All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported operations, or division by zero. The library must raise custom exceptions to indicate specific errors to the user."""

print("6. Personalized math library - Soluzione: \n")

class FractionError(Exception):
    """Base class for other exceptions"""
    pass

class ZeroDenominatorError(FractionError):
    """Raised when the denominator is zero"""
    pass

class InvalidOperationError(FractionError):
    """Raised when an invalid operation is attempted"""
    pass


from math import gcd

class Fraction:

    def __init__(self, numerator, denominator):
        try:
            if denominator == 0:
                raise ZeroDenominatorError("Denominator cannot be zero.")
            self.numerator = numerator
            self.denominator = denominator
            self.simplify()
        except ZeroDenominatorError as e:
            print(e)

    def simplify(self):
        try:
            common_divisor = gcd(self.numerator, self.denominator)
            self.numerator //= common_divisor
            self.denominator //= common_divisor
        except Exception as e:
            print(f"An error occurred during simplification: {e}")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def __add__(self, other):
        try:
            if not isinstance(other, Fraction):
                raise InvalidOperationError("Can only add another Fraction instance.")
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        except InvalidOperationError as e:
            print(e)

    def __sub__(self, other):
        try:
            if not isinstance(other, Fraction):
                raise InvalidOperationError("Can only subtract another Fraction instance.")
            numerator = self.numerator * other.denominator - other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        except InvalidOperationError as e:
            print(e)

    def __mul__(self, other):
        try:
            if not isinstance(other, Fraction):
                raise InvalidOperationError("Can only multiply by another Fraction instance.")
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        except InvalidOperationError as e:
            print(e)

    def __truediv__(self, other):
        try:
            if not isinstance(other, Fraction):
                raise InvalidOperationError("Can only divide by another Fraction instance.")
            if other.numerator == 0:
                raise ZeroDenominatorError("Cannot divide by a fraction with zero numerator.")
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Fraction(numerator, denominator)
        except (InvalidOperationError, ZeroDenominatorError) as e:
            print(e)

    def __eq__(self, other):
        try:
            if not isinstance(other, Fraction):
                raise InvalidOperationError("Can only compare with another Fraction instance.")
            return self.numerator * other.denominator == self.denominator * other.numerator
        except InvalidOperationError as e:
            print(e)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Custom Exception for Data Structure Integrity

"""7. Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.  Define the custom data structure linked list use classes with methods to append, remove and access a given element, and write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error)."""

print("7. Custom Exception for Data Structure Integrity - Soluzione: \n")

class DataStructureIntegrityError(Exception):
    """Exception raised for errors in the data structure integrity."""
    pass

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        try:
            if not self.head:
                raise DataStructureIntegrityError("Cannot remove from an empty list.")
            
            if self.head.data == data:
                self.head = self.head.next
                return

            current = self.head
            while current.next and current.next.data != data:
                current = current.next

            if not current.next:
                raise DataStructureIntegrityError(f"Element {data} not found in the list.")
            
            current.next = current.next.next
        except DataStructureIntegrityError as e:
            print(e)

    def access(self, index):
        try:
            if not self.head:
                raise DataStructureIntegrityError("Cannot access an element from an empty list.")
            
            current = self.head
            count = 0
            while current:
                if count == index:
                    return current.data
                current = current.next
                count += 1
            
            raise DataStructureIntegrityError(f"Index {index} is out of bounds.")
        except DataStructureIntegrityError as e:
            print(e)
            return None

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def reverse(self):
        try:
            if not self.head:
                raise DataStructureIntegrityError("Cannot reverse an empty list.")
            
            prev = None
            current = self.head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self.head = prev
        except DataStructureIntegrityError as e:
            print(e)

    def is_ordered(self):
        try:
            if not self.head:
                raise DataStructureIntegrityError("Cannot check order of an empty list.")
            
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    return False
                current = current.next
            return True
        except DataStructureIntegrityError as e:
            print(e)
            return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(2)

    ll.print_list()  #  1 -> 3 -> 2

    ll.remove(3)
    ll.print_list()  # 1 -> 2

    print(ll.access(1))  #  2

    print(ll.is_ordered())  # True

    ll.reverse()
    ll.print_list()  # 2 -> 1

    print(ll.is_ordered())  # False

    ll.remove(3)  # Element 3 not found in the list.
    print(ll.access(3))  # Index 3 is out of bounds.
    ll2 = LinkedList()
    ll2.print_list()  # (Empty list)
    print(ll2.is_ordered())  # Cannot check order of an empty list.
    ll2.reverse()  # Cannot reverse an empty list.
    ll2.remove(1)  # Cannot remove from an empty list.
