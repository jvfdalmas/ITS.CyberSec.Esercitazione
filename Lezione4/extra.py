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