"""8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly. """

def display_message() -> str:
    """A function that prints one sentence telling everyone what you are learning about in this chapter"""
    return("I am learning functions!!!")

print(display_message())

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as "One of my favorite books is Alice in Wonderland". Call the function, making sure to include a book title as an argument in the function call."""

def favorite_book(book_title: str) -> str:
    """A function that accepts one parameter, book title, and print a message"""
    if isinstance(book_title, str):
        return(f"The book {book_title.title()} is a wonderful book!!!!")
    else:
        return ValueError("requires one str parameter: book_title")

print(favorite_book(book_title="python\'s crash course"))


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments."""

def make_shirt(shirt_size: str, message: str) -> str:
    """A function that accepts two parameteres, shirt size and text to be printed on the shirt, and returns sentence summarizing the size of the shirt and the message printed on it."""
    if shirt_size in {"S", "M", "L"} and isinstance(message, str):
        return(f"The shirt size is {shirt_size.upper()} and your text is: \"{message.title()}\"")
    else:
        return ValueError("funcion requires two str parameter: shirt_size (S, M or L) and message")
    
print(make_shirt("L", "hope you have a nice day!!!!"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message."""

def make_shirt(shirt_size: str = "L", message: str = "i love python") -> str:
    """A function that accepts two parameteres, shirt size and text to be printed on the shirt, and returns sentence summarizing the size of the shirt and the message printed on it."""
    if shirt_size in {"S", "M", "L"} and isinstance(message, str):
        return(f"The shirt size is {shirt_size.upper()} and your text is: \"{message.title()}\"")
    else:
        return ValueError("funcion requires two str parameter: shirt_size (S, M or L) and message")
    
print(make_shirt())
print(make_shirt("M"))
print(make_shirt("L", "hope you have a nice day!!!!"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country."""

def describe_city(city: str, country: str = "Italy") -> str:
    """Function that accepts two parameters, city name and its country, and print a simple sentence"""
    if isinstance(city, str) and isinstance(country, str):
        return(f"The city of {city.title()} is located in {country.title()}.")
    else:
        return ValueError("funcion requires two str parameter: city and country. Default country value = \"Italy\".")
    
print(describe_city("Sao Paulo", "Brazil"))
print(describe_city("New York", "usa"))
print(describe_city("Rome"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned."""

def city_country(city: str, country: str) -> str:
    """ Function that takes two parameters, city name and its country, and return str like this: "city, country"."""
    if isinstance(city, str) and isinstance(country, str):
        return(f"{city.title()}, {country.title()}.")
    else:
        return ValueError("funcion requires two str parameter: city and country.")

print(city_country("Sao Paulo", "Brazil"))
print(city_country("New York", "usa"))
print(city_country("Rome", "Italy"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly. Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album."""

def make_album(artist: str, album_name: str, number_of_songs: int = None) -> dict:
    """ Function that builds a dictionary describing a music album. Take in an artist name and an album title, and it should return a dictionary. Third parameter allows to store the number of songs."""
    risult: dict = {}
    if number_of_songs == None:
        risult[artist] = album_name
        return risult
    else:
        risult[artist] = (album_name, number_of_songs)
        return risult

print(make_album("Shakira", "Laundry Service", 13))
print(make_album("Shakira", "Oral Fixation"))
print(make_album("Shakira", "She Wolf", 12))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")


"""8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop."""

#loop: bool = True
#while loop == True:
#    message: str = input("Do you want to create a dictionary with your favorite album? [answer \"no\" to leave the app] ")
#    if message == "no":
#        break
#    else:
#        parameter1: str = input("Please insert the singer\'s name: ")
#        parameter2: str = input("Please insert the album\'s name: ")
#        parameter3: int = input("Please insert number of records: ")
#    print(make_album(artist = parameter1, album_name = parameter2, number_of_songs = parameter3))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message."""

short_messages: list = ["Hope you are doing fine!", "Grow strong!", "you can do it!"]

def print_messages(arg: list) -> str:
    """ Function that prints each text message from a list"""
    for message in arg:
        print(message)

print_messages(short_messages)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")
"""8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly."""

unsent_messages: list = ['Hi, are you ok?', 'Miss you!', 'Let\'s have some fun!']

sent_messages: list = []

def send_messages(list: list) -> list:
    """ Function that prints each text message from a list and moves each message to a new list called sent_messages as it’s printed"""
    while unsent_messages:
        for message in unsent_messages:
            current_message = unsent_messages.pop(0)
            print(f'\nSending this message "{current_message}"...')
            print('Done!')
            sent_messages.append(current_message)
    if not unsent_messages:
        print("You have no unsent messages!")
  
    print("You have sent the following messages:" + (str(sent_messages)))

send_messages(unsent_messages)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages."""

send_messages(sent_messages[:])
print(sent_messages)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time."""

def sandwiches(*args: tuple) -> str:
    """ Function that accepts items a person wants on a sandwich and it should print a summary of the sandwich being ordered."""
    return f"Your sandwich with {', '.join(args)} has been ordered!"

print(sandwiches("pomodoro", "mozzarella"))
print(sandwiches("prosciuto", "mozzarella", "rucula"))

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you. All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"""

def build_profile(first_name: str, last_name: str, param1: dict, param2:dict, param3:dict) -> str:
    """Function that builds a profile of yourself, using your first and last names and three other key-value pairs that describe you as parameterers"""
    return f"My name is {first_name.title()} {last_name.title()}, {list(param1.keys())[0]}: {list(param1.values())[0]}, {list(param2.keys())[0]}: {list(param2.values())[0]}, {list(param3.keys())[0]}: {list(param3.values())[0]}."

print(build_profile(first_name="Joao", last_name="Dal Mas", param1={"age": 35}, param2={"hair": "brown and curly"}, param3={"height":"1.83 cm"}))


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned to make sure all the information was stored correctly. """

def make_car(manufacturer: str, car_model: str, **kwargs: dict) -> dict:
    """ Function that stores information about a car in a dictionary. Function should always receive a manufacturer and a model name and accepts an arbitrary number of dictionary arguments."""
    risult: dict = {"car model": car_model, "manufacturer": manufacturer}
    risult.update(kwargs)
    return risult

car: list = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions."""
""" 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import * """

from car_printing_function import make_car as mk

car2: list = mk('honda', 'civic', color='gray', tow_package=False)
print(car2)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section,."""