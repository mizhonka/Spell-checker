# Project specification

## Summary

This spell checker will check for misspellings in a given text and recommend corrections by utilizing the Damerau–Levenshtein distance.

## Basic information

Programming language to be used is Python.  

The documentation, programming and the program itself (including the vocabulary) will all be in English.  

My degree programme is *tietojenkäsittelytieteen kandidaatti (TKT)*.

## Input / Output

* The program will receive a text file as input and read it as a string
* It will one by one output a misspelled word and correction suggestions. The user is then asked for input on which correction should be used or skip the word
* The program will then output a corrected version of the text file (if any changes were made)

## Data structures and algorithms

Similarly to [Ispell](https://www.cs.hmc.edu/~geoff/ispell.html), this spell checker will recommend corrections that are based on a Damerau–Levenshtein distance of 1. This means that it will only 
suggest similar words that can be edited from the original word with one operation (insertion, deletion, substitution or transposition). This type of spell checker isn't 'perfect', but according
to Damerau 80% of spelling errors are a result of one mistake in one of the four previously mentioned cases.

The vocabulary will be stored as a trie structure.

When the program gets a word as an input, it will check whether the word is found in its vocabulary. The time complexity of this is O(n), where n is the length of the word.  

If the word is found in the vocabulary, there is no need for correction.

If the word is not found in the vocabulary, the algorithm will look for words that have a Damerau–Levenshtein distance of one. The time complexity of calculating the distance between two words is
excepted to be O(nm), where n and m are the lengths of these words. (Since we are looking for words with the distance of 1, m can only be n, n-1 or n+1)

## Sources

https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance  
https://en.wikipedia.org/wiki/Ispell  
https://www.geeksforgeeks.org/trie-insert-and-search/



