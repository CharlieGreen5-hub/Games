import random
import time

# Deck setup

ranks = ['2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10 ', 'J ', 'Q ', 'K ', 'A ']
suits = ['♠', '♥', '♣', '♦']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9,'10': 10, 'J': 10, 'Q': 10, 'K': 10}
deck = []
for i in range(13):
    deck.append(ranks[i] + suits[0])
    deck.append(ranks[i] + suits[1])
    deck.append(ranks[i] + suits[2])
    deck.append(ranks[i] + suits[3])

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



#Game Loop
while True:
    player_hand = []
    bot_hand = []
    used_deck = deck.copy()
    print('Dealing now', end=" ")
    time.sleep(0.5)
    print('.', end=" ")
    time.sleep(0.5)
    print('.', end=" ")
    time.sleep(0.5)
    print('.')
    for i in range(2):
        card_selector = random.randint(0, len(used_deck) - 1)
        player_hand.append(used_deck[card_selector])
        used_deck.pop(card_selector)
        card_selector = random.randint(0, len(used_deck) - 1)
        bot_hand.append(used_deck[card_selector])
        used_deck.pop(card_selector)
    print('Your cards are ' + str(player_hand[1]) + ' and ' + str(player_hand[0]))
    time.sleep(0.5)
    print("The opponent's hand has been dealt.\nThe Dealer's upcard is " + bot_hand[0])
    time.sleep(0.5)
    player_card_value = 0
    bot_card_value = 0
    while True:
        for i in range(len(player_hand)):
            if str(player_hand[i].split(' ',1)[0]) != 'A':
                player_card_value += values[str(player_hand[int(i)].split(' ', 1)[0])]
            elif str(player_hand[i].split(' ',1)[0]) == 'A':
                if player_card_value <= 10:
                    player_card_value += 11
                elif player_card_value > 10:
                    player_card_value += 1
        for i in range(len(bot_hand)):
            if str(bot_hand[i].split(' ',1)[0]) != 'A':
                bot_card_value += values[str(bot_hand[int(i)].split(' ', 1)[0])]
            elif str(bot_hand[i].split(' ',1)[0]) == 'A':
                if bot_card_value <= 10:
                    bot_card_value += 11
                elif bot_card_value > 10:
                    bot_card_value += 1
        print('Your hand value is ' + str(player_card_value))