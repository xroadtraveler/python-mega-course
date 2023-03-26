import json
from difflib import get_close_matches

# Loads JSON data into program
data = json.load(open("data.json"))

# Searches 'data' for compatible matches, returns definitions of input word
def define(word):
    word = word.lower()

    # Do first-level check for exact word matches
    if word in data:
        return data[word]
    
    # Handles cases for proper nouns, such as city names
    elif word.title() in data:
        return data[word.title()]
    
    # Handles acronyms such as USA or NATO
    elif word.upper() in data:
        return data[word.upper()]
    
    # Search similar words in the case of a typo
    # Check that similar words exist by checking for empty returned lists
    elif len(get_close_matches(word, data.keys())) > 0:
        # Set user input (Y/N) to a variable 'yn', prompt user to confirm whether suggested word was their word
        yn = input("Did you mean %s instead? Enter 'Y' if yes, or 'N' if no: " % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if yn.upper() == "Y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif yn.upper() == "N":
            return "The word doesn’t exist. Please double check it."
        else:
            return "We didn't understand your entry. Please try again."
    else:
        return "The word doesn’t exist. Please double check it."

# Prompts user to input a word to be defined
word = input("Enter word: ")

# Runs 'define' on a word, stores the output in a variable that we can iterate through
output = define(word)

# Check if output is 'list'
if type(output) == list:
    # Loop through 'output' and print each item on a separate line
    for item in output:
        print(item)
# Check if output type is 'string'
else:
    # Print string output
    print(output)