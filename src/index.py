from text_data import TextData


def main():
    text=input("Input text to be checked: ")
    data=TextData(text)
    corrections=data.get_suggestions()
    print("The following words were spelled incorrectly")
    for word, correction in corrections.items():
        print(f"{word} (did you mean '{correction}'?)")



if __name__ == "__main__":
    main()
