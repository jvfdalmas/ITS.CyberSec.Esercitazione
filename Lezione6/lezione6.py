""" CLASSE """

class Person:

    def __init__(self, name: str, surname: str, taxpayers_id: str, birthday: str, birth_place: str, gender: str) -> None:
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
        
        self._taxpayers_id = taxpayers_id

    def compute_taxpayers_id(self) -> str:
        self._taxpayers_id: str = "calcolare il CF!"
        pass
    
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
    
persona_1: Person = Person(name="Flavio", surname="Giorgi", taxpayers_id="DGDFVR", birthday="24/12/1994", birth_place="Roma", gender="Male")
#persona_2: Person = Person(name="Joao", surname="Dal Mas", taxpayers_id="DMJVF")

print(persona_1._name, persona_1.surname)
#print(persona_2._name, persona_2.surname)

print(persona_1.get_name())
print(str(persona_1))
#print(str(persona_2))

#queue: list = [persona_1, persona_2]
#for person in queue:
#    persons_name = person.get_name()
#    persons_tax_id = person.get_taxpayers_id()
#    print(f"The taxpayers id of {persons_name} is {persons_tax_id}")

persona_1.set_taxpayers_id("FFFF")
print(persona_1.get_taxpayers_id())



