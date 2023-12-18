import unittest
from damerau_levenshtein import DamerauLevenshtein


class TestDamerauLevenshtein(unittest.TestCase):
    def test_distance_with_insertions(self):
        dam_lev = DamerauLevenshtein("treat", "threats")
        dist = dam_lev.calculate_distance()
        self.assertEqual(dist, 2)

    def test_distance_with_deletions(self):
        dam_lev = DamerauLevenshtein("tryout", "out")
        dist = dam_lev.calculate_distance()
        self.assertEqual(dist, 3)

    def test_distance_with_substitutions(self):
        dam_lev = DamerauLevenshtein("crash", "brass")
        dist = dam_lev.calculate_distance()
        self.assertEqual(dist, 2)

    def test_distance_with_transpositions(self):
        dam_lev = DamerauLevenshtein("angel", "angle")
        dist = dam_lev.calculate_distance()
        self.assertEqual(dist, 1)

    def test_distance_with_combinations_a(self):
        dam_lev = DamerauLevenshtein("kitten", "sitting")
        dist = dam_lev.calculate_distance()
        self.assertEqual(dist, 3)

    def test_distance_with_combinations_b(self):
        dam_lev = DamerauLevenshtein("stack", "taken")
        dist = dam_lev.calculate_distance()
        self.assertEqual(dist, 4)
