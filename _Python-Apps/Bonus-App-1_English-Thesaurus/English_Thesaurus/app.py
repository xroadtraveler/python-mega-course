import json
from difflib import get_close_matches

# Loads JSON data into program
data = json.load(open("data.json"))

# Searches 'data' for compatible matches, returns definitions of input word
def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
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

# Prints resulting definition of user input
print(define(word))