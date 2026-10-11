import argparse
from collections import Counter, defaultdict

def valid_letters(value):
    """Validates that argument is a letter in the English alphabet."""
    if not (value.isascii() and value.isalpha()):
        raise argparse.ArgumentTypeError(
            f"'{value}' is invalid. Only standard English letters (A-Z, a-z) are allowed."
        )
    return value

    
def valid_number(value):
    """Validates that argument is a positive whole number."""
    try:
        size = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid whole number.")
        
    if size <= 0:
        raise argparse.ArgumentTypeError(f"'{value}' must be a positive number greater than 0.")
    return size


def semantically_validate_args(letters, size):
    """Validates letters and size are compatible."""
    if (len(letters) / size != size):
        raise Exception("The number of letters should be the square of the size")
    
    
def load_word_file(file):
    """Loads the word file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f]
    except OSError as err:
        raise Exception(f"Unable to load word dictionary: {err}")
        
        
def generate_square(letters, size, words):
    
    prefix_dictionary = defaultdict(list)
    
    for word in words:
        if len(word) == size:
            for i in range(size):
                prefix_dictionary[word[:i]].append(word)
               
    def backtrack(square, letters):
        
        if len(square) == size:
            return True
        
        row_prefix = ""
        
        for word in square:
            row_prefix += word[len(square)]
            
        candidates = []
        
        candidates = prefix_dictionary[row_prefix]
                
        for word in candidates:
            
            word_count = Counter(word)
            available_letters = Counter(letters)
            
            can_make_word = True
            
            for letter, count in word_count.items():
                if count > available_letters[letter]:
                    can_make_word = False
                    break
                
            if not can_make_word:
                continue
            
            square.append(word)
            remaining_letters = available_letters - word_count
            
            if backtrack(square, remaining_letters):
                return True
            
            square.pop()
            
        return False
    
    square = []
        
    if backtrack(square, letters):
        return square
    
    return None


def parse_args(args=None):
    parser = argparse.ArgumentParser(
            description=""
        )
    
    parser.add_argument(
        "-l", "--letters",
        required=True,
        type=valid_letters,
        help="The letters to construct the word square from",
    )
    
    parser.add_argument(
        "-s", "--size",
        required=True,
        type=valid_number, 
        help="The size used to construct the grid",
    )
    
    parser.add_argument(
        "-f", "--file", 
        required=True,
        help="The file containing available words",
    )

    return parser.parse_args()
    
    
def main():
    
    args = parse_args()
    
    letters = args.letters
    size = args.size
    filename = args.file
    
    semantically_validate_args(letters, size)
    word_file = load_word_file(filename)

    print("Generating word square")
    result = generate_square(letters.lower(), size, word_file)
    if result is None:
        print("No Solution")
    else:
        for word in result:
            print(word)
    
if __name__ == "__main__":
    main()