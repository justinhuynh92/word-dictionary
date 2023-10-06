# check if the word is in the dictionary
# print the definition
from PyDictionary import PyDictionary

dictionary = PyDictionary()

#ask user for what it wants to get the defintion of
while True:
    word = input('Enter your word: ')
    if word == '':
        break
    
    print(dictionary.meaning(word))
