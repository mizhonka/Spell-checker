import unittest
from word_list import WordList
from damerau_levenshtein import DamerauLevenshtein


class TestSpellchecker(unittest.TestCase):
    def setUp(self):
        self.dictionary = WordList()
        self.dam_lev = DamerauLevenshtein("hello", "world")

    def test_word_list_exists(self):
        self.assertIsNotNone(self.dictionary.words)

    def test_word_list_real_word_returns_true(self):
        self.assertTrue(self.dictionary.look_up_word("hello"))

    def test_word_list_fake_word_returns_false(self):
        self.assertFalse(self.dictionary.look_up_word("asdf"))

    def test_dam_lev_empty_grid_on_init(self):
        self.assertEqual(self.dam_lev.grid, [])

    def test_dam_lev_word_lenghts_correct(self):
        self.assertEqual(self.dam_lev.len_a, 5)
        self.assertEqual(self.dam_lev.len_b, 5)

    def test_dam_lev_grid_size_correct(self):
        self.dam_lev.calculate_distance()
        self.assertEqual(len(self.dam_lev.grid), 6)
        self.assertEqual(len(self.dam_lev.grid[0]), 6)
