### CLASSE Dottore
"""Creare un file chiamato "dottore.py".
In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona, una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale), ed una parcella per le visite in studio (si usi il tipo float).
Gli attributi della classe dottore devono essere anch'essi privati.

- Definire i seguenti metodi:
    - costruttore della classe Dottore, il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel).
    Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float, altrimenti assegna None all'attributo che non verifica la condizione richiesta, mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".

    - setSpecialization(specialization): consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo. Il valore viene modificato se e solo se viene passata al metodo una stringa.
    In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".

    - setParcel(parcel): consente di impostare la parcella di un dottore, modificando il valore del relativo attributo.
    Il valore viene modificato se e solo se viene passato al metodo un float.
    In caso contrario, stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".

    - getSpecialization(): consente di ritornare la specializzazione del dottore.

    - getParcel(): consente di ritornare la parcella del dottore.

    - isAValidDoctor(): stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!" , se il dottore risulta valido.
    In caso contrario, stampare "Doctor nome e cognome is not valid!".

    - doctorGreet():tale metodo richiama la funzione greet() della classe Persona.
    Poi, stampa il seguente saluto "Sono un medico specializzazione" """

from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        
        # Chiama nome, cognome ed età definiti dalla classe Persona,
        Persona.__init__(self, first_name, last_name)
        
        # Controllo se specialization è una stringa
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")

        # Controllo se parcel è un float
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization: str):
        # Consente di impostare la specializzazione di un dottore
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel: float):
        #  Consente di impostare la parcella di un dottore,
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self) -> str:
        # Consente di ritornare la specializzazione del dottore
        return self.__specialization

    def getParcel(self) -> str:
        # Consente di ritornare la parcel del dottore
        return self.__parcel

    def isAValidDoctor(self) -> str:
        # Stabilisce se un dottore è un dottore valido
        if self.getAge() > 30:
            return f"Doctor {self.getName()} {self.getLastname()} is valid!"
        else:
            return f"Doctor {self.getName()} {self.getLastname()} is not valid!"
        
    def doctorGreet(self):
        # Richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto "Sono un medico {specialization}"
        self.greet()
        return f"{self.greet()}\nSono un medico {self.getSpecialization()}"