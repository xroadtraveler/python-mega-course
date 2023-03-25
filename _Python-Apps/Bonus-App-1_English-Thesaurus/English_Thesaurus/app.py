import json

data = json.load(open("data.json"))

def define(word):
    return data[word]

word = input("Enter word: ")

print(define(word))