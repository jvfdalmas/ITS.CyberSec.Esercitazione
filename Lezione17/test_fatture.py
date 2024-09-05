### Creazione di Test Case con UnitTest
"""Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
Istruzioni
Creare un nuovo file Python denominato "test_persona.py".
Importare il modulo unittest e tutte le classi definite.

Test della Classe Fattura
- Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
- Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
- Scrivere test per verificare:
  - L'inizializzazione corretta della classe Fattura.
  - Il calcolo corretto del salario e del numero di fatture.
  - L'aggiunta e la rimozione di pazienti dalla lista."""

import unittest
from paziente import Paziente
from dotttore import Dottore
from fatture import Fattura

class TestFatture(unittest.TestCase):
  
  def setUp(self):
     self.dottore = Dottore("Michele", "Fonte", "generale", 0.8)
     self.pazziente1 = Paziente("Simone", "Antonelli", "PZ001")
     self.pazziente2 = Paziente("Marco", "Cascio", "PZ002")
     self.pazziente3 = Paziente("Angelo", "Locarini", "PZ003")
     self.pazzienti = [self.pazziente1, self.pazziente2, self.pazziente3]
     self.fatture = Fattura(self.pazzienti, self.dottore)
     self.pazziente4 = Paziente("Giuseppe", "Mosca", "PZ004")

  # Scrivere test per verificar il funzionamento del metodo Getsalary
  def test_getSalary(self):
     self.assertAlmostEqual(self.fatture.getSalary(), 2.4)

  # Scrivere test per verificar il funzionamento del metodo Getfatture
  def test_getFatture(self):
     self.assertEqual(self.fatture.getFatture(), 3)

  # Scrivere test per verificar il funzionamento del metodo add_patient
  def test_addPatient(self):
     self.assertEqual(self.fatture.addPatient(self.pazziente4), "Alla lista del Dottor Fonte è stato aggiunto il paziente PZ004")
     self.assertEqual(self.pazzienti[-1], self.pazziente4)

  # Scrivere test per verificar il funzionamento del metodo remove_patient
  def test_removePatient(self):
     self.fatture.addPatient(self.pazziente4)
     self.assertEqual(self.fatture.removePatient(self.pazziente4), "Alla lista del Dottor Fonte è stato rimosso il paziente PZ004")
     self.assertNotIn(self.pazziente4, self.pazzienti)

if __name__ == "__main__":
    unittest.main()