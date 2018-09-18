location = 11
invalidInput = False
while location != 31:
    if location == 11 or location == 21 or location == 31:
        if invalidInput == False:
            print('You can travel: (N)orth.')
        dire = input('Direction: ')
        if dire == 'n' or dire == 'N':
            invalidInput = False
            location += 1
        else:
            invalidInput = True
            print('Not a valid direction!')
    elif location == 12:
        if invalidInput == False:
            print('You can travel: (N)orth or (E)ast or (S)outh.')
        dire = input('Direction: ')
        if dire == 'n' or dire == 'N':
            invalidInput = False
            location += 1
        elif dire == 'e' or dire == 'E':
            invalidInput = False
            location += 10
        elif dire == 's' or dire == 'S':
            invalidInput = False
            location -= 1
        else:
            invalidInput = True
            print('Not a valid direction!')
    elif location == 13:
        if invalidInput == False:
            print('You can travel: (E)ast or (S)outh.')
        dire = input('Direction: ')
        if dire == 'e' or dire == 'E':
            invalidInput = False
            location += 10
        elif dire == 's' or dire == 'S':
            invalidInput = False
            location -= 1
        else:
            invalidInput = True
            print('Not a valid direction!')
    elif location == 23:
        if invalidInput == False:
            print('You can travel: (E)ast or (W)est.')
        dire = input('Direction: ')
        if dire == 'e' or dire == 'E':
            invalidInput = False
            location += 10
        elif dire == 'w' or dire == 'W':
            invalidInput = False
            location -= 10
        else:
            invalidInput = True
            print('Not a valid direction!')
    elif location == 22 or location == 33:
        if invalidInput == False:
            print('You can travel: (S)outh or (W)est.')
        dire = input('Direction: ')
        if dire == 's' or dire == 'S':
            invalidInput = False
            location -= 1
        elif dire == 'w' or dire == 'W':
            invalidInput = False
            location -= 10
        else:
            invalidInput = True
            print('Not a valid direction!')
    else: # location = 32
        if invalidInput == False:
            print('You can travel: (N)orth or (S)outh.')
        dire = input('Direction: ')
        if dire == 's' or dire == 'S':
            invalidInput = False
            location -= 1
        elif dire == 'n' or dire == 'N':
            invalidInput = False
            location += 1
        else:
            invalidInput = True
            print('Not a valid direction!')
print('Victory!')

