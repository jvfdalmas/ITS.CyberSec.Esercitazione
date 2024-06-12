"""CLASSE: Fattura
Creare un file chiamato "fatture.py".
In tale file, creare una classe chiamata Fattura.

- Definire i seguenti metodi:

    - init(patient,doctor): deve avere come input una lista di pazienti ed un dottore.
    Tale metodo deve verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor().
    In caso affermativo assegnare all'attributo fatture (di tipo intero) il numero di pazienti che ha il dottore, mentre assegnare 0 all'attributo salary (di tipo int).
    In caso contrario, assegnare il valore None a tutti i 4 gli attributi della classe e stampare un messaggio di errore, come, ad esempio:
    "Non è possibile creare la classe fattura poichè il dottore non è valido!".

    - getSalary(): deve ritornare il salario guadagnato dal dottore.
    Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.

    -getFatture(): deve ritornare il valore dell'attributo fatture, dopo aver assegnato ad esso il numero dei pazienti che ha il dottore.

    - addPatient(newPatient): consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary().
    Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente codice_identificativo"

    - removePatient(): consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary().
    Stampare "Alla lista del Dottor cognome è stato rimosso il paziente codice_identificativo"

- Scrivere, infine, il codice driver che crei due dottori e due liste di pazienti.
  La prima lista di pazienti deve contere 3 pazienti, mentre la seconda 1 paziente solo.

    - Impostare l'età di ogni medico, affinchè i due medici risultino validi!
    - Il primo medico si presenta, richiamando il metodo doctorGreet().
    - Si presenta anche il secondo medico!

    - Creare un oggetto fattura chiamato fattura1. Alla fattura 1 devono essere associati il dottore_1 e la lista di 3 pazienti.

    - Creare un oggetto fattura chiamato fattura2. Alla fattura 2 devono essere associati il dottore_2 e la lista di un paziente solo.

    - Stampare in output il salario di ogni singolo dottore. Ad esempio:
      "Salario Dottore1: salario euro!
       Salario Dottore2: salario euro!"

    - Rimuovere un paziente dalla lista dei pazienti del dottore 1 ed inserire tale paziente nella lista del dottore 2.
    - Stampare in output il salario di ogni dottore.
    - Stampare in output il guadagno totale incassato dall'ospedale. Il guadagno totale viene calcolato sommando i guadagni di ogni dottore.
      Esempio:
      "In totale, l'ospedale ha incassato: tot euro!" """

from paziente import Paziente
from dotttore import Dottore

class Fattura:
    
  def __init__(self, patient: list[Paziente], doctor: Dottore) -> None:
        
    #Verificare se il dottore può esercitare la professione, richiamando la funzione isAValidDoctor()
    if doctor.isAValidDoctor():
      self.__patient = patient
      self.__doctor = doctor
      self.__fatture = len(self.__patient)
      self.__salary = len(self.__patient) * doctor.getParcel()
    else:
      self.__fatture = None
      self.__salary = None
      self.__patient = None
      self.__doctor = None
      return "Non è possibile creare la classe fattura poichè il dottore non è valido!"

  def getSalary(self):
    # Deve ritornare il salario guadagnato dal dottore
    self.__salary = len(self.__patient) * self.__doctor.getParcel()
    return self.__salary

  def getFatture(self): 
    # Deve ritornare il valore dell'attributo fatture, dopo aver assegnato ad esso il numero dei pazienti che ha il dottore.
    self.__fatture = len(self.__patient)
    return self.__fatture

  def addPatient(self, newPatient: Paziente): 
    # Consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario, richiamando il metodo getFatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente codice_identificativo"
    self.__patient.append(newPatient)
    self.getFatture()
    self.getSalary()
    return f"Alla lista del Dottor {self.__doctor.getLastname()} è stato aggiunto il paziente {newPatient.getidCode()}"

  def removePatient(self, oldPatient: Paziente): 
    # Consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary(). Stampare "Alla lista del Dottor cognome è stato rimosso il paziente codice_identificativo""""
    if oldPatient in self.__patient:
      self.__patient.remove(oldPatient)
      self.getFatture()
      self.getSalary()
      return f"Alla lista del Dottor {self.__doctor.getLastname()} è stato rimosso il paziente {oldPatient.getidCode()}"
    else:
      return f"il paziente {oldPatient.getidCode()} non c'è alla lista del Dottor {self.__doctor.getLastname()}"

