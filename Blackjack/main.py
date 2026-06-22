import math
import random
import time

# Deck setup

ranks = ['2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10 ', 'J ', 'Q ', 'K ', 'A ']
suits = ['♠', '♥', '♣', '♦']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9,'10': 10, 'J': 10, 'Q': 10, 'K': 10}
aces = ['A ♠', 'A ♥', 'A ♣', 'A ♦']
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
instructions = input("Press 'I' for instructions and rules, or type any other key to start.\n> ")
if instructions.upper() == 'I':
    print('''1) Blackjacks will pay out 3:2, rounded down.
2) If you bust, you lose, regardless of whether the dealer busts.
3) Follow the prompts, and type out inputs that are shown in square brackets.
4) Enjoy playing!''')
    time.sleep(3)
game = 0

# Start loop

while money > 0:
    while True:
        bet = input("How much would you like to bet? You have " + str(money) + " tokens left.\n> ")
        if not bet.isdigit():
            print("Please enter a whole number.")
        else:
            bet = int(bet)
            if bet <= money:
                print("You've bet " + str(bet) + " tokens.")
                money = money - bet
                with open("money.txt", "w") as f:
                    f.write(str(money))
                game = 1
                break
            else:
                print("Please enter a number lower than your balance, which is " + str(money) + ".")





    if game == 1:
        player_card_value = 0
        split_card_value = 0
        splittable = 0
        split_bet = 0
        first_hand_bust = 0
        second_hand_bust = 0
        player_blackjack = 0
        bot_card_value = 0
        main_hand_end = 0
        first_hand_end = 0
        second_hand_end = 0
        player_hand = []
        split_hand = []
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

        # Checking if the hand can be split
        if player_hand[0].split(' ',1)[0] == player_hand[1].split(' ',1)[0] and money >= bet:
            splittable = 1
            split_bet = bet
            money -= bet

        turn = 0
        bot_ace = 0
        while game == 1:
            player_card_value = 0
            bot_card_value = 0
            split_card_value = 0
            player_ace = 0
            split_ace = 0
            bot_ace= 0
            # Calculating Card Values
            for i in range(len(player_hand)):
                if str(player_hand[i].split(' ',1)[0]) != 'A':
                    player_card_value += values[str(player_hand[int(i)].split(' ', 1)[0])]
                elif str(player_hand[i].split(' ',1)[0]) == 'A':
                    player_ace += 1
            if player_ace > 0:
                for i in range(player_ace):
                    if player_card_value <= 10:
                        player_card_value += 11
                    elif player_card_value > 10:
                        player_card_value += 1

            if splittable == 2:
                for i in range(len(split_hand)):
                    if str(split_hand[i].split(' ', 1)[0]) != 'A':
                        split_card_value += values[str(split_hand[int(i)].split(' ', 1)[0])]
                    elif str(split_hand[i].split(' ', 1)[0]) == 'A':
                        split_ace += 1
            if split_ace > 0:
                for i in range(split_ace):
                    if split_card_value <= 10:
                        split_card_value += 11
                    elif split_card_value > 10:
                        split_card_value += 1
            for i in range(len(bot_hand)):
                if str(bot_hand[i].split(' ',1)[0]) != 'A':
                    bot_card_value += values[str(bot_hand[int(i)].split(' ', 1)[0])]
                elif str(bot_hand[i].split(' ',1)[0]) == 'A':
                    bot_ace += 1
            if bot_ace > 0:
                for i in range(bot_ace):
                    if bot_card_value <= 10:
                        bot_card_value += 11
                    elif bot_card_value > 10:
                        bot_card_value += 1
            if splittable == 2:
                print('Your first hand value is ' + str(player_card_value) + '. ')
                print('Your second hand value is ' + str(split_card_value) + '. ')
            if main_hand_end != 1 and splittable != 2:
                print('Your hand value is ' + str(player_card_value) + '. ')
            if main_hand_end == 1:
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
                print('The dealer has a Blackjack! You lost ' + str(bet) + ' tokens.')
                game = 0
                break

            if splittable == 2:
                if player_card_value > 21:
                    print("Your first hand bust!")
                    first_hand_bust = 1
                if split_card_value > 21:
                    print("Your second hand bust!")
                    second_hand_bust = 1
                if first_hand_bust == 1 and second_hand_bust == 1:
                    print('Both of your hands busted. You lose!')
                    break
                if player_card_value == 21 and bot_card_value != 21:
                    print('Your first hand got to 21!')
                    first_hand_end = 1
                    money += (bet * 2)
                if split_card_value == 21 and bot_card_value != 21:
                    second_hand_end = 1
                    print('Your split hand got to 21!')
                    money += (bet * 2)
                if player_card_value == 21 and split_card_value == 21 and bot_card_value != 21:
                    break
                elif player_card_value == 21 and split_card_value < 21 and bot_card_value == 21:
                    print("Your first hand and the dealer's hand got to 21. \nYour first bet was returned. You lost your split hand.")
                    money += bet
                    break
                elif split_card_value == 21 and player_card_value < 21 and bot_card_value == 21:
                    print("Your split hand and the dealer's hand got to 21. \nYour split bet was returned. You lost your first hand.")
                    money += bet
                    break
                if bot_card_value > 21:
                    print('The dealer busts!')
                    if first_hand_bust != 1:
                        money += (bet * 2)
                    if second_hand_bust != 1:
                        money += (split_bet * 2)
                    break

                if first_hand_end == 1 and second_hand_end == 1:
                    main_hand_end = 1

                if main_hand_end == 1 and bot_card_value >= 17:
                    if player_card_value > bot_card_value:
                        print("Your first hand is bigger than the dealer's hand.")
                        money += bet * 2
                    elif bot_card_value > player_card_value:
                        print("The dealer's hand is bigger than your first hand.")
                    else:
                        print("Your first hand tied with the dealer. Your bet was returned.")
                        money += bet

                    if split_card_value > bot_card_value:
                        print("Your second hand is bigger than the dealer's hand.")
                        money += bet * 2
                        break

                    elif bot_card_value > split_card_value:
                        print("The dealer's hand is bigger than your second hand.")
                        break
                    else:
                        print("Your second hand tied with the dealer. Your bet was returned.")
                        money += bet
                        break

            else:
                if player_card_value == 21 and bot_card_value != 21:
                    print('You got 21! You win!')
                    money += (bet * 2)
                    break
                elif player_card_value == 21 and bot_card_value == 21:
                    print('You and the dealer got 21! You push and earn nothing.')
                    money += bet
                    break
                elif bot_card_value == 21 and player_card_value != 21:
                    print('The dealer got 21. You lost ' + str(bet) + ' tokens.')
                    break


                if player_card_value > 21:
                    print('You BUST! You lose!')
                    print("The dealer's card value was " + str(bot_card_value))
                    game = 0
                    break

                if bot_card_value > 21:
                    print('The dealer busts! You win!')
                    money += 2 * bet
                    break

                if main_hand_end == 1 and bot_card_value >= 17:
                    if player_card_value > bot_card_value:
                        print("Your hand is bigger than the dealer's hand.")
                        money += bet * 2
                        break
                    elif bot_card_value > player_card_value:
                        print("The dealer has a bigger hand. You lose.")
                        break
                    else:
                        print("You tied with the dealer. Your bet was returned.")
                        money += bet
                        break

            turn += 1
            if splittable == 1:
                while True:
                    player_action = input('You can [SPLIT] this hand, [HIT] or [STAND], or [DOUBLE] down.\n> ')
                    if player_action.upper() == 'SPLIT':
                        split_hand.append(player_hand[1])
                        player_hand.pop(1)
                        splittable = 2
                        card_selector = random.randint(0, len(used_deck) - 1)
                        player_hand.append(used_deck[card_selector])
                        used_deck.pop(card_selector)
                        card_selector = random.randint(0, len(used_deck) - 1)
                        split_hand.append(used_deck[card_selector])
                        used_deck.pop(card_selector)
                        print('\nYour first hand is ' + player_hand[0] + ' and ' + player_hand[1])
                        print('Your second hand is ' + split_hand[0] + ' and ' + split_hand[1])
                        break
                    elif player_action.upper() == 'HIT':
                        print('Drawing a card', end=' ')
                        time.sleep(0.5)
                        print('.', end=" ")
                        time.sleep(0.5)
                        print('.', end=" ")
                        time.sleep(0.5)
                        print('.')
                        time.sleep(0.5)
                        card_selector = random.randint(0, len(used_deck) - 1)
                        player_hand.append(used_deck[card_selector])
                        print('You drew the ' + used_deck[card_selector])
                        used_deck.pop(card_selector)
                        time.sleep(0.5)
                        print('Your cards are ' + player_hand[0], end = '')
                        for i in range((len(player_hand)-1)):
                            print(' and ' + player_hand[i+1], end = '')
                        print('\n', end='')
                        break
                    elif player_action.upper() == 'STAND':
                        print("You didn't draw a card.")
                        main_hand_end = 1
                        break
                    elif player_action.upper() == 'DOUBLE':
                        money -= bet
                        bet = bet * 2
                        print('Drawing a card', end=' ')
                        time.sleep(0.5)
                        print('.', end=" ")
                        time.sleep(0.5)
                        print('.', end=" ")
                        time.sleep(0.5)
                        print('.')
                        time.sleep(0.5)
                        card_selector = random.randint(0, len(used_deck) - 1)
                        player_hand.append(used_deck[card_selector])
                        print('You drew the ' + used_deck[card_selector])
                        used_deck.pop(card_selector)
                        time.sleep(0.5)
                        print('Your cards are ' + player_hand[0], end='')
                        for i in range((len(player_hand) - 1)):
                            print(' and ' + player_hand[i + 1], end='')
                        print('\n', end='')
                        main_hand_end = 1
                        break
                    else:
                        print('Please type out the action.')



            else:
                if main_hand_end == 0:
                    if splittable == 2:
                        if first_hand_end == 0 and first_hand_bust == 0:
                            while True:
                                first_hand_action = input('On your first hand, you can either [HIT] or [STAND].\n> ')
                                if first_hand_action.upper() == 'HIT':
                                    print('Drawing a card', end=" ")
                                    time.sleep(0.5)
                                    print('.', end=" ")
                                    time.sleep(0.5)
                                    print('.', end=" ")
                                    time.sleep(0.5)
                                    print('.')
                                    time.sleep(0.5)
                                    card_selector = random.randint(0, len(used_deck) - 1)
                                    player_hand.append(used_deck[card_selector])
                                    print('You drew the ' + used_deck[card_selector])
                                    used_deck.pop(card_selector)
                                    time.sleep(0.5)
                                    print('Your cards are ' + player_hand[0], end = '')
                                    for i in range((len(player_hand)-1)):
                                        print(' and ' + player_hand[i+1], end = '')
                                    print('\n', end = '')
                                    break
                                elif first_hand_action.upper() == 'STAND':
                                    print("You didn't draw a card on your first hand.")
                                    first_hand_end = 1
                                    break
                                else:
                                    print("Please type out the action.")
                        if second_hand_end == 0 and second_hand_bust == 0:
                            while True:
                                second_hand_action = input('On your second hand, you can either [HIT] or [STAND].\n> ')
                                if second_hand_action.upper() == 'HIT':
                                    print('Drawing a card', end=" ")
                                    time.sleep(0.5)
                                    print('.', end=" ")
                                    time.sleep(0.5)
                                    print('.', end=" ")
                                    time.sleep(0.5)
                                    print('.')
                                    time.sleep(0.5)
                                    card_selector = random.randint(0, len(used_deck) - 1)
                                    split_hand.append(used_deck[card_selector])
                                    print('You drew the ' + used_deck[card_selector])
                                    used_deck.pop(card_selector)
                                    time.sleep(0.5)
                                    print('Your cards are ' + split_hand[0], end = '')
                                    for i in range((len(split_hand)-1)):
                                        print(' and ' + split_hand[i+1], end = '')
                                    print("\n", end='')
                                    break
                                elif second_hand_action.upper() == 'STAND':
                                    print("You didn't draw a card on your second hand.")
                                    second_hand_end = 1
                                    break
                                else:
                                    print("Please type out the action.")

                    else:
                        while True:
                            if turn == 1 and money >= bet:
                                player_action = input('You can choose to [HIT] or [STAND], or you can [DOUBLE] down.\n> ')
                            else:
                                player_action = input('You can choose to [HIT] or [STAND].\n> ')
                            if player_action.upper() == 'HIT':
                                print('Drawing a card', end=" ")
                                time.sleep(0.5)
                                print('.', end=" ")
                                time.sleep(0.5)
                                print('.', end=" ")
                                time.sleep(0.5)
                                print('.')
                                time.sleep(0.5)
                                card_selector = random.randint(0, len(used_deck) - 1)
                                player_hand.append(used_deck[card_selector])
                                print('You drew the ' + used_deck[card_selector])
                                used_deck.pop(card_selector)
                                time.sleep(0.5)
                                print('Your cards are ' + player_hand[0], end = '')
                                for i in range((len(player_hand)-1)):
                                    print(' and ' + player_hand[i+1], end = '')
                                print('\n', end = '')
                                break
                            elif player_action.upper() == 'STAND':
                                print("You didn't draw a card.")
                                main_hand_end = 1
                                break
                            elif player_action.upper() == 'DOUBLE' and turn == 1 and money >= bet:
                                money -= bet
                                bet = bet * 2
                                print('Drawing a card', end =' ')
                                time.sleep(0.5)
                                print('.', end=" ")
                                time.sleep(0.5)
                                print('.', end=" ")
                                time.sleep(0.5)
                                print('.')
                                time.sleep(0.5)
                                card_selector = random.randint(0, len(used_deck) - 1)
                                player_hand.append(used_deck[card_selector])
                                print('You drew the ' + used_deck[card_selector])
                                used_deck.pop(card_selector)
                                time.sleep(0.5)
                                print('Your cards are ' + player_hand[0], end = '')
                                for i in range((len(player_hand)-1)):
                                    print(' and ' + player_hand[i+1], end = '')
                                print('\n', end = '')
                                main_hand_end = 1
                                break
                            else:
                                print("Please type out the action.")
                        time.sleep(0.5)
                        if bot_card_value >= 17:
                            print('The dealer stands and does not draw a card.')
                        elif bot_card_value < 17:
                            print('The Dealer is drawing', end=" ")
                            time.sleep(0.5)
                            print('.', end=" ")
                            time.sleep(0.5)
                            print('.', end=" ")
                            time.sleep(0.5)
                            print('.')
                            card_selector = random.randint(0, len(used_deck) - 1)
                            bot_hand.append(used_deck[card_selector])
                            # print('The dealer drew the ' + used_deck[card_selector])
                            used_deck.pop(card_selector)
                            # time.sleep(0.5)
                            # print("The dealer's cards are " + bot_hand[0], end='')
                            # for i in range((len(bot_hand) - 1)):
                            #     print(' and ' + bot_hand[i + 1], end='')
                            # print('\n', end = '')
                            time.sleep(0.5)
                elif bot_card_value < 17:
                    print('The Dealer is drawing', end=" ")
                    time.sleep(0.5)
                    print('.', end=" ")
                    time.sleep(0.5)
                    print('.', end=" ")
                    time.sleep(0.5)
                    print('.')
                    time.sleep(0.5)
                    card_selector = random.randint(0, len(used_deck) - 1)
                    bot_hand.append(used_deck[card_selector])
                    print('The dealer drew the ' + used_deck[card_selector])
                    used_deck.pop(card_selector)
                    time.sleep(0.5)
                    print("The dealer's cards are " + bot_hand[0], end='')
                    for i in range((len(bot_hand) - 1)):
                        print(' and ' + bot_hand[i + 1], end='')
                    print('\n', end='')
                    time.sleep(1)

print('You ran out of money. Type "R" to reset.')
reset = input('> ')
if reset == 'R':
    money = 500
    with open("money.txt", "w") as f:
        f.write(str(money))
else:
    print('Game over, reset your tokens in the txt file.')
