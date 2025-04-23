import random

def getanswer(answernumber): # The getAnswer() function is defined
    if answernumber == 1: # The program execution moves to the top of the getAnswer() function, and the value r is stored in a parameter named answerNumber.
        return 'It is certain'
    elif answernumber == 2:
        return 'It is decidedly so'
    elif answernumber == 3:
        return 'Yes'
    elif answernumber == 4:
        return 'Reply hazy try again'
    elif answernumber == 5:
        return 'Ask again later'
    elif answernumber == 6:
        return 'Concentrate and ask again'
    elif answernumber == 7:
        return 'My reply is no'
    elif answernumber == 8:
        return 'Outlook not so good'
    elif answernumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9) # This value is stored in a variable named r.
fortune = getanswer(r) # The getAnswer() function is called with r as the argument
print(fortune) # The returned string is assigned to a variable named fortune

# print(getAnswer(random.randint(1, 9))) # This code is equivalent to the code above.