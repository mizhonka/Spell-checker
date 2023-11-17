# Week 3 Report

**Hours used in total:** 11

## What I did

This week I looked through coding examples and figured out the logic behind the Damerau-Levenshtein algorithm. I implemented a working algorithm into my program and also made a simple main program to test these features. As usual I made sure my project has full test coverage and code quality is checked with pylint.  

Started working on a testing document.

## How has the project progressed?

The class DamerauLevenshtein now has a working function to calculate the distance between two words.

Via command line (execute _python src/index.py_) the user can  
1. Test whether a given word is "correct" (exists in the vocabulary)
2. Calculate the Damerau-Levenshtein distance between two words (the smallest number of operations to turn word1 into word2)

## What I learned this week

I _almost_ fully understand how the Damerau-Levenshtein algorithm works. I also got more comfortable with using list declaration in Python.

## What has been unclear or problematic?

The Damerau-Levenshtein algorithm is more complicated than I thought. The regular optimal string alignment algorithm was easy enough to understand when I went through it step by step, but many code examples I studied didn't include adjacent transpositions. I did find full pseudocode on Wikipedia and kinda just went with it.

## What next?

Next I will be working on a somewhat functional spell checker, that combines my current features and gives word suggestions.
