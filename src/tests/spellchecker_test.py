import unittest
from word_list import WordList

class TestSpellchecker(unittest.TestCase):
    def setUp(self):
        self.dictionary=WordList()

    def test_word_list_exists(self):
        self.assertIsNotNone(self.dictionary.words)
