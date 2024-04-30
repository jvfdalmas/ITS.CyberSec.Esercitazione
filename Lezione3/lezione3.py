# Joao Victor Figueiredo Dal Mas
# 30/04/2024

"""4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!"""

pizze: list = ['margheritta', 'mozzarella', 'fiore di zucca']

for pizza in pizze:
    if pizza == "margheritta":
        print(f'the {pizza} is my favorite pizza!')
    elif pizza == "mozzarella":
        print(f'the {pizza} is my second favorite pizza!')
    elif pizza == "fiore di zucca":
        print(f'the {pizza} is one of the pizzas that I tried for the first time in Italy!')
print("\nI love all these pizze")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!"""

Animals: list = ["monkey", "gorilla", "ape"]
for Animal in Animals:
    print(f"I don't think {Animal} would make a good pet...")
print("None of these animals would make a good pet...")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive."""

countingto20: list = [number for number in range(1,21)]
print(countingto20)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)"""

countingtomillion: list = [number for number in range(1_000_001)]
print(countingtomillion)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers."""

print(min(countingtomillion))
print(max(countingtomillion))
print(sum(countingtomillion))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number."""

Oddnumbers: list = [number for number in range(1, 21, 2)]
print(Oddnumbers)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list."""

multipleofthree: list = []
for number in range(3,33):
    if number % 3 == 0:
        multipleofthree.append(number)
print(multipleofthree)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube."""

cubes: list = []
for number in range(1,11):
    cube: int = number ** 3
    cubes.append(cube)
print(cubes)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes."""

Cubes: list = [number ** 3 for number in range(1,11)]
print(Cubes)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list."""

My_Pizza: list = ['mozzarella', 'pepperone', 'fior di zucca', 'capriciosa']
print(f"The first three pizzas of my list are {', '.join(My_Pizza[0:3])}")
print(f"The two pizzas in the middle of my list are {', '.join(My_Pizza[1:3])}")
print(f"The last three pizzas of my list are {', '.join(My_Pizza[-3::])}")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list."""

My_Pizza: list = ['mozzarella', 'pepperone', 'fior di zucca', 'capriciosa']
Friends_Pizza: list = My_Pizza[:]
My_Pizza.append('rucula')
Friends_Pizza.append('pollo')

print(f"My favorite pizzas are {', '.join(My_Pizza)}")

for pizza in Friends_Pizza:
    print(f"This is one of my friends' favorite pizza: {pizza}.")


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""4-14. PEP 8:  Look through the original PEP 8 style guide at https://peps.python.org/pep-0008/ You won’t use much of it now, but it might be interesting to skim through it."""
"""4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8."""

Oddnumbers: list = [number for number in range(1, 21, 2)]
print(Oddnumbers)

animals: list = ["monkey", "gorilla", "ape"]
for animal in animals:
    print(f"I don't think {animal} would make a good pet...")
print("None of these animals would make a good pet...")

my_pizza: list = ['mozzarella', 'pepperone', 'fior di zucca', 'capriciosa']
print(f"The first three pizzas of my list are {', '.join(my_pizza[0:3])}")
print(f"The two pizzas in the middle of my list are {', '.join(my_pizza[1:3])}")
print(f"The last three pizzas of my list are {', '.join(my_pizza[-3::])}")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False."""

animal: list = "monkey"

print("Is animal == ape? I predict False!")
print(animal == "ape")

print("Is animal == bee? I predict False!")
print(animal == "bee")

print("Is animal == whale? I predict False!")
print(animal == "whale")

print("Is animal == gorilla? I predict False!")
print(animal == "gorilla")

print("Is animal == lion? I predict False!")
print(animal == "lion")

print("Is animal == monkey? I predict True!")
print(animal == "monkey")

animal: str = "dog"
print("Is animal == dog? I predict True!")
print(animal == "dog")

animal: str = "cat"
print("Is animal == cat? I predict True!")
print(animal == "cat")

animal: str = "duck"
print("Is animal == duck? I predict True!")
print(animal == "duck")

animal: str = "mouse"
print("Is animal == mouse? I predict True!")
print(animal == "mouse")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list"""

