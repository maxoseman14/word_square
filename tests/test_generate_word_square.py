import pytest
import sys
from generate_word_square import validate_arguments, generate_square


def test_argument_validation():
    """Verifies that the arguments are compatible."""
    
    with pytest.raises(Exception, match="The number of letters should be the square of the multiplier"):
        validate_arguments("abcdefg", 3)


def test_generate_square():
    possible_words = ["rose", "oven", "send", "ends"]
    letters = "sdasfagfa"
    multiplier = 4
    
    generate_square(possible_words, letters, multiplier)  

    
def test_get_possible_words():
    
    word_list = ["fa", "pa", "up"]
    expected_words = ["fa", "up"]
    
    possible_words = get_possible_words(word_list, "pfau", 2)
    
    assert expected_words == possible_words
    
    