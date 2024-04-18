# Joao Victor Dal Mas
# 17/04/2024

print("Hello World!")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""" 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”"""

name: str = 'Joao Victor'
surname: str  = 'Dal Mas'
message: str  = f'Hello, {name} {surname}, would you like to learn Python today?'

print(message)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case. """

name: str  = 'joAo'
surname: str  = 'dAl mAs'

lowercase_name: str  = f'{name.lower()} {surname.lower()}'
upercase_name: str  = f'{name.upper()} {surname.upper()}'

print(lowercase_name)
print(upercase_name)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""  2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.” """

print("Albert Einstein, once said: \"A person who never a mistake never tried anything new\".")

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""" 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message. """

author: str  = 'Albert Einstein'
message: str  = "A person who never a mistake never tried anything new"

famous_person: str  = f'{author}, once said: "{message}".'

print(famous_person)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do. """

file: str = 'code.txt'

print(f'The file you searched is named "{file.removesuffix(".txt")}".')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time. """

names: list = ['Bruno', 'Vitor', 'Michele']

print(names[0])
print(names[1])
print(names[2])

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name."""

message_bruno: str = f'{names[0]} is a dear friend who died last year'

message_vitor: str = f'{names[1]} is my youngest friend.'

message_michele: str = f'{names[2]} lives with me.'

print(message_bruno)

print(message_vitor)

print(message_michele)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.” """

transport_modes: list = ["car", "train", "vespa"]
message_transport: str = f'these are my favorites transport modes: {", ".join(transport_modes)}.'
print(message_transport)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner. """

guests: list = ['Buddah', 'Jesus', 'Bin Laden', 'Putin']

print(guests)

invite0: str = f'hey {guests[0]}, i want your zen vibe at my party'

invite1: str = f'my dear {guests[1]}, make a miracle and bring some wine'

invite2and3: str = f'I am not sure if I want both {guests[2]} and {guests[3]} at my party. Sorry!'

print("\n", invite0, "\n", invite1, "\n", invite2and3)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list."""

declined_guest1: str = guests.pop(-2)
print(f'The {declined_guest1} wont come to the party.')

new_guest1 = guests.insert(-1, "Seiya")

print(f'The new guest list is: {", ".join(guests)}.')

new_invite2 = f'It\'s saint {guests[-2]} time! Come over to the party!'
invite2and3: str = f'I am not sure if I want {guests[3]} at my party. Sorry!'
invite3: str = invite2and3

print("\n", invite0, "\n", invite1, "\n", new_invite2, "\n", invite3)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list."""

print(f'great news! I have found a bigger table for our party!')

guests.insert(0, "Obama")
guests.insert(3, "mamma")
guests.append("Lula")
print(f'The new guest list is: {", ".join(guests)}.')

invite0: str = f'Bring USA vibes to the party, Mr.{guests[0]}.'
invite1: str = f'Hey {guests[1]}, I want your zen vibe at my party.'
invite2: str = f'My dear {guests[2]}, make a miracle and bring some wine'
invite3: str = f'Come on over, {guests[3]}! Bring some cake.'
invite4: str = f'It\'s saint {guests[4]} time! Come over to the party!'
invite5: str = f'I am not sure if I want {guests[5]} at my party. Sorry!'
invite6: str = f'Come to the party, dear president {guests[6]}.'

print("\n", invite0,"\n",invite1,"\n",invite2,"\n",invite3,"\n",invite4,"\n",invite5,"\n",invite6)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program."""

print(f'Bad news! I have found that the new bigger table will not arrive on time.I will have to uninvite almost everyone, excpet for two guests!')

uninvited_guest6: str = guests.pop()
print(f'Hey {uninvited_guest6}, you are uninvinted to the party! Hope you have not changed your agenda!')
uninvited_guest5: str = guests.pop()
print(f'Hey {uninvited_guest5}. You are uninvinted to the party! I told you from the start I did not want you to come...')
uninvited_guest0: str = guests.pop(0)
print(f'Hey {uninvited_guest0}. You are uninvinted to the party! No politicals allowed due to lack of seats...')
uninvited_guest4: str = guests.pop()
print(f'Hey {uninvited_guest4}. You are uninvinted to the party! You are not real anyway...')
uninvited_guest3: str = guests.pop(2)
print(f'Hey {uninvited_guest3}. You are uninvinted to the party! Hope you are OK with it.')
new_invite0: str = f'Dear {guests[0]}. You are still invited to the party and I hove you can bring veg food.'
new_invite1: str = f'Dear {guests[1]}. You are still invited to the party and I hove you can bring miracle wine.'
print("\n", new_invite0,"\n",new_invite1)

del guests[0]
del guests[0]
print(f' the empty guest list: {guests}')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed."""

places_to_visit: list = ["Japan", "Chile", "Isreal", "Australia", "Netherlands"] # Store the locations in a list. Make sure the list is not in alphabetical order
print(places_to_visit) # Print your list in its original order
print(sorted(places_to_visit)) # Use sorted() to print your list in alphabetical order without modifying the actual list
print(places_to_visit)
print(sorted(places_to_visit)[::-1]) # Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
print(places_to_visit) # Show that your list is still in its original order
places_to_visit.reverse() # Use reverse()  to change the order of your list.
print(places_to_visit)
places_to_visit.reverse() # Use reverse() to change the order of your list again.
print(places_to_visit)
places_to_visit.sort() # Use sort() to change your list so it’s stored in alphabetical order.
print(places_to_visit)
places_to_visit.sort(reverse = True) # Use sort() to change your list so it’s stored in reverse-alphabetical order
print(places_to_visit) # Print the list to show that its order has changed


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner."""

