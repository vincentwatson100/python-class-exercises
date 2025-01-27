#import
import random
#make color
green = '\033[032m'
yellow = '\033[033m'
red = '\033[031m'
end = '\033[0m'

#give directions
print('Welcome to Wordle game. you have six guesses to guess the five letter secret word:')
#make word list using files
#fhand = open('fiveLetterWords.py')

word_list = ['grape','peach','mango']

#make computer choose random word 
secret_word = random.choice(word_list)
num_guesses = 6
#make an input
guess = input('please enter a five letter word:')
#make sure guess is 5 letters
if len(guess) == 5:
    print(f'you have, {num_guesses}left')
if len(guess) != 5:
    print('that is an invalid guess, the guess must be five letters exactly. please guess again:')
if guess == secret_word:
    print(f'{green}YOU WIN YOU GUESSED THE SECRET WORD.{end}')
#finish making green colored characters
for letter_index in range (len(guess)):
    if guess[letter_index] == secret_word[letter_index]:
        print(f'{green}{guess[letter_index]}{end}')
    
    #make  yellow charcters
    if guess[letter_index] in secret_word:
        print(f'{yellow}{guess[letter_index]}{end}')
    
    #make red colored characters 
    else:
        print(f'{red}{guess}{end}')
    #control number of inputs and make it so a non 5 letter word counts
    #number_of_inputs = 6
    #for 




