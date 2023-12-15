import unittest
from damerau_levenshtein import DamerauLevenshtein


class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.dam_lev = DamerauLevenshtein("aui", "uia")

    def test_dam_lev_distance_is_correct(self):
        dist = self.dam_lev.calculate_distance()
        self.assertEqual(dist, 2)

    # testaa suppealla sanastolla
    # selvitä kumpaa laskentatapaa käytetään
    # testaa eri keinoja käyttäviä muutoksia
