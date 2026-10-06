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
    
    char_counts = Counter(letters)
    
    
    for word in word_list:
        fits = True
        if len(word) == multiplier:
            letter_counts = Counter(word)
            for letter, count in letter_counts.items():
                if char_counts[letter] < count:
                    # The word cannot be made from available pool
                    fits = False
                    break
            if not fits:
                continue
            words.append(word)
            for char in word:
                char_counts.subtract(char)
                
            
    return words



def generate_square_algorithm(available_words, multiplier):
    
    current_square = []
    
    for key, current_word in enumerate(available_words):
        # e.g. word is ROSE
        
        characters = list(current_word) # R O S E
        
        possible_words = defaultdict(list)
        
        # find words that start with remaining characters
        # add them to dictionaries so you end up with:
        #  {
        #     1: ["OVEN"],
        #     2: ["SEND"],
        #     3: ["ENDS"]
        # }
        
        for key, character in enumerate(characters[1:], start=1):
            
            for word in available_words:
                
                if word.startswith(character):
                    possible_words[key].append(word)
                else:
                    continue
    
        possible_words[0].append(current_word)
        #  {
        #     0: ["ROSE"],
        #     1: ["OVEN"],
        #     2: ["SEND"],
        #     3: ["ENDS"]
        # }
        
        if len(possible_words) != multiplier:
            # There were no words starting each character of the original word
            # Move current word to end of available_words list
            continue
             
        sorted_possible_words = dict(sorted(possible_words.items()))
        
        square_candidates = defaultdict(list)
        
        for index in sorted_possible_words:
            # Start from next word (OVEN)
            position = index + 1
            possible_words_list = possible_words[position]
            for possible_word in possible_words_list:
                # Need to spell word with index of other words in other lists
                word_to_spell = possible_word # OVEN
                letters = list(word_to_spell) # [O V E N]
                
                letter_indexed_words = []
                
                for letter_index, letter in enumerate(letters):
                    
                    if len(letter_indexed_words) == 0:
                        letter_indexed_words = sorted_possible_words.copy()
                    
                    letter_indexed_words[letter] = letter_indexed_words.pop(letter_index)
                    
                candidates = []
                for letter_index, liw_list in letter_indexed_words.items():
                    # find the letter at the index in the words in the list
                    
                    for letter_indexed_word in liw_list:
                        if list(letter_indexed_word)[position] == letter_index:
                            candidates.append(letter_indexed_word)
                            continue
                        else:
                            liw_list.pop(letter_indexed_word)
                
            if len(candidates) == multiplier:
                square_candidates[index] = candidates
            else:
                break
                            
        if len(square_candidates) == multiplier:
           if all(len(item) == multiplier for key, item in dict(square_candidates.items())):
               print("Square complete")
        else:
            break
    

        
    
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