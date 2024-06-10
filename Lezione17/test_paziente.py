### Creazione di Test Case con UnitTest
"""Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
Istruzioni
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Paziente
- Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Paziente."""

import unittest
from paziente import Paziente

# Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
class TestPaziente(unittest.TestCase):

    # Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
    def setUp(self):
        self.paziente = Paziente(first_name = "Marco", last_name = "Cascio", idCode="PZ001")

    # Scrivere test per verificare l'inizializzazione corretta degli attributi first_name, last_name e age
    def test_init_first_name(self):
        paziente = Paziente(first_name = 123, last_name = "Cascio", idCode="PZ001")
        self.assertIsNone(paziente.getName())
        self.assertEqual(paziente.getLastname(), "Cascio")
        self.assertIsNone(paziente.getAge())

    def test_init_last_name(self):
        paziente = Paziente(first_name = "Marco", last_name = 1, idCode="PZ001")
        self.assertIsNone(paziente.getLastname())
        self.assertEqual(paziente.getName(), "Marco")
        self.assertIsNone(paziente.getAge())
  
    def test_init_age(self):
        self.assertEqual(self.paziente.getAge(), 0)
  
    # Scrivere test per verificar il funzionamento del metodo setName
    def test_setName(self):
        self.paziente.setName("Paolo")
        self.assertEqual(self.paziente.getName(),"Paolo")
        self.paziente.setName(123) # Il nome inserito non è una stringa!
        self.assertEqual(self.paziente.getName(),"Paolo")  # non dovrebbe cambiare

    # Scrivere test per verificar il funzionamento del metodo setLastName
    def test_setlastName(self):
        self.paziente.setLastName("Picchiami")
        self.assertEqual(self.paziente.getLastname(),"Picchiami")
        self.paziente.setLastName(123) # Il cognome inserito non è una stringa!
        self.assertEqual(self.paziente.getLastname(),"Picchiami")  # non dovrebbe cambiare
  
    # Scrivere test per verificar il funzionamento del metodo setAge
    def test_setAge(self):
        self.paziente.setAge(35)
        self.assertEqual(self.paziente.getAge(), 35)
        self.paziente.setAge(3.5) # L'età deve essere un numero intero!
        self.assertEqual(self.paziente.getAge(), 35) # non dovrebbe cambiare

    # Scrivere test per greet
    def test_Greet(self):
        self.assertEqual(self.paziente.greet(),"Ciao, sono Marco Cascio! Ho 0 anni!")

    # Scrivere test per verificar il funzionamento del metodo setIdCode
    def test_setID(self):
        self.paziente.setIdCode("PZ100")
        self.assertEqual(self.paziente.getidCode(), "PZ100")
        self.paziente.setIdCode(100) # L'ID code deve essere una stringa!
        self.assertEqual(self.paziente.getidCode(), "PZ100") # non dovrebbe cambiare

    # Scrivere test per verificar il funzionamento del metodo patientInfo
    def test_patientInfo(self):
        self.assertEqual(self.paziente.patientInfo(),f"Paziente: Marco Cascio\nID: PZ001")

if __name__ == "__main__":
    unittest.main()