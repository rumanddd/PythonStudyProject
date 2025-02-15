import random

#Chooses a number between 1 and 50
secretNumber = random.randint(1, 50)
print('I am thinking of a number between 1 and 50.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    if guessesTaken == 6:
        print('Take a guess, you have ' + str(7 - guessesTaken) + ' guess left.')
    else:
        print('Take a guess, you have ' + str(7 - guessesTaken) + ' guesses left.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')  # Tells the player if their guess is too low
    elif guess > secretNumber:
        print('Your guess is too high.')  # Tells the player if their guess is too high
    else:  # The correct guess
        if guessesTaken == 1:
            print('Good job! You guessed my number in 1 guess!')  # Singular case
        else:
            print('Good job! You guessed my number in {guessesTaken} guesses!')  # Plural case
        break  # Exit the loop since the correct number was guessed.