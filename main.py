import random
import time

# Deck setup

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9,'10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
deck = []
for i in range(13):
    deck.append(ranks[i] + ' of ' + suits[0])
    deck.append(ranks[i] + ' of ' + suits[1])
    deck.append(ranks[i] + ' of ' + suits[2])
    deck.append(ranks[i] + ' of ' + suits[3])

# Money Loading

money = open("money.txt", "r")
money = int(money.read())
print("Welcome to Bumblebee's Casino! We're playing Blackjack with one deck of cards.")

# Start loop

while True:
    bet = input("How much would you like to bet? You have " + str(money) + " tokens left.\n> ")
    if not bet.isdigit():
        print("Please enter a number.")
    else:
        bet = int(bet)
        if bet <= money:
            print("You've bet " + str(bet) + " tokens.")
            money = money - bet
            break
        else:
            print("Please enter a number lower than your balance, which is " + str(money) + ".")

player_hand = []
used_deck = deck.copy()
print(used_deck)
while True:

