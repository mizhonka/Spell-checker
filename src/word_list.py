class WordList:
    """
    This class handles a list of words in the vocabulary.

    Attributes:
        words (list): The list containing the existing words.

    """

    def __init__(self):
        """
        The constructor for WordList class.

        """
        self.words = []
        self.form_list()

    def form_list(self):
        """
        Reads the words.txt file and adds the words to a list.

        """
        with open("src/words.txt", encoding="utf-8") as w:
            for row in w:
                row = row.replace("\n", "")
                self.words.append(row)

    def look_up_word(self, word):
        """
        Checks if a given word exists in the word list.

        Parameters:
            word (string): The word to be checked.

        Returns:
            True (boolean): If the word exists.
            False (boolean): If the word doesn't exist.

        """
        if word in self.words:
            return True
        return False
