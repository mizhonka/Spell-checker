import unittest
from spell_checker import SpellChecker


class TestSpellChecker(unittest.TestCase):
    def test_spell_checker_gives_suggestion_for_incorrect_word(self):
        input = "hello world asdf"
        checker = SpellChecker(input)
        corrections = checker.get_suggestions()
        self.assertEqual(len(corrections), 1)
        self.assertTrue("asdf" in checker._incorrect_words)

    def test_distance_of_one_gets_corrected(self):
        input = "fooo"
        checker = SpellChecker(input)
        corrections = checker.get_suggestions()
        self.assertEqual(len(corrections), 1)
        self.assertTrue("fooo" in checker._incorrect_words)

    def test_get_text_returns_correct_text(self):
        input = "one two three"
        checker = SpellChecker(input)
        str_form = checker.get_text()
        self.assertEqual(input, str_form)

    def test_input_without_letters_gives_no_corrections(self):
        input = "123!"
        checker = SpellChecker(input)
        corrections = checker.get_suggestions()
        self.assertEqual(len(corrections), 0)
        self.assertTrue(input not in checker._incorrect_words)
