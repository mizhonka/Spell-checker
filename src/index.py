from word_list import WordList
from damerau_levenshtein import DamerauLevenshtein


def main():
    dictionary = WordList()
    lb = "\n"
    while True:
        cmd = input(
            f"{lb}0 - Look up word {lb}1 - Calculate Damerau-Levenshtein Distance{lb}")
        try:
            cmd = int(cmd)
        except ValueError:
            break
        if cmd == 0:
            word = input("Enter a word: ")
            if dictionary.look_up_word(word):
                print("This word is spelt correctly")
            else:
                print("This word is spelt incorrectly")
        elif cmd == 1:
            word_a = input("Enter word 1: ")
            word_b = input("Enter word 2: ")
            dist = DamerauLevenshtein(word_a, word_b).calculate_distance()
            print(
                f"The smallest number of operations to turn {word_a} into {word_b} is {dist}")


if __name__ == "__main__":
    main()
