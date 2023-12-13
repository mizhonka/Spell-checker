from string import ascii_lowercase


class TrieNode:
    """
    This class acts as a node for trie.

    Attributes:
        children (list): Children of this node.
        is_end_of_word (boolean): True if this node is the last letter of a word, else False.

    """

    def __init__(self):
        """
        The constructor for TrieNode class.

        """
        self.children = [None]*27
        self.is_end_of_word = False


class WordList:
    """
    This class contains a trie structure of words in the vocabulary.

    Attributes:
        words (TrieNode): Root trie node containing the existing words.

    """

    def __init__(self):
        """
        The constructor for WordList class.

        """
        self.words = TrieNode()
        self.form_list()

    def _get_index(self, ch):
        """
        Finds the index of a letter in the English alphabet.

        Returns:
            (int) Index.

        """
        if ch == "-":
            return 26
        return ord(ch)-ord("a")

    def _get_letter(self, n):
        """
        Finds a letter with its index.

        Returns:
            (str) Letter.

        """
        if n == 26:
            return "-"
        return ascii_lowercase[n]

    def _insert(self, word):
        """
        Inserts a new word into the trie structure.

        Parameters:
            word (string): Word to be inserted.

        """
        cur = self.words
        length = len(word)
        for i in range(length):
            index = self._get_index(word[i])
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_end_of_word = True

    def _search(self, node, word, result):
        """
        Performs a depth-first search.

        Parameters:
            node (TrieNode): Current node.
            word (string): Current word.
            result (list): Words collected.

        Returns:
            result (list): Words collected.

        """
        for n in range(0, 27):
            child = node.children[n]
            if child:
                new_word = word+self._get_letter(n)
                if child.is_end_of_word:
                    result.append(new_word)
                result = self._search(child, new_word, result)
        return result

    def get_words(self):
        """
        Gets all words in the trie using DFS:

        Returns:
            (list): Found words.

        """
        return self._search(self.words, "", [])

    def form_list(self):
        """
        Reads words.txt file and inserts the words.

        """
        with open("src/static/words.txt", encoding="utf-8") as w:
            for row in w:
                row = row.replace("\n", "")
                self._insert(row.lower())

    def look_up_word(self, word):
        """
        Checks if a given word exists in the trie structure.

        Parameters:
            word (string): Word to be checked.

        Returns:
            True (boolean): If the word exists.
            False (boolean): If the word doesn't exist.

        """
        cur = self.words
        length = len(word)
        for i in range(length):
            index = self._get_index(word[i])
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur.is_end_of_word
