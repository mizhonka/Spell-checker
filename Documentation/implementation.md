# Implementation document

## Project structure

![Class diagram](https://github.com/mizhonka/Spell-checker/blob/main/Documentation/class_diagram.png)

**index.py** contains the main function and takes user input.

The program contains 4 classes:

**FileManager** reads user input from files and replaces it with the corrected text.

**WordList** acts as a vocabulary. It can be used to checked if a given word exists.

**DamerauLevenshtein** is used to calculate the Damerau-Levenshtein distance between two words.

**SpellChecker** checks the user input using WordList, calls DamerauLevenshtein and gives correction suggestions.

## Time complexity

### Damerau-Levenshtein algorithm

[Pseudocode example](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance#Distance_with_adjacent_transpositions)

The algorithm calculates the Damerau-Levenshtein distance with adjacent transpositions. In the worst case the time complexity is O(N * M), where N and M are the string lenghts.

## Use of large language models

No large language models (such as ChatGPT) have been used in this project.

## Sources

https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
