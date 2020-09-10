import random

def summ(arr):
    o = 0
    for i in arr:
        if type(i) == int:
            o += i

        elif i == "K" or i == 'J' or i == "Q":
            o += 10

        elif i == 'A':
            continue

    s = arr.count('A')

    if o <= 10:
        o += 11*s

    else:
        o += 1*s

    return o


print('')
print('')

print("Let's play BLACKJACK")
print('')
print('YOU HAVE 100 CHIPS')
chips = 100
cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
print('')

while True:

    deal = input('print D to get DEAL, and E to EXIT  : ')
    while True:
        if deal == "D" or deal == "d":
            break
        elif deal == 'E' or deal == 'e':
            exit()

    print('')

    while True:
        bet = int(input('PLACE YOUR BET (bet must be less then chips you have) : '))
        if bet <= chips:
            break
        else:
            print('\nyou dont have sufficient chips, you only have',chips,'chips\n')

    print('')
    print('')
    print('')

    print('DEALERS CARDS ')
    w = random.choice(cards)
    x = random.choice(cards)
    print(' x   {}  '.format(w))  # dealers cards
    print('')


    pc1 = random.choice(cards)
    pc2 = random.choice(cards)
    print('YOUR CARDS')
    print(' {}   {}  '.format(pc1,pc2))  # first turn of player
    print('')

    arr2 = [w,x]

    arr = [pc2,pc1]
    arr1 = [pc2,pc1]

    if summ(arr) == 21 and summ(arr2) != 21:
        print('BLACKJACK')
        chips = chips + bet + bet/2
        print('YOU HAVE', chips, 'CHIPS LEFT')
        continue
    elif summ(arr) == 21 and summ(arr2) == 21:
        print('PUSH')
        print('YOU HAVE', chips, 'CHIPS LEFT')
        continue


    while summ(arr) <= 21:
        print('')
        print('')
        print('DEALERS CARDS ')
        print(' x   {}  '.format(w))  # dealers cards
        print('')

        h = input('to HIT print H , to STAND print S  : ')
        print('')
        if h == 'h' or h == 'H':
            f = random.choice(cards)
            arr.append(f)
            print('YOUR CARDS')
            listToStr = ' '.join([str(elem) for elem in arr])
            d = []
            for i in listToStr:
                d.append(i)
            listToStr = ' '.join([str(elem) for elem in d])
            print(listToStr)
            print('')

        elif h == 's' or h == 'S':
            print('YOUR CARDS')
            listToStr = ' '.join([str(elem) for elem in arr])
            d = []
            for i in listToStr:
                d.append(i)
            listToStr = ' '.join([str(elem) for elem in d])
            print(listToStr)
            print('')
            break

    while summ(arr2) <= 17:
        arr2.append(random.choice(cards))
    print('')
    print('')
    print('DEALERS CARDS')
    listToStr = ' '.join([str(elem) for elem in arr2])
    d = []
    for i in listToStr:
        d.append(i)
    listToStr = ' '.join([str(elem) for elem in d])
    print(listToStr)

    print('')
    print('')

    if summ(arr) > 21:
        print('BUST')
        print('YOU LOSE')
        chips = chips - bet

    elif summ(arr) == 21 and summ(arr2) < 21:
        print('YOU WON')
        chips = chips + bet

    elif summ(arr) == 21 and summ(arr2) == 21:
        print('PUSH')

    elif summ(arr) == summ(arr2):
        print('PUSH')

    elif summ(arr2) > 21:
        print('YOU WON')
        chips = chips + bet

    elif summ(arr) < summ(arr2):
        print('YOU LOSE')
        chips = chips - bet

    elif summ(arr2) < summ(arr):
        print('YOU WON')
        chips = chips + bet



    print('')
    print('')
    print('YOU HAVE', chips , 'CHIPS LEFT')
    if chips == 0:
        print('YOU HAVE NO CHIPS LEFT, YOU CANT PLAY FURTHER ')
        break
