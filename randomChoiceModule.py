import random

pets = ['Dog', 'Cat', 'Snake'] # This is a list
random.choice(pets)
'Dog'
random.choice(pets)
'Cat'
random.choice(pets) # Will print out a random element from the list
'Snake'

print(random.choice(pets)) # Will print out a random element from the list
# You can consider random.choice(someList) to be a shorter form of someList[random.randint(0, len(someList) – 1]
