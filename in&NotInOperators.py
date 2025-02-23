myPets = ['Rambo', 'Mia', 'Pluto']
print('Enter a pet name:')
name = input()
if not name in myPets:
    print('I do not have any pet with the name ' + name)
else:
    print('Correct! ' + name + ' is one of my pets.')