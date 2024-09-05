# Safe Square Root

"""1. Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). Handle ValueError if the input is negative by returning an informative message."""

print("1. Safe Square Root - Soluzione: \n")

    
    
# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Password Validation

"""2. Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords."""

print("2. Password Validation - Soluzione: \n")


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Context Managers for File Handling

"""3. Context Managers for File Handling: Use the with statement and context managers to open and close a file. Handle potential IOError within the with block for clean resource management."""

print("3. Context Managers for File Handling - Soluzione: \n")




# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Database of dates

"""4. Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. Note that a date is an object for your database; it must be instantiated from a string"""

print("4. Database of dates - Soluzione: \n")



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


#  An interactive calculator

"""5. An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
        If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
        Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError.
        If the second input is not '+' or '-', again raise a FormulaError.
        If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, until the user enters quit."""

print("5. An interactive calculator - Soluzione: \n")


# import unittest

# class TestCalculator(unittest.TestCase):
#     def test_addition(self):
#         self.assertEqual(calculate("1 + 1"), 2)
#         self.assertEqual(calculate("0 + 0"), 0)
#         self.assertEqual(calculate("-1 + -1"), -2)
#         self.assertEqual(calculate("3.5 + 2.5"), 6.0)

#     def test_subtraction(self):
#         self.assertEqual(calculate("5 - 3"), 2)
#         self.assertEqual(calculate("0 - 0"), 0)
#         self.assertEqual(calculate("-1 - -1"), 0)
#         self.assertEqual(calculate("3.5 - 1.5"), 2.0)

#     def test_invalid_input_length(self):
#         with self.assertRaises(FormulaError):
#             calculate("1 +")
#         with self.assertRaises(FormulaError):
#             calculate("1 1 + 1")
#         with self.assertRaises(FormulaError):
#             calculate("1")

#     def test_invalid_numbers(self):
#         with self.assertRaises(FormulaError):
#             calculate("a + 1")
#         with self.assertRaises(FormulaError):
#             calculate("1 + b")
#         with self.assertRaises(FormulaError):
#             calculate("a + b")

#     def test_invalid_operator(self):
#         with self.assertRaises(FormulaError):
#             calculate("1 * 1")
#         with self.assertRaises(FormulaError):
#             calculate("1 / 1")
#         with self.assertRaises(FormulaError):
#             calculate("1 ^ 1")

# if __name__ == "__main__":
#     unittest.main()


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



# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 


# Custom Exception for Data Structure Integrity

"""7. Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.  Define the custom data structure linked list use classes with methods to append, remove and access a given element, and write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). Raise this exception if the data structure's integrity is compromised (e.g., empty list access, index error)."""

print("7. Custom Exception for Data Structure Integrity - Soluzione: \n")


# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(3)
#     ll.append(2)

#     ll.print_list()  #  1 -> 3 -> 2

#     ll.remove(3)
#     ll.print_list()  # 1 -> 2

#     print(ll.access(1))  #  2

#     print(ll.is_ordered())  # True

#     ll.reverse()
#     ll.print_list()  # 2 -> 1

#     print(ll.is_ordered())  # False

#     ll.remove(3)  # Element 3 not found in the list.
#     print(ll.access(3))  # Index 3 is out of bounds.
#     ll2 = LinkedList()
#     ll2.print_list()  # (Empty list)
#     print(ll2.is_ordered())  # Cannot check order of an empty list.
#     ll2.reverse()  # Cannot reverse an empty list.
#     ll2.remove(1)  # Cannot remove from an empty list.
