# Week 2 Report

**Hours used in total:** 7

## What I did

This week I implemented a simple class for vocabulary. I also started implementing an algorithm for calculating the Damerau-Lavenshtein distance and looked up some tutorials online.  

I created some tests for these classes and put up test coverage to Codecov (badge is located at the top of the README file). I also added docstring to them.   

Testing, checking code quality with pylint and sending coverage report to Codecov are all featured in Github actions.

## How has the project progressed?

The program now has two classes; WordList and DamerauLavenshtein. Both of these classes have 100% test coverage.  

WordList contains a simple list that contains the needed English vocabulary and a function to check if a given word exists.  

For now DamerauLavenshtein has no functionality and only has basic construction.

## What I learned this week

I learned more about the Damerau-Lavenshtein algorithm, especially how the basic Lavenshtein algorithm is implemented.

## What has been unclear or problematic?

The algorithm seems very complicated, but I'm trying to breakdown some examples online to fully understand how they work.  

Also, I tried adding autopep8 formatting to github actions but it didn't seem to work. I don't think it really matters though, since I can do it via command line and Visual Studio does some formatting when saving.

## What next?

Next I will be working on completing an algorithm to calculate the Damerau-Levenshtein distance.
