# Implementation document

## Project structure

![Class diagram](https://github.com/mizhonka/Spell-checker/blob/main/Documentation/class_diagram.png)

**index.py** contains the main function and takes user input.

The program contains 4 classes:

**FileManager** reads user input from files and replaces it with the corrected text.

**WordList** acts as a vocabulary. It can be used to checked if a given word exists.  

**DamerauLavenshtein** is used to calculate the Damerau-Lavenshtein distance between two words.

**SpellChecker** checks the user input using WordList, calls DamerauLavenshtein and gives correction suggestions.
