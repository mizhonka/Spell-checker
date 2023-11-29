# Week 4 Report

**Hours used:** 5

## What I did

Mostly finished core functionality. Created new classes FileManager (for reading user input from files) and SpellChecker (for handling user input and giving spelling suggestions).

Created poetry tasks for running the main program, pylint and unit testing.

Updated the testing document and started working on the implementation document.

## How has the project progressed?

The program can be run with command _poetry run invoke start_.

The user can either write text directly through command line or give a file path to a text file.

The program will then check the user input for incorrect words. If any mistakes exist, the program will give correction suggestions, which the user can either accept or skip.

Accepted corrections will be applied and the corrected text will be printed out. If the user passed a file, the file will be overwritten with the corrected text.

## What I learned this week

Learned to replace _for i in range 0, len()_ structure with enumerate, since pylint suggested it. Also reminded myself how to use poetry tasks and draw class diagrams.

## What has been unclear or problematic?

What do I do if my input contains numbers or punctuation? I realized that some of the words in the vocabulary contain hyphens, which I decided to include when correcting words. Periods and commas are easy enought to replace with blanks when they are located at the end of the word, so maybe I should just ignore words that contain any weird characters in the middle.

## What next?

Next I will be implementing a trie data structure for my vocabulary.
