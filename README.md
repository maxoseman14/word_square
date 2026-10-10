# Word Square Generator

Python CLI tool for generating a valid word square from a given list of letters.


## Prerequisities

To run this from the command line you will need:
* Python >3.8
* To install the requirements.txt
```
    pip install -r requirements.txt
```
* To have a local copy of a word dictionary, you can find one here: http://norvig.com/ngrams/enable1.txt

## Running the script

To run from the root of this project:

e.g.
```
    python .\generate_word_square.py --letters "aaccdeeeemmnnnoo" --multiplier 4 --file "enable1.txt"
```

The output should be a grid of multiplier * multiplier where the words in each column and row of the same
number spell the same word.

e.g.
```
    moan
    once
    acme
    need
```