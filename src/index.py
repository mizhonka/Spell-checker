from word_list import WordList

def main():
    dictionary=WordList()
    print(dictionary.look_up_word("cat"))
    print(dictionary.look_up_word("asdfg"))

if __name__=="__main__":
    main()
