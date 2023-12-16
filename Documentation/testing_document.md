# Testing document

## Unit testing

![codecov](https://codecov.io/gh/mizhonka/Spell-checker/graph/badge.svg?token=2QSRCPDGGL)  
The following classes have been tested via Python unittest, and branch coverage can be seen on Codecov (click the badge above). Test and UI folders have been excluded.

### WordList

Using the same vocabulary as the program, the following features have been tested:
* WordList instance exists
* Real word returns true (input string 'hello')
* Fake work returns false (input string 'asdf')

In addition the following trie structure has been tested:
![Trie diagram](https://github.com/mizhonka/Spell-checker/blob/main/Documentation/trie%20diagram.png)
* Trie size (number of nodes) is correct
* Trie contains the selected words (input strings 'a', 're', 'in', 'inn', 'rat', 'ran', 'rap')

### DamerauLevenshtein

The Damerau-Levenshtein algortihm resulting in a correct distance has been tested with the following pairs of strings:
* 'treat', 'threats' (insertions)
* 'tryout', 'out' (removals)
* 'crash', 'brass' (substitutions)
* 'angel', 'angle' (transposition)
* 'kitten', 'sitting' (transposition, insertion)
* 'stack', 'taken' (all operations)


