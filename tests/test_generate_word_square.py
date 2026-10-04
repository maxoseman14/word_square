import pytest
import sys
from generate_word_square import validate_arguments, generate_square_algorithm, generate_square, get_possible_words


def test_argument_validation():
    """Verifies that the arguments are compatible."""
    
    with pytest.raises(Exception, match="The number of letters should be the square of the multiplier"):
        validate_arguments("abcdefg", 3)


def test_generate_square_algorithm():
    possible_words = ["rose", "oven", "send", "ends"]
    multiplier = 4
    
    generate_square_algorithm(possible_words, multiplier)
    
    
    
def test_generate_square():
    letters = "eeeeddoonnnsssrv"
    multiplier = 4
    
    generate_square(letters=letters, multiplier=multiplier)
    
    
def test_get_possible_words():
    
    word_list = ["fa", "pa", "up"]
    
    possible_words = get_possible_words(word_list, "pfau", 2)
    
    assert word_list == possible_words
    
    
def test_find_words():
    
    word_list = ["rose", "send", "oven", "ends"]
    
    find_words(word_list=word_list, multiplier=4)
    
    