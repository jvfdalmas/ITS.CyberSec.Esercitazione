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
persona_2: Person = Person(name="Joao Victor", surname="Figueiredo", birthday="03/07/1988", birth_place="Campinas", gender="Male")
persona_3: Person = Person(name="Michele", surname="Fontevecchia", birthday="06/10/1967", birth_place="Sora", gender="Male")

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

student1: Student = Student(name = "Joao Victor", study_program="Cybersecurty", age=35, gender="Male")
student2: Student = Student(name = "Simone", study_program="Cybersecurty", age=20, gender="Male")
student3: Student = Student(name = "Angelo", study_program="Cybersecurty", age=19, gender="Male")

print(student1.print_info())
print(student2.print_info())
print(student3.print_info())




