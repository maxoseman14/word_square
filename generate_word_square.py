import argparse
import requests
from collections import Counter


def validate_arguments(letters, multiplier):
    print(f"Validating arguments... letters: {letters}, multiplier: {multiplier}")
    if (len(letters) / multiplier != multiplier):
        message = "The number of letters should be the square of the multiplier"
        print(message)
        raise Exception(message)
    
    
def load_word_list():
    response = requests.get("http://norvig.com/ngrams/enable1.txt")

    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        
        
def can_build_word(word, char_pool):
    
    # Count the frequencies of letters in both the word and your pool
    word_counts = Counter(word)
    pool_counts = Counter(char_pool)
    
    # Check if the pool has enough of each letter required by the word
    for char, count in word_counts.items():
        if pool_counts[char] < count:
            return False
    return True


def get_possible_words(word_list: list, letters: str, multiplier: int):
    words = []
    for word in word_list:
        if len(word) == multiplier:
            if can_build_word(word, letters):
                words.append(word)
    return words


def generate_square_algorithm(possible_words: list, multiplier: int):
    current_square = []
    
    # Stop when square is full
    while len(current_square) < multiplier:
        
        unused_words = possible_words
        
        possible_words_dict = {}
        
        for current_word in unused_words:            
            
            # Start the square
            if(len(current_square) == 0):
                current_square.append(current_word)
                
                # Can't use this word again for this square
                unused_words.remove(current_word)
                
            else:
                # Create character list so can enumerate
                char_list = list(current_square[-1])
                
                # Start at the next position
                start_position = len(current_square)
                
                for index, character in enumerate(char_list[start_position:], start=start_position):
                    
                    position = index - 1
                    # find all words that contain the current char at the current index
                    matches = [word for word in unused_words if len(word) > position and word[position] == character]
                    
                    if(len(matches) > 0):
                        possible_words_dict[index] = matches
                    
                    # matches should contain all words that begin with the next character
                    # if (len(matches) > 0):
                    #     current_square.append(matches[0])
                    #     unused_words.remove(matches[0])
                    #     break

                    
                    
    print(current_square)
    return current_square     
                
    # The Rule is the index of the available words can be spelt by the index of each word (up to the multiplier)  
    # ROSE, OVEN, SEND, ENDS
    
        
    
def generate_square(letters: str, multiplier: int):
    word_list = load_word_list()
    
    possible_words = get_possible_words(word_list, letters, multiplier)
 
    square = generate_square_algorithm(possible_words, multiplier)
    for word in square:
        print(word)
    

def generate_word_square(letters, multiplier):
    validate_arguments(letters, multiplier)
    generate_square(letters, multiplier)
    
    
    
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