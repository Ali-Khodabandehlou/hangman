# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:45:36 2019

@author: Ali
"""

#import random
from random_word import RandomWords

#words_library = ["super natural",
#                 "tsunami",
#                 "computer",
#                 "united states",
#                 "hangman",
#                 "manufacturer"]

def guess_the_word():
    num_of_possible_errors = 12
    errors = 0
    
    r = RandomWords()
#    actual_word = list(random.choice(words_library))
    actual_word = list(r.get_random_word(minLength=5))
    guessed_word = []
    word_length = 0
    for i in range(len(actual_word)):
        if actual_word[i] == " ":
            guessed_word.append(" ")
        elif actual_word[i] == "-":
            guessed_word.append("-")
        else:
            actual_word[i] = actual_word[i].lower()
            guessed_word.append("_")
            word_length += 1
    
    letter = ""
    
    print("\nthe word would have " + str(word_length) + " letters")
    
    while(True):
        letter = input("\nenter a letter: ")
        if letter in actual_word:
            for i, l in enumerate(actual_word):
                if(l == letter):
                    guessed_word[i] = letter
        else:
            errors += 1
            print("wrong!\nnumber of errors: " + str(errors))
        print("your guessed word: " + "".join(guessed_word))
        if errors >= num_of_possible_errors:
            print("\nyou lost!")
            print("the word was: " + "".join(actual_word) + "\n")
            break
        if guessed_word == actual_word:
            print("\ncongradulations! You guessed the word correctly.")
            break
    
    
def welcome():
    print("Welcome to the hangman game.")
    print("Enter your guess letter and we'll show you your guessed word.")
    print("The rest is easy to follow ;-)")
    
    input("\npress enter whenever you're ready!")

welcome()

while(True):
    guess_the_word()
    a = input("\ndo you want to play again?(y/n) ")
    if a != "y":
        break