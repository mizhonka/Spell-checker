import unittest
from word_list import WordList


class TestSpellchecker(unittest.TestCase):
    def setUp(self):
        self.dictionary = WordList()

    def test_word_list_exists(self):
        self.assertIsNotNone(self.dictionary.words)

    def test_word_list_real_word_returns_true(self):
        self.assertTrue(self.dictionary.look_up_word("hello"))

    def test_word_list_fake_word_returns_false(self):
        self.assertFalse(self.dictionary.look_up_word("asdf"))
