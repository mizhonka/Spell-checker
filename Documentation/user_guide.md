# User guide

## Installation

1. [Download the newest release](https://github.com/mizhonka/Spell-checker/releases), extract the zip file and navigate to the root folder.
2. Install dependencies with  
```
poetry install
```
4. Execute the program with
```
poetry run invoke start
```

## Usage
![Screenshot](https://github.com/mizhonka/Spell-checker/new/main/Documentation/program.png)  
Inside the program, you have a couple of ways of entering text:  
* Write directly in the text box
* Open a .txt file with _Open file_

When you want to check the current text, press _Submit_. If any spelling mistakes were found, they will be highlighted in yellow. You will also be given a correction suggestion for each misspelling.  

You can accept a suggestion and replace the original word by pressing _Accept_. If you don't wish to do so, press _Skip_. After you have gone through every suggestion, the changes will be applied to the text.

You can also save the current text on your device as a new file with _Save as..._

