"""1. Create a Playlist:

Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. The function should return a dictionary with the playlist name and a set of songs. Call the function with different numbers of songs to demonstrate flexibility.

Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary, the name of a playlist, and a boolean value indicating whether it is liked (True or False). This function should return an updated dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)"""

def create_playlist(playlist_name: str, songs_titles: set) -> dict:
    playlist: dict = {playlist_name: list(songs_titles)}
    return playlist

playlist1 = create_playlist("Road Trip", {"Song 1", "Song 2"})
playlist2 = create_playlist("Chill Vibes", {"Song 3", "Song 4", "Song 5"})
print(playlist1)
print(playlist2)


def add_like(playlists_dict: dict, playlist_name: str, liked: bool):
    for name in playlists_dict.keys():
        if name == playlist_name:
            return playlists_dict
        else:
            playlists_dict[playlist_name] = []
            return playlists_dict


updated_playlist = add_like(playlist1, "Road Trip", liked = True)
print(updated_playlist)
updated_playlist = add_like(playlist1, "Trip", liked = True)
print(updated_playlist)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""2. Book Collection:

Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. This function should return a dictionary where the author's name is the key and the value is a list of their books. Demonstrate this function by adding books for different authors.

Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. This function should return an updated dictionary.

Example: delete_book(dictionary, “Mark Twain”)"""

def add_book(author_name: str, books: list) -> dict:
    risult: dict = {author_name: len(books)}
    return risult

MK_dict = add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
print(MK_dict)

def delete_book(dictionary: dict, author_name: str) -> dict:
    if author_name in dictionary:
        dictionary.pop(author_name)
    return dictionary

delete_book(MK_dict, "Mark Twain")
print(MK_dict)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""3. Personal Info:

Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. Make occupation, location, and age optional parameters. Use this function to create profiles for different people, demonstrating how it handles these optional parameters.

Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)"""

def build_profile(name: str, surname: str, occupation: str = None, location: str = None, age:int = None) -> dict:
    
    complete_name:str = name.title() + " " + surname.title()
    initial_profile: dict = {"Complete Name": complete_name}
    profile = {complete_name: {}}
    
    if occupation is not None:
        profile[complete_name]["Ocuppation"] = occupation
    if location is not None:
        profile[complete_name]["Location"] = location
    if age is not None:
        profile[complete_name]["Age"] = age
    
    if occupation is None and location is None and age is None:
        return initial_profile
    else:
        return profile

JD_profile = build_profile("John", "Doe")
print(JD_profile)
JD_profile = build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
print(JD_profile)

# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""4. Event Organizer:

Write a function called plan_event() that accepts an event name, a list of participants, and an hour. The function should return a dictionary that includes the event name and a list of the participants. Call this function with varying numbers of participants to plan different events.

Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)"""

def plan_event(event_name: str, participants: list, time: str) -> dict:
    event: dict = {event_name: {"list of participants": participants, "time of the event": time}}
    return event

eventA = plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],"4pm")
print(eventA)

def modify_event(dict_events: dict, event_name: str, participants: list = None, time: str = None) -> dict:
    if event_name in dict_events:
        if participants is not None:
            dict_events[event_name]["list of participants"] = participants
        if time is not None:
            dict_events[event_name]["time of the event"] = time
        return dict_events
    else:
        return "no change was made"
    

modify_event(eventA, "D", ["Alice", "Bob", "Charlie"],"4pm")
print(eventA)

modify_event(eventA, "Code Workshop", ["Alice", "Charlie"],"3pm")
print(eventA)


# -------------------------------------------------------------------------------------------------------------------------------
print("\n") 

"""5. Shopping List:

Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. It should return a dictionary with the store name and a set of items to buy there. Test the function with different stores and item lists.

Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

Write a function called print_shopping_list() that accepts a dictionary and a store name, then prints each item from that store's shopping list.

Example: print_shopping_list(dictionary, "Grocery Store")"""