import unittest
from spell_checker import SpellChecker
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

    def test_give_corrections(self):
        misspelled_data="cat e pars tins"
        checker=self.create_checker(misspelled_data)
        suggestions=[s for i, s in checker.get_suggestions().items()]
        self.assertEqual(suggestions, ["rat", "a", "a", "in"])

    def test_get_word(self):
        data="one two three"
        checker=self.create_checker(data)
        result=checker.get_word_at((1, 3))
        self.assertEqual(result, "one")
        result=checker.get_word_at((5, 3))
        self.assertEqual(result, "two")
        result=checker.get_word_at((9, 5))
        self.assertEqual(result, "three")

    def test_get_text_after_correcting(self):
        misspelled_data="cat"
        checker=self.create_checker(misspelled_data)
        suggestion=[(i,s) for i,s in checker.get_suggestions().items()][0]
        checker.correct(suggestion[0], suggestion[1])
        self.assertEqual("rat", checker.get_text())

    def test_word_stays_capitalized(self):
        misspelled_data="Cat"
        checker=self.create_checker(misspelled_data)
        suggestion=[s for i,s in checker.get_suggestions().items()][0]
        self.assertEqual("Rat", suggestion)

    def test_input_with_no_letters(self):
        data="123!"
        checker=self.create_checker(data)
        self.assertEqual({}, checker._incorrect_words)





