# Testing document

## Unit testing

[![codecov](https://codecov.io/gh/mizhonka/Spell-checker/graph/badge.svg?token=2QSRCPDGGL)](https://codecov.io/gh/mizhonka/Spell-checker)  
The following classes have been tested via Python unittest, and branch coverage can be seen on Codecov (click the badge above)

### WordList

**test_word_list_exists**: list initialized is not none  

**test_word_list_real_word_returns_true**: real word returns true (tested with input string 'hello')  

**test_word_list_fake_word_returns_false**: fake word return false (tested with input string 'asdf')  

### DamerauLevenshtein

**test_dam_lev_distance_is_correct**: Damerau-Levenshtein distance is calculated correctly (tested with input strings 'CA' and 'ABC')

### SpellChecker

**test_spell_checker_gives_suggestion_for_incorrect_word**: SpellChecker gives a right amount of corrections for the right words (tested with input string 'hello world asdf')  

**test_distance_of_one_gets_corrected**: SpellChecker gives a correction when incorrect word has a DamerauLevenshtein distance of 1 with another word (tested with input string 'fooo')  

**test_get_word_at_returns_correct_word**: SpellChecker function _get_word_at(index)_ returns the right word (tested with input string 'one two three')  

**test_correct_changes_word**: SpellChecker function _correct(index, correction)_ changes the right word (tested with input string 'onn')  

**test_get_text_returns_correct_text**: SpellChecker function _get_text()_ returns the right string (tested with input string 'one two three')  

### FileManager

**test_file_manager_returns_text_with_existing_file**: FileManager returns file content as string when the file exists (tested with file _testfile.txt_ inside the _tests_ folder)   

**test_file_manager_returns_none_with_non_existing_file**: FileManager returns _None_ when trying to read a non-existing file (tested with fake file path 'doesnotexist.txt')  

**test_file_manager_writes_file**: FileManager changes file content to given input (tested with input 'four five six' with testfile.txt)


