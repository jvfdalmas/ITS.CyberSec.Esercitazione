### Creazione di Test Case con UnitTest
"""Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
Istruzioni
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Persona
- Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
- Scrivere test per verificare:
  - L'inizializzazione corretta degli attributi first_name, last_name e age.
  - Il funzionamento dei metodi setName, setLastName e setAge."""

import unittest
from persona import Persona

# Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
class TestPersona(unittest.TestCase):
    
  # Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome
  def setUp(self):
    self.persona = Persona(first_name = "Marco", last_name = "Cascio")
  
  # Scrivere test per verificare l'inizializzazione corretta degli attributi first_name, last_name e age
  def test_init_first_name(self):
    persona = Persona(first_name = 123, last_name = "Cascio")
    self.assertIsNone(persona.getName())
    self.assertEqual(persona.getLastname(), "Cascio")
    self.assertIsNone(persona.getAge())

  def test_init_last_name(self):
    persona = Persona(first_name = "Marco", last_name = 1)
    self.assertIsNone(persona.getLastname())
    self.assertEqual(persona.getName(), "Marco")
    self.assertIsNone(persona.getAge())
  
  def test_init_age(self):
    self.assertEqual(self.persona.getAge(), 0)
  
  # Scrivere test per verificar il funzionamento del metodo setName
  def test_setName(self):
    self.persona.setName("Paolo")
    self.assertEqual(self.persona.getName(),"Paolo")
    self.persona.setName(123) # Il nome inserito non è una stringa!
    self.assertEqual(self.persona.getName(),"Paolo")  # non dovrebbe cambiare

  # Scrivere test per verificar il funzionamento del metodo setLastName
  def test_setlastName(self):
    self.persona.setLastName("Picchiami")
    self.assertEqual(self.persona.getLastname(),"Picchiami")
    self.persona.setLastName(123) # Il cognome inserito non è una stringa!
    self.assertEqual(self.persona.getLastname(),"Picchiami")  # non dovrebbe cambiare
  
  # Scrivere test per verificar il funzionamento del metodo setAge
  def test_setAge(self):
    self.persona.setAge(35)
    self.assertEqual(self.persona.getAge(), 35)
    self.persona.setAge(3.5) # L'età deve essere un numero intero!
    self.assertEqual(self.persona.getAge(), 35) # non dovrebbe cambiare

  # Scrivere test per greet
  def test_Greet(self):
    self.assertEqual(self.persona.greet(),"Ciao, sono Marco Cascio! Ho 0 anni!")


if __name__ == "__main__":
    unittest.main()
