import pytest
from generate_word_square import validate_arguments, generate_square


def test_argument_validation_success():
    """Verifies that the arguments are compatible."""
    validate_arguments("abcd", 2)

def test_argument_validation():
    """Test that an exception is raised if the arguments are not compatible"""
    
    with pytest.raises(Exception, match="The number of letters should be the square of the multiplier"):
        validate_arguments("abcdefg", 3)
    
def test_generate_square():
    solution = ["moan", "once", "acme", "need"]
    letters = "aaccdeeeemmnnnoo"
    multiplier = 4
    
    result = generate_square(solution, letters, multiplier)
    assert result == solution
    
    
def test_generate_square_with_prefix_alternatives():
    possible_words = ["moan", "once", "acid", "need", "aced", "acme"]
    solution = ["moan", "once", "acme", "need"]
    letters = "aaccdeeeemmnnnoo"
    multiplier = 4

    result = generate_square(possible_words, letters, multiplier)
    
    assert result == solution
    
    
def test_generate_square_incorrect_letters():
    possible_words = ["moan", "once", "acid", "need", "aced", "acme"]
    letters = "aaccdeeeemmnnnop"
    multiplier = 4

    result = generate_square(possible_words, letters, multiplier)
    
    assert result == None