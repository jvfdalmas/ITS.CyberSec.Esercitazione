### CLASSE: Paziente
"""Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).

- Definire i seguenti metodi:

    - costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.

    - setIdCode(idCode): consente di impostare il codice identificativo del paziente.

    - getidCode(): consente di ritornare il codice identificativo del paziente.
   
    - patientInfo(): stampa in output le informazioni del paziente in questo modo:
        "Paziente: nome e cognome
         ID: codice identificativo" """

from persona import Persona

class Paziente(Persona):

    def __init__(self, first_name: str, last_name: str, idCode: str):
        
        # Chiama nome, cognome ed età definiti dalla classe Persona,
        Persona.__init__(self, first_name, last_name)

        # Controllo se idCode è una stringa
        if isinstance(idCode, str):
            self.__idCode = idCode
        else:
            self.__idCode = None
            print("L'id Code inserito non è una stringa!")

    def setIdCode(self, idCode: str):
        # Consente di impostare il codice identificativo del paziente
        if isinstance(idCode, str):
            self.__idCode = idCode
        else:
            print("L'id Code inserito non è una stringa!")
    
    def getidCode(self): 
        # Consente di ritornare il codice identificativo del paziente.
        return self.__idCode

    def patientInfo(self): 
        #  Stampa in output le informazioni del paziente in questo modo: "Paziente: nome e cognome \n ID: codice identificativo"
        return f"Paziente: {self.getName()} {self.getLastname()}\nID: {self.getidCode()}"