import unittest
from word_list import WordList


class TestWordList(unittest.TestCase):
    def setUp(self):
        self.dictionary = WordList()
        self.dictionary.form_list()
        self.words=["a", "re", "in", "inn", "rat", "ran", "rap"]
        self.trie=self.create_trie()

    def create_trie(self):
        trie=WordList()
        for w in self.words:
            trie._insert(w)
        return trie

    def test_trie_size_is_correct(self):
        self.assertEqual(self.trie.size, 11)

    def test_trie_contains_words(self):
        isFound=True
        for w in self.words:
            if not self.trie.look_up_word(w):
                isFound=False
                break
        self.assertTrue(isFound)

    def test_word_list_exists(self):
        self.assertIsNotNone(self.dictionary.words)

    def test_word_list_real_word_returns_true(self):
        self.assertTrue(self.dictionary.look_up_word("hello"))

    def test_word_list_fake_word_returns_false(self):
        self.assertFalse(self.dictionary.look_up_word("asdf"))
