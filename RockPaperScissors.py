import random,sys

print('Rock, Paper, Scissors')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: Rock, Paper, Scissors or Quit')
        playerMove = input()
        if playerMove =='Quit':
            sys.exit()
        if playerMove == 'Rock' or playerMove == 'Paper' or playerMove == 'Scissors':
            break


    # Display what the player chose:
    if playerMove == 'Rock':
        print('Rock versus...')
    elif playerMove == 'Paper':
        print('Paper versus...')
    elif playerMove == 'Scissors':
        print('Scissors versus...')
    elif playerMove == 'Quit':
        break

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'Rock'
    elif randomNumber == 2:
        computerMove = 'Paper'
    elif randomNumber == 3:
        computerMove = 'Scissors'

    print(computerMove)

    # Display and record the win/loss/tie:
    if playerMove == 'Rock' and computerMove == 'Scissors':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'Paper' and computerMove == 'Rock':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'Scissors' and computerMove == 'Paper':
        print('You win!')
        wins = wins + 1
    elif playerMove == computerMove:
        print('Tie!')
        ties = ties + 1
    else:
        print('You lose!')
        losses = losses + 1

# I later want to add a timer or something to add some suspense or animation, something to make it a little slower.