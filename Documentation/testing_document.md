# Testing document

## Unit testing

[![codecov](https://codecov.io/gh/mizhonka/Spell-checker/graph/badge.svg?token=2QSRCPDGGL)](https://codecov.io/gh/mizhonka/Spell-checker)  
The following classes have been tested via Python unittest, and branch coverage can be seen on Codecov (click the badge above)

### WordList

**test_word_list_exists**: checks that the list initialized is not none  
**test_word_list_real_word_returns_true**: checks that a real word returns true (tested with input string 'hello')
**test_word_list_fake_word_returns_false**: checks than a fake word return false (tested with input string 'asdf')

### DamerauLevenshtein

**test_dam_lev_distance_is_correct**: checks that Damerau-Levenshtein distance is calculated correctly (tested with input strings 'CA' and 'ABC')

