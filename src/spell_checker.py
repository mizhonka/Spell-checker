from string import punctuation
from damerau_levenshtein import DamerauLevenshtein
from word_list import WordList


class SpellChecker:
    """
    This class stores the given text input and gives spelling suggestions for each word.

    Attributes:
        _words (list): List containing every word in the input data.
        _extras (dictionary): Dictionary containing numbers and punctuation, that are ignored by the algorithm.
        _incorrect_words (dictionary): Dictionary containing every incorrect word and it's index.
        _suggestions (dictionary): Dictionary containing a suggested word for every incorrect word.
        _dictionary (WordList): Instance of class WordList.

    """

    def __init__(self, data):
        """
        The constructor for SpellChecker class.

        Parameters:
            data (string): Text input given by the user.

        """
        self._words = data.split()
        self._extras = {}
        self._get__extras()
        self._incorrect_words = {}
        self._dictionary = WordList()
        self._suggestions = {}
        self._get_incorrect_words()

    def _get__extras(self):
        """
        Fills a dictionary with characters that are ignored by the spell checker.

        """
        keys = [ord(p) for p in punctuation]
        keys.remove(ord("-"))
        for n in range(10):
            keys.append(ord(str(n)))
        self._extras = dict.fromkeys(keys, "")

    def _strip_characters(self, word):
        """
        Removes any punctuation or numbers from given word.

        Parameters:
            word (string): Word to be stripped.

        Returns:
            (string): Stripped word.

        """
        stripped=word.translate(self._extras)
        return stripped

    def _get_incorrect_words(self):
        """
        Checks every word in self._words and fills self._incorrect_words.

        """
        for i, word in enumerate(self._words):
            stripped = self._strip_characters(word)
            if not stripped:
                continue
            if not self._dictionary.look_up_word(stripped):
                self._incorrect_words[stripped] = i

    def get_suggestions(self):
        """
        Fills self._suggestions with spelling suggestions for incorrect words.

        Returns:
            self._suggestions (dictionary)

        """
        for wrong, index in self._incorrect_words.items():
            cur = ("", -1)
            for word in self._dictionary.get_words():
                dam_lev = DamerauLevenshtein(wrong, word)
                distance = dam_lev.calculate_distance()
                if cur[1] < 0 or distance < cur[1]:
                    cur = (word, distance)
                if cur[1] == 1:
                    break
            self._suggestions[index] = cur[0]
        return self._suggestions

    def get_word_at(self, index):
        """
        Returns a word from self._words at given index.

        Parameters:
            index (int): Given index.

        Returns:
            (string): Matching word.

        """
        return self._words[index]

    def correct(self, index, correction):
        """
        Replaces a word in self._words with a corrected word.

        Parameters:
            index (int): List position for the word to be changed.
            correction (string): Corrected word.

        """
        self._words[index] = correction

    def get_text(self):
        """
        Turns words into a string.

        Returns:
            (string): self._words as a string.

        """
        return " ".join(self._words)
