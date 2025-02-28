import random  # Importing the random module

# Defining a list of pet names
pets = ['Dog', 'Cat', 'Snake']  # This is a list

# Using random.choice() to select a random element from the list
print(random.choice(pets))  # Will print out a random pet from the list

# You can consider random.choice(someList) to be a shorter form of:
# someList[random.randint(0, len(someList) – 1)]
