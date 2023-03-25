import json

data = json.load(open("data.json"))

def define(word):
    if word.lower() in data:
        return data[word.lower()]
    else:
        return "The word doesn’t exist. Please double check it."

word = input("Enter word: ")

print(define(word))