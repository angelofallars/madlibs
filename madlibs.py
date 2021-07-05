#! python3
'''
madlibs.py - Replace ADJECTIVE, NOUN, ADVERB and VERB
             in text files then save them to a new file.

Usage: Create a \text folder in the directory and
       put in .txt files with constructions like
       ADJECTIVE, NOUN, ADVERB and VERB to be replaced.
'''

import os
import re


def __main__():

    if not os.path.exists('.\\text'):
        print("No text folder 'text' detected.\
               Create one to do Mad Libs in there.")
        return None

    # Get files in text folder.
    files = os.listdir('.\\text')

    # Remove non .txt files and already madlibbed files
    for file in files:
        if file[-4:] != '.txt' or file[-14:] == '_madlibbed.txt':
            files.remove(file)

    # List files available to select.
    print('Select a file to do MAD LIBS in.')
    for file in range(len(files)):
        print(f'{file + 1}. {files[file]}')

    # Ask for file input from user.
    while True:
        try:
            select_file = int(input('>> '))
            current_file = files[select_file - 1]
            break

        except IndexError:
            print('Invalid input. Try again.')
            continue

        except ValueError:
            print('Invalid input. Try typing in the number of the text file\
                   you want to edit.')
            continue

    print(f'\n{current_file}:')
    ml_input = open(f'.\\text\\{current_file}').read()
    print(f'{ml_input}\n')

    # Find occurences of ADJECTIVE, NOUN, ADVERB and VERB.
    regex_words = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)+')
    words = regex_words.findall(ml_input)

    # Input the user to replace the words.

    replacers = []

    for word in words:

        # Enter a <grammatical structure>
        if word[0] == 'A':
            print('Enter an ', end='')
        else:
            print('Enter a ', end='')

        print(f'{word.lower()}:')
        replacers.append(input('>> '))

    # Replace them.
    for i in range(len(replacers)):
        ml_input = ml_input.replace(words[i], replacers[i], 1)
        # Print results to screen.
    print(f'\nSaved to {current_file[:-4]}_madlibbed.txt:')
    print(ml_input)

    # Save results to new text file.
    ml_output = open(f'.\\text\\{current_file[:-4]}_madlibbed.txt', 'w')
    ml_output.write(ml_input)
    ml_output.close()


__main__()
