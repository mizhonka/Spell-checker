import unittest
from spell_checker import SpellChecker
from word_list import WordList
from tests.trie_stub import TrieStub


class TestSpellChecker(unittest.TestCase):
    def setUp(self):
        self.trie=TrieStub().trie

    def create_checker(self, data):
        checker=SpellChecker(data)
        checker._dictionary=self.trie
        checker._incorrect_words={}
        checker._get_incorrect_words()
        return checker

    def test_get_word_at(self):
        checker=self.create_checker("two words")
        self.assertEqual("two", checker.get_word_at((1, 3)))


