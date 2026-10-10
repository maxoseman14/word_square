import argparse
from collections import Counter


def validate_arguments(letters, multiplier, word_file):
    print(f"Validating arguments: letters: '{letters}', multiplier: {multiplier}, word_file: {word_file}")
    if (len(letters) / multiplier != multiplier):
        message = "The number of letters should be the square of the multiplier"
        raise Exception(message)
    
    try:
        with open(word_file, "r", encoding="utf-8") as f:
            return [line.strip().lower() for line in f]
    except OSError as err:
        message = "Unable to load word dictionary: {err}"
        raise Exception(message)
        
        
def generate_square(letters, multiplier, words):
               
    def backtrack(square, letters):
        
        if len(square) == multiplier:
            return True
        
        prefix = ""
        
        for word in square:
            prefix += word[len(square)]
            
        candidates = []
        
        for word in words:
            if len(word) == multiplier and word.startswith(prefix):
                candidates.append(word)
                
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
    
    
def main():
    parser = argparse.ArgumentParser(
        description=""
    )

    parser.add_argument(
        "-l", "--letters",
        type=str,
        help="The letters to construct the word square from",
    )
    
    parser.add_argument(
        "-m", "--multiplier", 
        type=int, 
        default=4,
        help="The multiplier used to construct the grid",
    )
    
    parser.add_argument(
        "-f", "--file", 
        type=str, 
        help="The file containing available words",
    )

    # 3. Parse the arguments from the command line
    args = parser.parse_args()
    letters = args.letters
    multiplier = args.multiplier
    word_file_name = args.file
    
    word_file = validate_arguments(letters, multiplier, word_file_name)
    
    result = generate_square(letters, multiplier, word_file)
    if result is None:
        print("No Solution")
    else:
        for word in result:
            print(word)
    
if __name__ == "__main__":
    main()