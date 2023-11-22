from damerau_levenshtein import DamerauLevenshtein
from word_list import WordList

class TextData:
    """
    This class stores the given text input and gives spelling suggestions for each word.

    Attributes:
        _words (list): List containing every word in the input data.
        _incorrect_words (list): List containing every misspelled word in the input data.
        _suggestions (dictionary): Dictionary containing a suggested word for every incorrect word.
        _dictionary (WordList): Instance of class WordList.

    """
    def __init__(self, data):
        """
        The constructor for TextData class.

        Parameters:
            data (string): Text input given by the user.

        """
        self._words=data.split()
        self._incorrect_words=[]
        self._dictionary=WordList()
        self._suggestions={}
        self._get_incorrect_words()

    def _get_incorrect_words(self):
        """
        Checks every word in self._words and fills self._incorrect_words.

        """
        for word in self._words:
            if not self._dictionary.look_up_word(word):
                self._incorrect_words.append(word)

    def get_suggestions(self):
        """
        Fills self._suggestions with spelling suggestions for incorrect words.

        Returns:
            self._suggestions (dictionary)

        """
        for wrong in self._incorrect_words:
            cur=("", -1)
            for word in self._dictionary.words:
                damLev=DamerauLevenshtein(wrong, word)
                distance=damLev.calculate_distance()
                if cur[1]<0 or distance<cur[1]:
                    cur=(word, distance)
                if cur[1]==1:
                    break
            self._suggestions[wrong]=cur[0]
        return self._suggestions






