import unittest
from tests.trie_stub import TrieStub
from word_list import WordList


class TestWordList(unittest.TestCase):
    def setUp(self):
        self.stub=TrieStub()

    def test_trie_size_is_correct(self):
        self.assertEqual(self.stub.trie.size, 11)

    def test_trie_contains_words(self):
        isFound = True
        for w in self.stub.words:
            if not self.stub.trie.look_up_word(w):
                isFound = False
                break
        self.assertTrue(isFound)

    def test_trie_does_not_contain_word(self):
        self.assertFalse(self.stub.trie.look_up_word("fake"))

    def test_form_list_from_file(self):
        dictionary=WordList()
        dictionary.form_list()
        self.assertEqual(10010, len(dictionary.get_words()))
