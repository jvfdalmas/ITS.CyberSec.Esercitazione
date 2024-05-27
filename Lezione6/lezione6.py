""" CLASSE """

class Person:

    def __init__(self, name: str, surname: str, birthday: str, birth_place: str, gender: str) -> None:
        ID: int = 1  # come ID non è sotto self, Python non riconosce come attributo della classe e non la stampa 
        self._name: str = name # attributo della classe     # per convenzione, sempre che c'è un "_" significa attributo privato
        self.surname: str = surname # attributo della classe
        self._birthday: str = birthday
        self._brith_place: str = birth_place
        self._gender: str = gender
        self._taxpayers_id: None = None
        self.compute_taxpayers_id()

    def get_name(self): # "get" serve per l'utente esterno aver accesso alla informazione privata
        """This function gets the attribute name.
        input: None
        return: self._name: str"""

        return self._name
    
    def get_taxpayers_id(self):
        """This function gets the attribute taxpayers id.
        input: None
        return: self._taxpayers_id: str"""

        return self._taxpayers_id
    
    def set_name(self, name: str):  # "set" serve per l'utente cambiare l'attributo 
        """This function sets the attribute name.
        input: name: str, the parameter contains the user's name
        return: None"""

        raise Exception("You cannot modify the name")
    
    def set_taxpayers_id(self, taxpayers_id: str):
        """This function sets the attribute taxpayers id.
        input: taxpayers_id: str, the parameter contains the user's taxpayer's id
        return: None"""
        
        raise Exception("You cannot modify taxpayer\'s id")

    def compute_taxpayers_id(self) -> str:
        from compute_taxpayers_id import compute_taxpayers_id as compute_tax_id
        self._taxpayers_id = compute_tax_id(nome = self._name, cognome = self.surname, data_di_nascita = self._birthday, genere = self._gender, comune_di_nascita = self._brith_place)
    
    def check_taxpayers_id(self, taxpayers_id: str) -> bool:
        """This function checks the taxpayer's id.
        input: taxpayers_id: str, the parameter contains the user's taxpayer's id
        return: boolean"""
        
        pass   
     
    def __str__(self) -> str:
        """This function prints the attributes in the form of a str.
        input: None
        return: str with the attributes """

        return f"name: {self._name}, surname: {self.surname}, taxpayers id: {self._taxpayers_id}"
    
    def __hash__(self) -> int:
        pass

    def __eq__(self, value: object) -> bool:

        return value.hash() == self.hash()
    
persona_1: Person = Person(name="Flavio", surname="Giorgi", birthday="24/12/1994", birth_place="Roma", gender="Male")
persona_2: Person = Person(name="Joana", surname="Figueiredo", birthday="04/01/1980", birth_place="Campinas", gender="Female")
persona_3: Person = Person(name="Michelle", surname="Fontenova", birthday="06/11/1960", birth_place="Milano", gender="Male")

print(persona_1._name, persona_1.surname)
print(persona_2._name, persona_2.surname)

print(persona_1.get_name())
print(str(persona_1))
print(str(persona_2))
print(str(persona_3))

queue: list = [persona_1, persona_2, persona_3]
for person in queue:
    persons_name = person.get_name()
    persons_tax_id = person.get_taxpayers_id()
    print(f"The taxpayer\'s id of {persons_name} is {persons_tax_id}")

#persona_1.set_taxpayers_id("FFFF")
print(persona_1.get_taxpayers_id())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 
"""Lezione 09 / 05 /2024"""

class Student:
    def __init__(self, name: str, study_program: str, age: int, gender: str):
        self.name: str = name
        self.study_program: str = study_program
        self.age: int = age
        self.gender: str = gender

    def print_info(self):
        return f"The student {self.name.title()} is studying {self.study_program.title()}. He is a {self.gender} and he is {self.age} years old."

student1: Student = Student(name = "Vitorio", study_program="Cybersecurty", age=30, gender="Male")
student2: Student = Student(name = "Simone", study_program="Cybersecurty", age=20, gender="Male")
student3: Student = Student(name = "Angelo", study_program="Cybersecurty", age=19, gender="Male")

print(student1.print_info())
print(student2.print_info())
print(student3.print_info())

class Food:

    def __init__(self, name: str, price: float, description: str) -> None:
        self.name = name
        self.price = price
        self.description = description

    def get_name(self) -> str:

        return self.name

    def get_price(self) -> float:

        return self.price
    
    def get_description(self) -> str:

        return self.description
    
    def print_food(self) -> str:

        return f"food name: {self.name}, food price: {self.price}, food description: {self.description}"

food1: Food = Food(name="pizza", price=3.5, description="round disk made of flour and water with toppings baked in the oven")
food2: Food = Food(name="bread", price=1.0, description="it is just bread...")
food3: Food = Food(name="hot dog", price=2.5, description="it is like hamburguer but with sausage")

