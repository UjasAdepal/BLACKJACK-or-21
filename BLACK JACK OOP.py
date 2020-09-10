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
        o += 11 * s

    else:
        o += 1 * s

    return o


class Blackjack:

    def start(self):
        print('')
        print('')
        print("Let's play BLACKJACK")
        print('')
        print('YOU HAVE 100 CHIPS')
        print('')

    def random_choise(self):

        pc1 = random.choice(cards)
        pc2 = random.choice(cards)
        arr.append(pc1)
        arr.append(pc2)

    def deal(self):
        while True:
            if deal == 'D' or deal == 'd':
                break
            elif deal == 'E' or deal == 'e':
                exit()

    def bet(self, bett):
        print('')
        if bett <= chips:
            pass
        else:
            print('')
            print('you dont have sufficient chips, you only have ', chips ,' left')
            exit()

    def initialdealerscards(self):

        print('DEALERS CARDS ')
        print(' x   {}  '.format(w))  # dealers cards

    def your_cards(self):
        print('')
        print('YOUR CARDS')
        listToStr = ' '.join([str(elem) for elem in arr])
        d = []
        for i in listToStr:
            d.append(i)
        listToStr = ' '.join([str(elem) for elem in d])
        print(listToStr)
        print('')
        print('')

    def cheak(self):
        print('')
        global chips
        if summ(arr) > 21:
            print('BUST')
            print('YOU LOSE')
            chips = chips - bett

        elif summ(arr) == 21 and summ(arr2) < 21:
            print('YOU WON')

            chips = chips + bett

        elif summ(arr) == 21 and summ(arr2) == 21:
            print('PUSH')

        elif summ(arr) == summ(arr2):
            print('PUSH')

        elif summ(arr2) > 21:
            print('YOU WON')

            chips = chips + bett

        elif summ(arr) < summ(arr2):
            print('YOU LOSE')

            chips = chips - bett

        elif summ(arr2) < summ(arr):
            print('YOU WON')

            chips = chips + bett

    def random(self,hitorstand):
            print('')
            x.initialdealerscards()
            if hitorstand == 'h' or hitorstand == 'H':
                f = random.choice(cards)
                arr.append(f)
                x.your_cards()
            elif hitorstand == 's' or hitorstand == 'S':
                x.your_cards()

    def dealerscards(self):
        while summ(arr2) <= 17:
            arr2.append(random.choice(cards))
        print('')
        print('DEALERS CARDS')
        listToStr = ' '.join([str(elem) for elem in arr2])
        d = []
        for i in listToStr:
            d.append(i)
        listToStr = ' '.join([str(elem) for elem in d])
        print(listToStr)
        print('')

    def bust(self):
        global chips
        if summ(arr) > 21:
            print('BUST')
            print('YOU LOSE')
            chips = chips - bett

    def zerocoins(self):
        if chips == 0:
            print('YOU DONT HAVE ANY CHIPS LEFT, YOU CANT PLAY FURTHER')
            exit()


x = Blackjack()
x.start()
chips = 100
while True:

    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    w = random.choice(cards)
    q = random.choice(cards)
    arr2 = [w, q]
    arr = []
    x.random_choise()
    deal = input('print D to get DEAL, and E to EXIT  : ')
    x.deal()
    bett = int(input('\nPLACE YOUR BET (bet must be less then chips you have) : '))
    x.bet(bett)
    print('')
    print('')
    x.initialdealerscards()
    x.your_cards()
    if summ(arr) == 21:
        print('BLACKJACK')
        chips += 3 / 2 * bett
        print('YOU HAVE', chips, 'CHIPS LEFT')
        continue
    elif summ(arr) == 21 and summ(arr2) == 21:
        print('PUSH')
    while summ(arr) <= 21:
        print('')
        x.initialdealerscards()
        print('')
        hitorstand = input('to HIT print H , to STAND print S  : ')

        if hitorstand == 'h' or hitorstand == 'H':
            f = random.choice(cards)
            arr.append(f)
            print(end='')
            x.your_cards()
        elif hitorstand == 's' or hitorstand == 'S':
            x.your_cards()
            break
    x.dealerscards()
    x.cheak()
    print('')
    print('')
    print('YOU HAVE', chips, 'CHIPS LEFT')
    print('')
    x.zerocoins()
