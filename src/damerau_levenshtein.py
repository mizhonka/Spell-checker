class DamerauLevenshtein:
    """
    This class calculates the Damerau–Levenshtein distance between 2 words.

    Attributes:
        len_a (int): Length of the first (starting) word.
        len_b (int): Length of the second (target) word.
    """

    def __init__(self, word_a, word_b):
        """
        The constructor for class DamerauLevenshtein.

        Parameters:
            word_a (string): First (starting) word.
            word_b (string): Second (target) word.
        """
        self.len_a=len(word_a)
        self.len_b=len(word_b)

    def calculate_distance(self):
        """
        Calculates the Damerau–Levenshtein distance.

        Returns:
            distance (int): The calculated distance.
        """
        #self.grid=[[0]*self.len_b+1 for _ in range(self.len_a+1)]
        row=[0]*(self.len_b+1)
        self.grid=[row]*(self.len_a+1)
        for i in range(self.len_a+1):
            self.grid[i][0]=i
        for i in range(self.len_b+1):
            self.grid[0][i]=i
