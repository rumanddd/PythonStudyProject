import sys

while True:
    print('Type exit to exit')
    response = input()
    if response =='exit':
        sys.exit()
    print('You typed ' + response) # The indentation is behind the sys.exit to say that it will print this line only if the user does not type exit, seeing it's inline with the if statement.