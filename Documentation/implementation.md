# Implementation document

## Project structure

![Class diagram](https://github.com/mizhonka/Spell-checker/blob/main/Documentation/project_structure.png)

**index.py** contains the main function.

The program contains 5 classes:

**UI** creates a Tkinter gui.  

**MainView** contains and controls all of the ui elements.

**WordList** acts as a vocabulary. It can be used to check if a given word exists.

**DamerauLevenshtein** is used to calculate the Damerau-Levenshtein distance between two words.

**SpellChecker** checks the user input using WordList, calls DamerauLevenshtein and gives correction suggestions.

## Time complexity

### Damerau-Levenshtein algorithm

[Pseudocode example](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance#Distance_with_adjacent_transpositions)

The algorithm calculates the Damerau-Levenshtein distance with adjacent transpositions. In the worst case the time complexity is O(N * M), where N and M are the string lenghts.  

### Trie structure

[Pseudocode for insertion](https://en.wikipedia.org/wiki/Trie#Insertion)  

[Pseudocode for searching](https://en.wikipedia.org/wiki/Trie#Searching)

The vocabulary is read from a text file, then stored in a trie.  
The time complexity for both searching and inserting is O(D * M), where D is the size of the alphabet (in this case 27) and M is the length of the chosen string.  

### Flaws and improvements

The way the program handles numbers and punctuation is a bit unclear at the moment. For example, if two words would be joined with...periods, they would be recognized as one word.

The trie structure and Damerau-Levenshtein algorithm could be optimized to calculate the distance while going through the trie, and then returning back if no shorter distance is found.

In terms of code quality, the UI and MainView classes could be implemented better. I orginally meant to have multiple views in the gui, hence I seperated the "main" view in its own class.

## Use of large language models

No large language models (such as ChatGPT) have been used in this project.

## Sources

https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance  
https://en.wikipedia.org/wiki/Trie
