# zmiany  na kiedyś:
# - Dodać Split
# - Dodac Insurance
# - Dodać  animacje


import random
import time

oneColorCards = [2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING", "ACE"]
dealersCards = []
playersCards = []

def dealer_draws():
    card = random.choice(oneColorCards)
    dealersCards.append(card)
    #print(str(dealersCards))
    print("Dealer got: " + str(dealersCards))

def dealer_draws_face_down():
    card = random.choice(oneColorCards)
    dealersCards.append(card)
    print(str(dealersCards))
    print("Dealer draws face down")

def player_draws():
    card = random.choice(oneColorCards)
    playersCards.append(card)
    #print(str(playersCards))
    print("Player got: " + str(playersCards))

def game_begin():
    dealer_draws()
    time.sleep(1)
    player_draws()
    time.sleep(1)
    dealer_draws_face_down()
    time.sleep(1)
    player_draws()
    time.sleep(1)
    check_if_bj()

def check_if_bj():
    if card_counter(dealersCards) == card_counter(playersCards) == 21:
        print("Push")
        exit()

    if card_counter(dealersCards) == 21:
        print("Dealer has BlackJack :(")
        exit()

    if card_counter(playersCards) == 21:
        print("Player has BlackJack :)")
        exit()


def card_counter(cards):
    s = 0
    aceOn = 0

    for i in range(len(cards)):
        if cards[i] == "JACK" or cards[i] == "QUEEN" or cards[i] == "KING":
            s += 10
        elif cards[i] == "ACE":
            aceOn +=1
        else:
            s += int(cards[i])

    if aceOn > 0:
        for i in range(aceOn):
            if s < 11:
                s+=11
            else:
                s+=1

    return s

def check_who_won(cards1, cards2):
    if card_counter(cards1) > card_counter(cards2):
        print("Player won :)")
        exit()
    elif card_counter(cards1) < card_counter(cards2):
        print("Dealer won :(")
        exit()
    else:
        print("Push")
        exit()

def hit_or_stand():
    i = input("Hit or Stand (write H or S)")

    if i == "H":
        player_draws()
        time.sleep(1)
        if card_counter(playersCards) > 21:
            print("Dealer wins :(")
            exit()
    elif i == "S":
        print("Dealer got: " + str(dealersCards))
        time.sleep(1)
        # print(str(card_counter(dealersCards)))
        while card_counter(dealersCards) < 17:
            print("Dealer draws a card")
            dealer_draws()
            time.sleep(1)
            if card_counter(dealersCards) > 21:
                print("Player won :)")
                exit()

        check_who_won(playersCards, dealersCards)

#MAIN:

game_begin()

while True:
    hit_or_stand()

