#! python3
# hangman.py - Guess numbers before you get hanged!

import random
import sys

pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
"""
Hangman ASCII from
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
"""

# Get the list of words from hangman_words.txt from the same directory.
hangman_words = open('.\\hangman_words.txt').readlines()


def main_game():
    print('--HANGMAN--')

    word = random.choice(hangman_words).strip('\n')
    solved = [' '] * len(word)

    # Counter of wrong guesses
    counter = 0

    # Number of wrong guesses available before game over
    limit = 7 - 1

    # Letters that are not in the word
    wrong_guesses = []

    while True:

        # Print hangman
        print(pics[counter])

        # Print the word
        print('Word: ', end='')
        for i in solved:
            if i == ' ':
                print('_ ', end='')
            else:
                print(f'{i} ', end='')
        print('')

        # Print wrong guesses
        print(f"Misses: ", end='')
        print(*wrong_guesses, sep=', ')

        # Check win condition
        if ''.join(solved) == word:
            print('You won!\n')
            break
        elif counter >= limit:
            print(f"Game over!\nThe word was '{word}'\n")
            break

        # Input a letter
        while True:
            try:
                letter = input('>> ')[0].lower()
            except IndexError:
                continue

            # Player cannot input in already wrong guesses
            if letter in wrong_guesses:
                continue

            break

        # Check if letter is in word
        if letter in word:

            # Reveal the correct letter in solved
            for i in range(len(word)):
                if word[i] == letter:
                    solved[i] = word[i]

        # If not, add to hangman counter
        else:
            counter += 1
            wrong_guesses.append(letter)


def __main__():
    while True:
        print("Wanna play hangman? Enter 'y'! ('q' to quit)")
        user_input = input('>> ')

        if user_input.lower() == 'y':
            main_game()
        elif user_input.lower() == 'q':
            sys.exit()


__main__()
