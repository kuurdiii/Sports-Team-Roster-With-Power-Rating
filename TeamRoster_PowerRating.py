'''
ID P9363
CIS 443 - 01
Due 11/11/2021

This Python script allows the user to enter data about a
sports team roster and perform specified actions using a
menu system.

'''

# empty dict
roster = {}

# user input for players
s = input('Enter pairs: ')
tokens = s.split()
n = len(tokens)
if n % 2 == 1:
    n -= 1

i = 0
while i < n:
    key = int(tokens[i])
    val = int(tokens[i+1])
    if True:
        roster[key] = val
    i += 2

# menu with a loop. Breaks when user types 'q'
loop = True
while loop:
    print('\nMENU:')
    print('a - Add player')                         # ref 1
    print('d - Remove player')                      # ref 2
    print('u - Update player rating')               # ref 3
    print('r - Outputs players above a rating')     # ref 4
    print('o - Output roster')                      # ref 5
    print('q - Quit')                               # ref 6
    selection = input('Choose an option: ')


# ref 1
    if selection == 'a':
        var = input('Enter players jersey number and rating: ')     # input
        var = var.split()
        roster[int(var[0])] = int(var[1])       # adds new player into dict
        print("Added.")


# ref 2
    elif selection == 'd':
        var = input('Enter players jersey number to delete: ')
        if int(var) in roster.keys():       # checks if player exists
            del roster[int(var)]            # deletes player
            print("deleted.")


# ref 3
    elif selection == 'u':
        var = input('Enter players jersey number: ')
        if int(var) in roster.keys():       # checks if player exists
            rating = input('New rating: ')      # input for new rating
            roster[int(var)] = int(rating)      # adds new rating to dict


# ref 4
    elif selection == 'r':
        var = input('Enter rating: ')
        print("\nJersey Number     ", "Rating")
        print('-------------', '    ', '------')
        for v in roster.keys():
            if roster[v] > int(var):
                # checks if rating number is big or l
                # less than existing rating numbers
                print(f'{v:7} {roster[v]: 14}')


# ref 5
    elif selection == 'o':         # output
        print("\nJersey Number     ", "Rating")
        print('-------------', '    ', '------')
        for key in sorted(roster, key=roster.get, reverse=False):
            # reverse set to fale to keep
            # list in ascending order
            print(f'{key:7} {roster[key]: 14}')


# ref 6
    elif selection == 'q':
        loop = False
        print('\nGoodbye!\n')
    else:
        print('Invalid')