print(food1.print_food())
print(food2.print_food())
print(food3.print_food())

print("\n")

class Menu:

    def __init__(self, food_list: list):
        self.menu = food_list

    def show_menu(self):

        for food in self.menu:
            print(food.print_food())

    def add_Food(self, new_food):

        if new_food not in self.menu:
            self.menu.append(new_food)
            print(f"{new_food.get_name()} was added to the menu!")
        else:
            print(f"{new_food.get_name()}  is already in the menu")
    
    def remove_Food(self, existing_food):
        if existing_food in self.menu:
            self.menu.remove(existing_food)
            print(f"{existing_food.get_name()} was removed from the menu!")
        else:
            print(f"{existing_food.get_name()} is NOT in the menu")

    def print_prices(self):
        print(self.menu)

menu1: Menu = Menu(food_list=[food1, food2])
menu1.show_menu()
print("\n")
menu1.add_Food(food3)
menu1.show_menu()
print("\n")
menu1.remove_Food(food2)
menu1.show_menu()
print("\n")
menu1.add_Food(food3)
menu1.show_menu()
print("\n")
menu1.remove_Food(food2)
menu1.show_menu()

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 
"""Esercizi Lezione 6 (Obbligatori)"""


"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods."""

"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance."""

""" 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business. """

class Restaurant_file:
    
    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        self.restaurant_name: str = restaurant_name
        self.cuisine_type: str = cuisine_type
        self.number_served: int = 0

    def describe_restaurant(self) -> str:
        return f"The restaurant {self.restaurant_name} is {self.cuisine_type} cuscine."
    
    def open_restaurant(self) -> str:
        return f"The restaurant {self.restaurant_name} is open!!!"
    
    def set_number_served(self, new_number_served: int) -> None:
        self.number_served = new_number_served
    
    def increment_number_served(self, served_in_a_day: int) -> None:
        self.number_served += served_in_a_day
    
restaurant1: Restaurant_file = Restaurant_file("Tokyo Food", "japanese")
restaurant2: Restaurant_file = Restaurant_file("Mamma Mia Osteria", "italian")
restaurant3: Restaurant_file = Restaurant_file("Picanha na Brasa", "brazilian")

print(restaurant1.describe_restaurant())
print(restaurant1.open_restaurant())
print(restaurant2.describe_restaurant())
print(restaurant2.open_restaurant())
print(restaurant3.describe_restaurant())
print(restaurant3.open_restaurant())
print(restaurant1.number_served)
print(restaurant2.number_served)
print(restaurant3.number_served)
restaurant1.set_number_served(19)
restaurant2.set_number_served(10)
restaurant3.set_number_served(5)
print(restaurant1.number_served)
print(restaurant2.number_served)
print(restaurant3.number_served)
restaurant1.increment_number_served(19)
restaurant2.increment_number_served(10)
restaurant3.increment_number_served(5)
print(restaurant1.number_served)
print(restaurant2.number_served)
print(restaurant3.number_served)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user."""

"""9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0."""

class User:

    def __init__(self, first_name: str, last_name: str, birthday: str, birth_city: str, ) -> None:
        self.first_name:str = first_name
        self.last_name: str = last_name
        self.birthday: str = birthday
        self.birth_city: str = birth_city
        self.login_attempt: int = 0

    def describe_user(self):
        return f"user\'s name: {self.first_name} {self.last_name}, city: {self.birth_city}, birhtday: {self.birthday}"
    
    def greet_user(self):
        return f"Hello, Mr(s). {self.last_name}!"
    
    def increment_login_attempt(self) -> None:
        self.login_attempt += 1
    
user1: User = User("Simone", "Antonelli", "19/08", "Roma")
user2: User = User("Michelle", "Fontana", "06/10", "Frosione")
user3: User = User("Renata", "DiVento", "25/02", "Campinas")

print(user1.describe_user())
print(user1.greet_user())
print(user2.describe_user())
print(user2.greet_user())
print(user3.describe_user())
print(user3.greet_user())

user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
user1.increment_login_attempt()
print(user1.login_attempt)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. """

class IceCreamStand(Restaurant_file):

    def __init__(self, restaurant_name: str, cuisine_type: str, flavors: list[str]) -> None:
        super().__init__(restaurant_name, cuisine_type)
        self.flavors: list = flavors
    
    def describe_flavors(self) -> str:
        str_flavors = ", ".join(self.flavors)
        return f"The following flavors are available: {str_flavors}."
    
icecreamstand1: IceCreamStand = IceCreamStand(restaurant_name = "Suck My Cone", cuisine_type = "Ice Cream Stand", flavors=["chocolate", "strawberry", "vanilla"])

