from word_list import WordList
from damerau_levenshtein import DamerauLevenshtein


def main():
    a="CA"
    b="ABC"
    dictionary = WordList()
    dam_lev=DamerauLevenshtein(a, b)
    print(dam_lev.calculate_distance())


if __name__ == "__main__":
    main()
