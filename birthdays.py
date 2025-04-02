birthdays = {'Ulviyya': '11th of September', 'Ruman': '30th of September', 'Pluto': '15th of June'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
            print(name + "'s birthday is on the " + birthdays[name])
    else:
            print('I do not have the birthday information for ' + name)
            print('When is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')