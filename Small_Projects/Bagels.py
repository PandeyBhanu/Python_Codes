import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(''''Bagels, a deductive logic game.

 I am thinking of a {}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
 When I say: That means:
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.
 Bagels No digit is correct.

 For example, if the secret number was 248 and your guess was 843, the
 clus would be Fermi Pico.'''.format(NUM_DIGITS))


while True:
    secretNum = getSecretNum()
    print('I have thought of a number')
    print(' You have {} gueeses to get it.'.format(MAX_GUESSES))

    numGuesses = 1 #counter to keep track of number of guesses
    while numGuesses <=MAX_GUESSES:
        guess = ''
        while len(guess) !=NUM_DIGITS or not guess.isdecimal(): #input validation length and numbers
            print('Guess #{}:'.format(numGuesses))
            guess = input('> ')

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if guess == secretNum:
            break       #correct guess break out of loop
        if numGuesses > MAX_GUESSES:
            print("You ran out of guesses")
            print("The answer was {}".format(secretNum))

    print('Do you want to play again ?')