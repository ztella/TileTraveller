location = 11

while location != 31:
    if location == 11 or location == 21 or location == 31:
        print('You can travel: (N)orth.')
        dire = input('Direction: ')
        if dire == 'n' or dire == 'N':
            location += 1
        else:
            print('Not valid direction!')
    elif location == 12:
        print('You can travel: (N)orth or (E)ast or (S)outh.')
        dire = input('Direction: ')
        if dire == 'n' or dire == 'N':
            location += 1
        elif dire == 'e' or dire == 'E':
            location += 10
        elif dire == 's' or dire == 'S':
            location -= 1
        else: 
            print('Not valid direction!')
    elif location == 13:
        print('You can travel: (E)ast or (S)outh.')
        dire = input('Direction: ')
        if dire == 'e' or dire == 'E':
            location += 10
        elif dire == 's' or dire == 'S':
            location -= 1
        else:
            print('Not valid direction!')
    elif location == 23:
        print('You can travel: (E)ast or (W)est.')
        dire = input('Direction: ')
        if dire == 'e' or dire == 'E':
            location += 10
        elif dire == 'w' or dire == 'W':
            location -= 10
        else:
            print('Not valid direction!')
    elif location == 22 or location == 33:
        print('You can travel: (S)outh or (W)est.')
        dire = input('Direction: ')
        if dire == 's' or dire == 'S':
            location -= 1
        elif dire == 'w' or dire == 'W':
            location -= 10
        else:
            print('Not valid direction!')
    else: # location = 32
        print('You can travel: (N)orth or (S)outh.')
        dire = input('Direction: ')
        if dire == 's' or dire == 'S':
            location -= 1
        elif dire == 'n' or dire == 'N':
            location += 1
        else:
            print('Not valid direction!')
print('Victory!')

