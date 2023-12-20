from word_list import WordList

class TrieStub:
    def __init__(self):
        self.trie=WordList()
        self.words=["a", "re", "in", "inn", "rat", "ran", "rap"]
        for w in self.words:
            self.trie._insert(w)
