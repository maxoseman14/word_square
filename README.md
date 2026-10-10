# Word Square Generator

Python CLI tool for generating a valid word square from a given list of letters.


## Prerequisities

To run this from the command line you will need:
* Python >3.8
* To install the requirements.txt
```
    pip install -r requirements.txt
```
* To have a local copy of a word dictionary containing valid English words, where each word is on a new line. You can find one here: http://norvig.com/ngrams/enable1.txt

## Running the script

To run from the root of this project:

e.g.
```
    python .\generate_word_square.py --letters "aaccdeeeemmnnnoo" --size 4 --file "enable1.txt"
```

The output should be a grid of size * size where the words in each column and row of the same
number spell the same word.

e.g.
```
    moan
    once
    acme
    need
```

## Running the unit tests

To run the unit tests:

```
    python -m pytest .\tests\test_generate_word_square.py
```