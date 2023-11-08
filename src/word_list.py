class WordList:
    def __init__(self):
        self.words=[]
        with open("src/words.txt") as w:
            for row in w:
                row=row.replace("\n", "")
                self.words.append(row)

    def look_up_word(self, word):
        if word in self.words:
            return True
        return False
