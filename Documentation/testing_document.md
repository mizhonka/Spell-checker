# Testing document

## Unit testing

[![codecov](https://codecov.io/gh/mizhonka/Spell-checker/graph/badge.svg?token=2QSRCPDGGL)](https://codecov.io/gh/mizhonka/Spell-checker)  
The following classes have been tested via Python unittest, and branch coverage can be seen on Codecov (click the badge above). Test and UI folders have been excluded.

### Test vocabulary

The following trie structure has been used in testing:  
![Trie diagram](https://github.com/mizhonka/Spell-checker/blob/main/Documentation/trie%20diagram.png)  
WordList instance contains the words 'a', 're', 'in', 'inn', 'rat', 'ran', 'rap'.

### WordList

The following features have been tested:

* Trie size (number of nodes) is correct.
* Trie contains every inserted word.
* look_up_word() function returns False if word doesn't exist (input string 'fake').
* form_list() function (reads words from a file) creates a trie and returns a correct amount of words.

### SpellChecker

The following features have been tested:

* SpellChecker gives appropriate suggestions (input string "cat e pars tins").
* get_word() function returns correct strings (input string "one two three", parameters (1,3), (5,3), (9,5)).
* get_text() function returns the correct string after a word has been replaced (input string 'cat')
* If a capitalized word gets replaced, it stays capitalized (input string 'Cat').
* If input contains only numbers and punctuation marks, it doesn't get corrected (input string '123!')

### DamerauLevenshtein

The Damerau-Levenshtein algortihm resulting in a correct distance has been tested with the following pairs of strings:
* 'treat', 'threats' (insertions)
* 'tryout', 'out' (removals)
* 'crash', 'brass' (substitutions)
* 'angel', 'angle' (transposition)
* 'kitten', 'sitting' (transposition, insertion)
* 'stack', 'taken' (all operations)