guests: list = ['Buddah', 'Jesus', 'Bin Laden', 'Putin']
print(f'the number of invites in the list is {len(guests)}.')


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once."""

countries = ["Brasil", "USA", "United Kingdom", "Italy", "France"]

countries.pop()
print(countries)
countries.append("France")
print(countries)
countries.remove("France")
del countries[0]
countries.insert(0, "Brasil")
print(countries)
countries.sort()
print(countries)
countries.sort(reverse = True)
print(countries)
print(sorted(countries))
print(sorted(countries)[::-1])
print(f'The final sorted country list is: {", ".join(sorted(countries))}.')


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

"""6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary."""

person: dict = {'first_name': 'Michele', 'last_name': 'Fontevecchia', 'age' : '56', 'city' : 'Rome'}
print(f'The person\'s first name is {person["first_name"]}.')
print(f'The person\'s last name is {person["last_name"]}.')
print(f'The person\'s age is {person["age"]}.')
print(f'The person lives in {person["city"]}.')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program. """

favorite_numbers: dict = {}

favorite_numbers['Michele'] = '56'
favorite_numbers['Joao'] = '8'
favorite_numbers['Renata'] = '25'
favorite_numbers['Gerarda'] = '31'
favorite_numbers['Alessia'] = '51'

for person, number in favorite_numbers.items():
    print(f'The favorite number of {person} is {number}.')


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output."""

glossary: dict = {
    'string': 'anything you put inside \'\'' , 
    'integer': 'numbers in full without fraction', 
    'boolean': 'a True or False sentence',
    "dictionary": "group of a key - value",
    "collections": "complex data type to collect infomation"
    }

for key, value in glossary.items():
    print(f'\nthe meaning of "{key.upper()}" is "{value.upper()}."')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person."""

Michele: dict = {'first_name': 'Michele', 'last_name': 'Fontevecchia', 'age' : '56', 'city' : 'Rome'}
Joao: dict = {'first_name': 'Joao', 'last_name': 'Dal Mas', 'age' : '35', 'city' : 'Rome'}
Renata: dict = {'first_name': 'Renata', 'last_name': 'di Vecce', 'age' : '36', 'city' : 'Monaco di Baviera'}

people: list = []
people.append(Joao)
people.append(Michele)
people.append(Renata)

for person in people:
    print(person)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. """

pet1: dict = {'kind': 'dog', 'owner': 'Michele'}
pet2: dict = {'kind': 'cat', 'owner': 'Alessia'}
pet3: dict = {'kind': 'mouse', 'owner': 'Bruno'}
pet4: dict = {'kind': 'rabbit', 'owner': 'Renata'}

pets: list = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"The pet is a {pet['kind']} owned by {pet['owner']}.")


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places."""

favorite_places: dict = {
    'Joao': ['Paris', 'Kyoto'],
    'Michele': ['New York'],
    'Bruno': ['Sydney', 'Rio de Janeiro', 'Tokyo']
}
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: {', '.join(places)}.")


# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers."""

favorite_numbers['Michele'] = ['56', "12", "13"]
favorite_numbers['Joao'] = ['8', "999"]
favorite_numbers['Renata'] = ['25', "01", "1988"]
favorite_numbers['Gerarda'] = ['31', "7", "14", "21"]
favorite_numbers['Alessia'] = ['51', "11", "08"]

for name, numbers in favorite_numbers.items():
    print(f'the favorite number of {name} are {numbers}.')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it."""

cities: dict = {
    'Rome' : {
        'location' : 'Italy',
        'population' : '2.8 million people',
        'language' : 'italian'
    },
    'Sao Paulo' : {
        'location' : 'Brasil',
        'population' : '12.3 million people',
        'language' : 'portuguese' 
    },
    'Paris' : {
        'location' : 'France',
        'population' : '2.2 million people',
        'language' : 'french' 
    } 
    }

for name, city_info in cities.items():
    print(f'\nname of the city: {name.title()}')
    location: str = city_info['location']
    print(f'location: {location}')
    population: str  = city_info['population']
    print(f'the aprox. population of the city is {population}')
    language: str  = city_info['language']
    print(f'the language spoken is {language}')

# -------------------------------------------------------------------------------------------------------------------------------
print("\n")

""" 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output."""

favorite_numbers['Michele'] = ['56', "12", "13"]
favorite_numbers['Joao'] = ['8', "999"]
favorite_numbers['Renata'] = ['25', "01", "1988"]
favorite_numbers['Gerarda'] = ['31', "7", "14", "21"]
favorite_numbers['Alessia'] = ['51', "11", "08"]

for name, numbers in favorite_numbers.items():
    numbers_str: str = ", ".join(numbers)
    print(f'the favorite number of {name.upper()} are {numbers_str}.')