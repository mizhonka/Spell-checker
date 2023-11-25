from spell_checker import SpellChecker
from file_manager import FileManager


def handle_corrections(corrections, checker, file):
    done = 0
    print("The following words were spelled incorrectly: \n")
    for index, correction in corrections.items():
        wrong = checker.get_word_at(index)
        cmd = int(input(
            f"'{wrong}' (did you mean '{correction}'?) \n 1 - Accept correction \n 2 - Skip \n"))
        if cmd == 1:
            checker.correct(index, correction)
            done += 1
            print(f"'{wrong}' was replaced with '{correction}'\n")
        elif cmd == 2:
            print(f"Skipped '{wrong}'\n")
    corrected_text = checker.get_text()
    if done and file:
        file.write_file(corrected_text)
    print(f"{done} corrections were made\n")
    print(corrected_text)


def get_data(cmd):
    file=None
    if cmd == 1:
        text = input("Input text: ")
    elif cmd == 2:
        path = input("Input file path: ")
        file = FileManager(path)
        text = file.read_file()
    return text, file


def main():
    while True:
        cmd = int(input("1 - Type text\n2 - Enter file path\n3 - Exit\n"))
        if cmd in (1, 2):
            text, file = get_data(cmd)
            if not text:
                continue
        elif cmd == 3:
            break
        checker = SpellChecker(text)
        corrections = checker.get_suggestions()
        if len(corrections):
            handle_corrections(corrections, checker, file)
            break
        print("There are no spelling errors, yay!")
        break


if __name__ == "__main__":
    main()
