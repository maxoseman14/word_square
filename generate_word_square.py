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



def generate_square_algorithm(available_words, multiplier):
    
    for key, current_word in enumerate(available_words):
        # e.g. word is ROSE
        
        characters = list(current_word)
        
        word_dict = defaultdict(list)
        
        # find words that start with remaining characters
        # add them to dictionaries
        for key, character in enumerate(characters[1:], start=1):
            
            for value in available_words:
                
                if value.startswith(character):
                    word_dict[key].append(value)
                else:
                    continue
    
        word_dict[0].append(current_word)
        if len(word_dict) != multiplier:
            # Move current word to end of available_words list
            continue
             
        # Loop through each item in the dictionary
        # First dict would be for O-words
        for index, value in sorted(word_dict.items()):
            # Don't care about first word
            start = index + 1
            dict_words = word_dict[start]
            for w in dict_words:
                # Need to spell w with index of other words in other lists
                word_to_spell = w # OVEN
                letters = list(word_to_spell) # [O V E N]
                
                for letter in letters:
                    for key, word_list in sorted(word_dict.items()): # word_dict is a dictionary of word lists
                        # In each dictionary, check for a word that has the letter at the right index
                        for word in word_list:
                            if list(word)[start] == letter:
                                continue
                            else:
                                # Remove word from the dictionary
                                word_list.pop(word)
                            
                
    
    

        
    
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