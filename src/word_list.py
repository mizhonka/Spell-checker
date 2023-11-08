class WordList:
    def __init__(self):
        self.words=[]
        with open("words") as w:
            for row in w:
                row=row.replace("\n", "")
                self.words.append(row)

    def look_up_word(self, word):
        if word in self.words:
            return f"'{word}' is a real word"
        return f"'{word}' is NOT a real word"
