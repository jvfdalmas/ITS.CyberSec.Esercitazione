from anagrama import anagram as ANAGRAM
import unittest

class TestAnagrama(unittest.TestCase):

    def test_anagrama(self):
        anagrama = ANAGRAM("calcario", "cariocal")
        self.assertEqual(anagrama, True, "the bool should return [TRUE]")

    def test_anagrama_false(self):
        anagrama = ANAGRAM("calcario", "calcariocalcario")
        self.assertEqual(anagrama, False, "the bool should return [False]")

if __name__ == "__main__":
    unittest.main()

    
