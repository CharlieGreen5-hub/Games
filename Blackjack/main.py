import math
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
        print("Please enter a whole number.")
    else:
        bet = int(bet)
        if bet <= money:
            print("You've bet " + str(bet) + " tokens.")
            money = money - bet
            game = 1
        else:
            print("Please enter a number lower than your balance, which is " + str(money) + ".")





    if game == 1:
        player_card_value = 0
        player_blackjack = 0
        bot_card_value = 0
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

        # Dealing Cards
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

        # Checking if player has a Blackjack
        if player_hand[0].split(' ',1)[0] == 'A':
            if player_hand[1].split(' ',1)[0] == '10' or player_hand[1].split(' ',1)[0] == 'J' or player_hand[1].split(' ',1)[0] == 'Q' or player_hand[1].split(' ',1)[0] == 'K':
                print('You have a Blackjack!')
                player_blackjack = 1
        elif player_hand[0].split(' ',1)[0] == '10' or player_hand[0].split(' ',1)[0] == 'J' or player_hand[0].split(' ',1)[0] == 'Q' or player_hand[0].split(' ',1)[0] == 'K':
            if player_hand[0].split(' ',1)[0] == 'A':
                print('You have a Blackjack!')
                player_blackjack = 1

        # Checking if player has a Blackjack
        if bot_hand[0].split(' ',1)[0] == 'A':
            if bot_hand[1].split(' ',1)[0] == '10' or bot_hand[1].split(' ',1)[0] == 'J' or bot_hand[1].split(' ',1)[0] == 'Q' or bot_hand[1].split(' ',1)[0] == 'K':
                if player_blackjack == 1:
                    print('The dealer also has a Blackjack!')
                else:
                    print('The dealer has a Blackjack! You lose.')
        elif bot_hand[0].split(' ',1)[0] == '10' or bot_hand[0].split(' ',1)[0] == 'J' or bot_hand[0].split(' ',1)[0] == 'Q' or bot_hand[0].split(' ',1)[0] == 'K':
            if bot_hand[0].split(' ',1)[0] == 'A':
                if player_blackjack == 1:
                    print('The dealer also has a Blackjack!')
                else:
                    print('The dealer has a Blackjack! You lose.')
        else:
            turn = 0
            bot_ace = 0
            while game == 1:
                player_card_value = 0
                bot_card_value = 0
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
                        bot_ace = 1
                        if bot_card_value <= 10:
                            bot_card_value += 11
                        elif bot_card_value > 10:
                            bot_card_value += 1
                print('Your hand value is ' + str(player_card_value) + '. ')
                if turn != 0:
                    print("The dealer's hand value is " + str(bot_card_value) + '. ')
                if player_card_value == 21 and turn == 0:
                    print('You have a Blackjack!')
                    if bot_card_value == 21:
                        print("The dealer also has a Blackjack! You didn't earn anything.")
                        money += bet
                        game = 0
                        break
                    else:
                        print('You were paid ' + str(math.floor(bet * 1.5)) + ' tokens.')
                        money = money + math.floor(bet * 2.5)
                        game = 0
                        break
                elif bot_card_value == 21 and turn == 0 and player_card_value < 21:
                    print('The dealer has a Blackjack! You lost ' + str(math.floor(bet * 1.5)) + ' tokens.')
                    money += bet
                    money -= math.floor(bet * 1.5)
                    game = 0
                    break
                if player_card_value == 21 and bot_card_value != 21:
                    print('You got 21! You win!')
                    money += (bet * 2)
                    break
                elif player_card_value == 21 and bot_card_value == 21:
                    print('You and the dealer got 21! You push and earn nothing.')
                    break
                elif bot_card_value == 21 and player_card_value != 21:
                    print('The dealer got 21. You lost ' + bet + '.')
                    break





                if player_card_value > 21:
                    print('You BUST! You lose!')
                    game = 0
                    break
                turn += 1
                player_action = input('You can choose to [HIT] or [STAY].\n> ')
                if player_action.upper() == 'HIT':
                    print('Drawing a card', end=" ")
                    time.sleep(0.5)
                    print('.', end=" ")
                    time.sleep(0.5)
                    print('.', end=" ")
                    time.sleep(0.5)
                    print('.')
                    card_selector = random.randint(0, len(used_deck) - 1)
                    player_hand.append(used_deck[card_selector])
                    print('You drew the ' + used_deck[card_selector])
                    used_deck.pop(card_selector)
                    time.sleep(0.5)
                    print('Your cards are ' + player_hand[0], end = '')
                    for i in range((len(player_hand)-1)):
                        print(' and ' + player_hand[i+1], end = '')
                elif player_action.upper() == 'STAY':
                    print("You didn't draw a card.")
                else:
                    print("Please type out the action.")
                time.sleep(0.5)
                if bot_card_value > 17:
                    print('The dealer stays and does not draw a card.')
                elif bot_card_value < 17 and bot_ace == 0:
                    print('\nThe Dealer is drawing', end=" ")
                    time.sleep(0.5)
                    print('.', end=" ")
                    time.sleep(0.5)
                    print('.', end=" ")
                    time.sleep(0.5)
                    print('.')
                    card_selector = random.randint(0, len(used_deck) - 1)
                    bot_hand.append(used_deck[card_selector])
                    print('The dealer drew the ' + used_deck[card_selector])
                    used_deck.pop(card_selector)
                    time.sleep(0.5)
                    print("The dealer's cards are " + bot_hand[0], end='')
                    for i in range((len(bot_hand) - 1)):
                        print(' and ' + bot_hand[i + 1], end='')
                    print('\n', end = '')
                    time.sleep(0.5)