# Testing document

## Unit testing

[![codecov](https://codecov.io/gh/mizhonka/Spell-checker/graph/badge.svg?token=2QSRCPDGGL)](https://codecov.io/gh/mizhonka/Spell-checker)
The following classes have been tested via Python unittest, and branch coverage can be seen on Codecov (click the badge above). Test and UI folders have been excluded.

### WordList

The following features have been tested using this trie:
![Trie diagram](https://github.com/mizhonka/Spell-checker/blob/main/Documentation/trie%20diagram.png)
* Trie size (number of nodes) is correct.
* Trie contains the selected words (input strings 'a', 're', 'in', 'inn', 'rat', 'ran', 'rap').
* look_up_word() function returns False if word doesn't exist (input string 'fake').
* form_list() function (reads words from a file) creates a trie and returns a correct amount of words.

### DamerauLevenshtein

The Damerau-Levenshtein algortihm resulting in a correct distance has been tested with the following pairs of strings:
* 'treat', 'threats' (insertions)
* 'tryout', 'out' (removals)
* 'crash', 'brass' (substitutions)
* 'angel', 'angle' (transposition)
* 'kitten', 'sitting' (transposition, insertion)
* 'stack', 'taken' (all operations)


