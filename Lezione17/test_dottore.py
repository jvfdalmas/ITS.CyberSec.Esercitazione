### Creazione di Test Case con UnitTest
"""Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
Istruzioni
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Dottore
- Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi specifici di Dottore.
  - Il funzionamento del metodo isValidDoctor con diverse età."""

import unittest
from dotttore import Dottore

class TestDottore(unittest.TestCase):
  # Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
  def setUp(self):
    self.dottore = Dottore(first_name = "Michele", last_name = "Fonte", specialization = "estetico", parcel= 0.4)

  # Scrivere test per verificare l'inizializzazione corretta degli attributi first_name, last_name e age
  def test_init_first_name(self):
    dottore = Dottore(first_name = 123, last_name = "Fonte", specialization = "estetico", parcel= 0.4)
    self.assertIsNone(dottore.getName())
    self.assertEqual(dottore.getLastname(), "Fonte")
    self.assertIsNone(dottore.getAge())

  def test_init_last_name(self):
    dottore = Dottore(first_name = "Michele", last_name = 1, specialization = "estetico", parcel= 0.4)
    self.assertIsNone(dottore.getLastname())
    self.assertEqual(dottore.getName(), "Michele")
    self.assertIsNone(dottore.getAge())
  
  def test_init_age(self):
    self.assertEqual(self.dottore.getAge(), 0)
  
  # Scrivere test per verificar il funzionamento del metodo setName
  def test_setName(self):
    self.dottore.setName("Paolo")
    self.assertEqual(self.dottore.getName(),"Paolo")
    self.dottore.setName(123) # Il nome inserito non è una stringa!
    self.assertEqual(self.dottore.getName(),"Paolo")  # non dovrebbe cambiare

  # Scrivere test per verificar il funzionamento del metodo setLastName
  def test_setlastName(self):
    self.dottore.setLastName("Picchiami")
    self.assertEqual(self.dottore.getLastname(),"Picchiami")
    self.dottore.setLastName(123) # Il cognome inserito non è una stringa!
    self.assertEqual(self.dottore.getLastname(),"Picchiami")  # non dovrebbe cambiare
  
  # Scrivere test per verificar il funzionamento del metodo setAge
  def test_setAge(self):
    self.dottore.setAge(55)
    self.assertEqual(self.dottore.getAge(), 55)
    self.dottore.setAge(3.5) # L'età deve essere un numero intero!
    self.assertEqual(self.dottore.getAge(), 55) # non dovrebbe cambiare

  # Scrivere test per verificar il funzionamento del metodo setSpecialization
  def test_setSpecialization(self):
    self.dottore.setSpecialization("di famiglia")
    self.assertEqual(self.dottore.getSpecialization(),"di famiglia")
  
  # Scrivere test per verificar il funzionamento del metodo setParcel
  def test_setParcel(self):
    self.dottore.setParcel(0.8)
    self.assertEqual(self.dottore.getParcel(), 0.8)
    self.dottore.setParcel(10)
    self.assertEqual(self.dottore.getParcel(), 0.8) # non dovrebbe cambiare

  # Scrivere test per isValidDoctor
  def test_isvalidDoctor(self):
    self.dottore.setAge(55)
    self.assertEqual(self.dottore.isAValidDoctor(), "Doctor Michele Fonte is valid!")
    self.dottore.setAge(25)
    self.assertEqual(self.dottore.isAValidDoctor(), "Doctor Michele Fonte is not valid!")

  # Scrivere test per greet
  def test_Greet(self):
    self.assertEqual(self.dottore.greet(),"Ciao, sono Michele Fonte! Ho 0 anni!")
    self.assertEqual(self.dottore.doctorGreet(),"Ciao, sono Michele Fonte! Ho 0 anni!\nSono un medico estetico")


if __name__ == "__main__":
    unittest.main()