print("Is ciao == Ciao? I predict False")
print("ciao" == "Ciao")

print("Is ciao != Ciao? I predict True")
print("ciao" != "Ciao")

my_pizza: list = ['mozzarella', 'pepperone', 'fior di zucca', 'capriciosa']
print("is salsiccia in the list? I predict False!")
if "salsiccia" in my_pizza:
    print(True)
else:
    print(False)

print("is salsiccia NOT in the list? I predict True!")
if "salsiccia" not in my_pizza:
    print(True)
else:
    print(False)

x: int = 100
print("is X <= 50? I predict False")
if x <= 50:
    print(True)
else:
    print(False)
print("is X == 100? I predict True")
if x == 100:
    print(True)
else:
    print(False)
print("is X >= 150? I predict False")
if x >= 150:
    print(True)
else:
    print(False)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.) """

alien_color: str = 'green'

if alien_color == 'green':
    print('the color green means you earned 5 points!')

if alien_color == 'red':
    print('the alien is in danger')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block."""

if alien_color == 'green':
    print('you earned 5 points!')
if alien_color != 'green':
    print('you earned 10 points!')

if alien_color == 'green':
    print('you earned 5 points!')
else:
    print('you earned 10 points!')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien."""

alien_colorG: str = 'green'
if alien_colorG == 'green':
    print('you earned 5 points!')
elif alien_colorG == 'yellow':
    print('you earned 10 points!')
elif alien_colorG == 'red':
    print('you earned 15 points!')
else:
    print('you did not earn points!')

alien_colorY: str = 'yellow'
if alien_colorY == 'green':
    print('you earned 5 points!')
elif alien_colorY == 'yellow':
    print('you earned 10 points!')
elif alien_colorY == 'red':
    print('you earned 15 points!')
else:
    print('you did not earn points!')

alien_colorR: str = 'red'
if alien_colorR == 'green':
    print('you earned 5 points!')
elif alien_colorR == 'yellow':
    print('you earned 10 points!')
elif alien_colorR == 'red':
    print('you earned 15 points!')
else:
    print('you did not earn points!')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder."""

age: int = 65

if 0 <= age < 2:
    print("the person is a baby.")
elif 2 <= age <4:
    print("the person is a toddler.")
elif 4 <= age < 13:
    print("the person is a kid.")
elif 13 <= age < 20:
    print("the person is a teenager.")
elif 20 <= age < 65:
    print("the person is an adult.")
elif 65 <= age:
    print("the person is an elder.")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like Apples!"""

favorite_fruits: list = ["banana",  "orange", "pineapple"]

for fruit in favorite_fruits:
    if fruit == "blackberry":
        print(f"You really like {fruit.title()}!!!")
    if fruit == "banana":
        print(f"You really like {fruit.title()}!!!")
    if fruit == "orange":
        print(f"You really like {fruit.title()}!!!")
    if fruit == "pineapple":
        print(f"You really like {fruit.title()}!!!")
    if fruit == "apple":
        print(f"You really like {fruit.title()}!!!")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again."""

usernames: list = ['admin', 'jdalmas', 'mfontevecchia', 'bandreucci', 'rdinatale']

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f'Welcome {user.upper()}! Please check the other users before you start your work.')
        if user != 'admin':
            print(f'Welcome {user.title()}! Report to {usernames[0].upper()} before working.')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed."""

usernames.clear()

if len(usernames) == 0:
    print('We need to find new users!')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.) """

usernames: list = ['admin', 'jdalmas', 'mfontevecchia', 'bandreucci', 'rdinatale']
new_users: list = ['rfontevecchia', 'Jdalmas', 'apannonne', 'jvsoares', 'Rdinatale']

for user in new_users:
    user = user.lower()
    if user in usernames:
        print(f'{user} has already been assigned in the past.')
    else:
        print(f'the username {user} is available.')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line."" """

numbers: list = []

for number in range(1,10):
    if number == 1:
        print('1st')
        numbers.append('1st')
    elif number == 2:
        print('2nd')
        numbers.append('2nd')
    elif number == 3:
        print('3rd')
        numbers.append('3rd')
    else:
        print(str(number) + 'th')
        numbers.append(str(number) + 'th')
print(numbers)