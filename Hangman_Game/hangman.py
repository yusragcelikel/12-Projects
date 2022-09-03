import random
from words import words_list

def get_valid_word(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)

        return word.upper()

def hangman():
