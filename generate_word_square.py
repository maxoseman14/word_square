import argparse
import requests
from collections import Counter, defaultdict


def validate_arguments(letters, multiplier):
    print(f"Validating arguments... letters: {letters}, multiplier: {multiplier}")
    if (len(letters) / multiplier != multiplier):
        message = "The number of letters should be the square of the multiplier"
        print(message)
        raise Exception(message)
    
    
def load_word_list():
    with open("enable1.txt", "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f]
        
        
def generate_square(words, letters, multiplier):
               
    def backtrack(square, letters):
        
        if len(square) == multiplier:
            return True
        
        prefix = ""
        
        for word in square:
            prefix += word[len(square)]
            
        candidates = []
        
        for word in words:
            if word.startswith(prefix):
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
    

def generate_word_square(letters, multiplier):
    validate_arguments(letters, multiplier)
    result = generate_square(load_word_list(), letters, multiplier):
    if result is None:
        print("No Solution")
    else:
        for word in result:
            print(word)
    
    
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

    # 3. Parse the arguments from the command line
    args = parser.parse_args()
    
    generate_word_square(args.letters, args.multiplier)
    
if __name__ == "__main__":
    main()