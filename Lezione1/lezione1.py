# Define variables name and age containing a name and an age. Format a string so that it prints out “My name is <NAME> and I am <AGE> years old.” (<...> are placeholders for the name and age)

name = "Victor"
age = 36

print( f"my name is {name} and I am {age} years old.")

# -----------------------------------------------------------------------------------------------------------------------------
print("\n")

# Given variables length and width, calculate the area and perimeter of a rectangle. Print the results in a formatted string!

widht = input("insert the base of the rectangle in cm: ")
lenght = input("insert the height of the rectangle in cm: ")
area_rectangle = int(widht) * int(lenght)
permiter_rectangle = (2 * int(widht)) + (2 * int(lenght))

if area_rectangle > 0 and permiter_rectangle > 0:
    print(f"considering a base of {widht} cm and a legnth of {lenght} cm, the area of the rectangle is {area_rectangle} cm2 and the permiter of the rectangle is {permiter_rectangle} cm.")
else:
    print("values are not valid to calculate the rectangle!")


# -----------------------------------------------------------------------------------------------------------------------------
print("\n")
# 1 Define a list called alphabet. It should contain the first 5 letters of the alphabet.

alphabet = ["a","b","c","d","e"]
print(f"The first five letters of the alphabet are: {alphabet}.")

# -----------------------------------------------------------------------------------------------------------------------------
print("\n")
# 2 Define the variables first_letter and last_letter. Fill them accordingly.

first_letter = alphabet[0]
last_letter = alphabet[-1]
print(f"The first letter of the list above is '{first_letter}', and the last letter of the list is '{last_letter}'.")

# -----------------------------------------------------------------------------------------------------------------------------
print("\n")
# 3 Define the variable first_three. Use slicing to fill this variable.

first_three = alphabet[0:3]
print(f"The first three letters of the list are: {first_three}.")

# -----------------------------------------------------------------------------------------------------------------------------
print("\n")
# 4 Define the variable last_three. Use slicing to fill this variable.

last_three = alphabet[-3:]
print(f"The last three letters of the list are: {last_three}.")

# -----------------------------------------------------------------------------------------------------------------------------
print("\n")
# 5 Add the next 3 letters of the alphabet to our alphabet.

alphabet += ["f","g","h"]
print(f"After including three more letters, the new list is: {alphabet}.")

# -----------------------------------------------------------------------------------------------------------------------------
print("\n")
# 6 Now, update your variable last_three.

last_three = alphabet[-3:]
print(f"The updated last three letters of the list are: {last_three}.")

# -----------------------------------------------------------------------------------------------------------------------------
print("\n")
# 7 Delete the last letter from our alphabet

alphabet.pop()
print(f"Afther deleting the last letter, the final list is: {alphabet}.")