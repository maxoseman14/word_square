import pytest
import re
from generate_word_square import (
    load_word_file,
    semantically_validate_args, 
    generate_square, 
    valid_letters,
    valid_number
)


@pytest.fixture
def valid_local_file(tmp_path):
    test_file = tmp_path / "words.txt"
    test_file.write_text("Test")
    return test_file


def test_valid_letters_success():
    """Test valid letters pass validation"""
    letters = "abcd"
    assert valid_letters(letters) == letters
    

def test_valid_letters_failure():
    """Test invalid letters fail validation"""
    letters = "abc0"
    with pytest.raises(Exception, match=re.escape("'abc0' is invalid. Only standard English letters (A-Z, a-z) are allowed.")):
        valid_letters(letters)
        
    
def test_valid_number_success():
    """Test valid numbers pass validation"""
    number = "1"
    assert valid_number(number) == int(number)
    

def test_valid_number_negative_failure():
    """Test negative number fail validation"""
    number = "-1"
    with pytest.raises(Exception, match=re.escape("'-1' must be a positive number greater than 0.")):
        valid_number(number)
        

def test_valid_number_decimal_failure():
    """Test decimal number fail validation"""
    number = "0.5"
    with pytest.raises(Exception, match=re.escape("'0.5' is not a valid whole number.")):
        valid_number(number)
    

def test_argument_validation_success():
    """Verifies that the arguments are compatible."""
    
    semantically_validate_args("abcd", 2)
    

def test_argument_validation_letters_size_failure():
    """Test that an exception is raised if the arguments are not compatible"""
    
    with pytest.raises(Exception, match="The number of letters should be the square of the size"):
        semantically_validate_args("abcdefg", 3)
        
        
def test_load_word_file():
    """Test that an exception is raised if the word dictionary file cannot be loaded"""
    
    with pytest.raises(Exception, match="Unable to load word dictionary"):
        load_word_file("file.txt")
        
    
def test_generate_square():
    """Test square generates when available words match solution words"""
    
    solution = ["moan", "once", "acme", "need"]
    letters = "aaccdeeeemmnnnoo"
    size = 4
    
    result = generate_square(letters, size, solution)
    assert result == solution
    
    
def test_generate_square_with_prefix_alternatives():
    """Test square generates when available words contain other possible prefixes"""

    possible_words = ["moan", "once", "acid", "need", "aced", "acme"]
    solution = ["moan", "once", "acme", "need"]
    letters = "aaccdeeeemmnnnoo"
    size = 4

    result = generate_square(letters, size, possible_words)
    
    assert result == solution
    
    
def test_generate_square_incorrect_letters():
    """Test no solution found when letter input cannot produce valid square"""
    
    possible_words = ["moan", "once", "acid", "need", "aced", "acme"]
    letters = "aaccdeeeemmnnnop"
    size = 4

    result = generate_square(letters, size, possible_words)
    
    assert result == None