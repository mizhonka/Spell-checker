import unittest
from text_data import TextData


class TestTextData(unittest.TestCase):
    def test_text_data_gives_suggestion_for_incorrect_word(self):
        input="hello world asdf"
        data=TextData(input)
        corrections=data.get_suggestions()
        self.assertEqual(len(corrections), 1)
        self.assertTrue("asdf" in corrections)

    def test_distance_of_one_gets_corrected(self):
        input="fooo"
        data=TextData(input)
        corrections=data.get_suggestions()
        self.assertTrue("fooo" in corrections)
