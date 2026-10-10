import argparse
from collections import Counter, defaultdict

def validate_arguments(letters, size, word_file):
    if (len(letters) / size != size):
        raise Exception("The number of letters should be the square of the size")
    
    try:
        with open(word_file, "r", encoding="utf-8") as f:
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
        "-m", "--size", 
        type=int, 
        default=4,
        help="The size used to construct the grid",
    )
    
    parser.add_argument(
        "-f", "--file", 
        type=str, 
        help="The file containing available words",
    )

    # 3. Parse the arguments from the command line
    args = parser.parse_args()
    letters = args.letters
    size = args.size
    word_file_name = args.file
    
    print(f"Validating arguments: letters: {letters}, size: {size}, word_file: {word_file_name}")
    word_file = validate_arguments(letters, size, word_file_name)
    
    print("Generating word square")
    result = generate_square(letters.lower(), size, word_file)
    if result is None:
        print("No Solution")
    else:
        for word in result:
            print(word)
    
if __name__ == "__main__":
    main()