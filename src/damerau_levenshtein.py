from string import ascii_lowercase


class DamerauLevenshtein:
    """
    This class calculates the Damerau–Levenshtein distance between 2 words.

    Attributes:
        word_a (string): First (starting) word.
        word_b (string): Second (target) word.
    """

    def __init__(self, word_a, word_b):
        """
        The constructor for class DamerauLevenshtein.

        Parameters:
            word_a (string): First (starting) word.
            word_b (string): Second (target) word.
        """
        self.word_a = word_a.lower()
        self.word_b = word_b.lower()
        self.grid = {}

    def _create_grid(self, a, b):
        """
        Creates a correct size grid for calculating the distance.

        Parameters:
            a (int): Length of word_a.
            b (int): Length of word_b.

        Returns:
            g (dictionary): Dictionary with tuple-coordinates (-1...a, -1...b) as keys.
        """
        coords = []
        t = (0, 0)
        for x in range(-1, a+1):
            for y in range(-1, b+1):
                t = (x, y)
                coords.append(t)
        g = dict.fromkeys(coords, 0)
        return g

    def _form_alphabet(self):
        """
        Creates a list of characters that are allowed in words.

        Returns:
            alphabet (list): The chosen list.
        """
        alphabet = list(ascii_lowercase)
        alphabet.append("-")
        return alphabet

    def calculate_distance(self):
        """
        Calculates the Damerau–Levenshtein distance.

        Returns:
            distance (int): The calculated distance.
        """
        len_a, len_b = len(self.word_a), len(self.word_b)
        maxdist = len_a+len_a
        # dictionary with English letters as keys
        alpha = dict.fromkeys(self._form_alphabet(), 0)
        self.grid = self._create_grid(len_a, len_b)
        self.grid[(-1, -1)] = maxdist
        for i in range(len_a+1):
            self.grid[(i, -1)] = maxdist
            self.grid[(i, 0)] = i
        for i in range(len_b+1):
            self.grid[(-1, i)] = maxdist
            self.grid[(0, i)] = i
        for i in range(1, len_a+1):
            tp = 0
            for j in range(1, len_b+1):
                k = alpha[self.word_b[j-1]]
                l = tp
                if self.word_a[i-1] == self.word_b[j-1]:
                    dist = 0
                    tp = j
                else:
                    dist = 1
                self.grid[(i, j)] = min(self.grid[(i-1, j)]+1,  # delete
                                        self.grid[(i, j-1)]+1,  # insert
                                        self.grid[(i-1, j-1)] + \
                                        dist,  # substitute
                                        self.grid[(k-1, l-1)] + (i-k-1) + 1 + (j-l-1))  # transpose
            alpha[self.word_a[i-1]] = i
        return self.grid[(len_a, len_b)]