print(icecreamstand1.describe_restaurant())
print(icecreamstand1.describe_flavors())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method. """

class Admin(User):

    def __init__(self, first_name: str, last_name: str, birthday: str, birth_city: str, admin:bool = True) -> None:
        super().__init__(first_name, last_name, birthday, birth_city)
        self.admin = admin
        self.privileges = ["can add post", "can delete user", "can change password"]
    
    def show_privileges(self):
        str_privileges = ", ".join(self.privileges)
        return f"This admin has the following privileges: {str_privileges}"
    
user2: Admin = Admin("Michelle", "Fontana", "06/10", "Frosione")

print(user2.show_privileges())


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges."""

class Admin(User):

    def __init__(self, first_name: str, last_name: str, birthday: str, birth_city: str, privileges, admin:bool = True) -> None:
        super().__init__(first_name, last_name, birthday, birth_city)
        self.admin = admin
        self.priviliges = privileges
    

class Privileges:
    def __init__(self, privileges: list[str]) -> None:
        self.privileges = privileges
    
    def show_privileges(self):
        str_privileges = ", ".join(self.privileges)
        return f"This admin has the following privileges: {str_privileges}"
    
privilege_list = ["can add post", "can delete user", "can change password"]
privileges: Privileges = Privileges(privilege_list)

user2: Admin = Admin("Michelle", "Fontana", "06/10", "Frosinone", privileges)

print(user2.priviliges.show_privileges())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range."""

class Car:
    '''Attempt to represent a car'''

    def __init__(self, make, model, year):
        '''Attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.year}, {self.make}, {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car's mileage'''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading'''
        self.odometer_reading += miles

class Battery:
    '''Represent aspects of the battery'''

    def __init__(self, battery_size=40):
        '''Battery attributes'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print statement describing battery size'''
        print(f"This car has {self.battery_size} KWH battery")
    
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        '''check the battery size and set to 65 if it isn't already'''
        if self.battery_size >= 65:
            print(f"your batteri size is {self.battery_size}")
        else:
            self.battery_size = 65
            print(f"your battery has been upgraded to {self.battery_size}.")


class Electric_Car(Car):
    '''Represent aspects of a car, specific to electric vehicles'''

    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class'''
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = Electric_Car('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly."""

from Restaurant_file import Restaurant

restaurant1: Restaurant = Restaurant("Tokyo Food", "japanese")
restaurant2: Restaurant = Restaurant("Mamma Mia Osteria", "italian")
restaurant3: Restaurant = Restaurant("Picanha na Brasa", "brazilian")
print(restaurant1.describe_restaurant())
print(restaurant1.open_restaurant())
print(restaurant2.describe_restaurant())
print(restaurant2.open_restaurant())
print(restaurant3.describe_restaurant())
print(restaurant3.open_restaurant())
print(restaurant1.number_served)
print(restaurant2.number_served)
print(restaurant3.number_served)
restaurant1.set_number_served(19)
restaurant2.set_number_served(10)
restaurant3.set_number_served(5)
print(restaurant1.number_served)
print(restaurant2.number_served)
print(restaurant3.number_served)
restaurant1.increment_number_served(19)
restaurant2.increment_number_served(10)
restaurant3.increment_number_served(5)
print(restaurant1.number_served)
print(restaurant2.number_served)
print(restaurant3.number_served)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly."""

from admin_file import User, Admin, Privileges

privilege_list = ["can add post", "can delete user", "can change password"]
privileges: Privileges = Privileges(privilege_list)

user2: Admin = Admin("Michelle", "Fontana", "06/10", "Frosinone", privileges)

print(user2.priviliges.show_privileges())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly."""

from admin_and_privileges_classes import Admin, Privileges

privilege_list = ["can add post", "can delete user", "can change password"]
privileges: Privileges = Privileges(privilege_list)

user2: Admin = Admin("Michelle", "Fontana", "06/10", "Frosinone", privileges)

print(user2.priviliges.show_privileges())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times."""

import random

class Dice:

    def __init__(self, sides: int = 6) -> None:
        self.sides = sides

    def roll_dice(self) -> int:
        rolled_dice = random.randint(1, self.sides)
        return rolled_dice
    
dice6: Dice = Dice()
for _ in range(10):
    print(dice6.roll_dice())

print()

dice20: Dice = Dice(20)
for _ in range(10):
    print(dice20.roll_dice())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize."""

lottery_list: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "a", "b", "c", "d", "e"]

random_items = random.sample(lottery_list, 4)

print(f"any ticket matching these 4 numbers or letters wins a prize: {random_items}")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket."""

my_ticket: list =  ['b', "3", "5", 'c']
counter = 0

while sorted(my_ticket) != sorted(random_items):
    counter += 1
    random_items = random.sample(lottery_list, 4)
    if sorted(my_ticket) == sorted(random_items):
        print(f"it took {counter} attempts, {random_items}")
    else:
        print(f"attempt No. {counter}, {random_items}")
