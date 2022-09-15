import unittest
import translator as tr

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(tr.english_to_french('Hello'),'Bonjour')
        self.assertIsNone(tr.english_to_french(''), '')
        
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(tr.french_to_english('Bonjour'),'Hello')
        self.assertIsNone(tr.french_to_english(''), '')

unittest.main()