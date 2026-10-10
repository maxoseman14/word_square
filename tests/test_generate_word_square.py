import pytest
from generate_word_square import validate_arguments, generate_square, parse_args


@pytest.fixture
def local_file(tmp_path):
    test_file = tmp_path / "words.txt"
    test_file.write_text("This is a test")
    return test_file


def test_argument_validation_success(local_file):
    """Verifies that the arguments are compatible."""
    
    validate_arguments("abcd", 2, local_file)
    

def test_argument_validation_letters_size_failure(local_file):
    """Test that an exception is raised if the arguments are not compatible"""
    
    with pytest.raises(Exception, match="The number of letters should be the square of the size"):
        validate_arguments("abcdefg", 3, local_file)
        
        
def test_argument_validation_file_does_not_exist():
    """Test that an exception is raised if the word dictionary file does not exist"""
    
    with pytest.raises(Exception, match="Unable to load word dictionary"):
        validate_arguments("abcdefghi", 3, "invalid.txt")
        
    
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
    
    
@pytest.mark.parametrize("bad_args", "expected_error",
[
    (
        ["--letters", 5, "--size", 7, "--file", "test.txt"],
        "error: argument -l/--letters: '5' is invalid. Only standard English letters (A-Z, a-z) are allowed."
    ),
    (
        ["--letters", "abc", "--size", "7", "--file", "test.txt"],
        "error: argument -m/--size: '7' is invalid. Only numbers are allowed"
    ),
    (
        ["--letters", "abc", "--size", 7, "--file", 1],
        
    ),
    (
        ["--letters", "abc", "--size", 7],
        "error: the following arguments are required: -f/--file"
    )
])
def test_parse_arguments_invalid_inputs(bad_args):
    """Test various invalid inputs all trigger SystemExit."""
    with pytest.raises(SystemExit):
        parse_args(bad_args)