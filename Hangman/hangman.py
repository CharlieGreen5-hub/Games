import random
import time
import sys

words = ["BICYCLE", "LUGGAGE", "SUBWAY", "UMBRELLA", "PASSPORT", "CALENDAR", "KEYHOLE", "BACKPACK", "HEADLIGHT", "MAGNIFYING", "BLIZZARD", "MAGNIFYING", "BLIZZARD", "VOLCANO", "WILDERNESS", "THUNDER","HURRICANE", "ECLIPSE", "GLACIER", "WATERFALL", "TORNADO", "AVALANCHE", "CHAMELEON", "PLATYPUS", "GORILLA", "FLAMINGO", "DOLPHIN", "SCORPION", "SQUIRREL", "OCTOPUS", "KANGAROO", "CHEETAH", "SPAGHETTI", "PINEAPPLE", "CHOCOLATE", "BARBECUE", "CINNAMON", "GUACAMOLE", "AVOCADO", "CROISSANT", "BROCOLLI", "SANDWICH", "WHISPER", "JOURNEY", "ADVENTURE", "MYSTERY", "LAUGHTER", "TREASURE", "CARNIVAL", "FESTIVAL", "GYMNASTICS", "ASTRONAUT"]


symbols = {0:("  ═╦═══╗",
              "       ║",
              "       ║",
              "       ╩"),
           1: ("  ═╦═══╗",
               "   O   ║",
               "       ║",
               "       ╩"),
           2: ("  ═╦═══╗",
               "   O   ║",
               "   ┼   ║",
               "       ╩"),
           3: ("  ═╦═══╗",
               "   O   ║",
               "  ┌┼   ║",
               "       ╩"),
           4: ("  ═╦═══╗",
               "   O   ║",
               "  ┌┼┐  ║",
               "       ╩"),
           5: ("  ═╦═══╗",
               "   O   ║",
               "  ┌┼┐  ║",
               "  /    ╩"),
           6: ("  ═╦═══╗",
               "   O   ║",
               "  ┌┼┐  ║",
               "  / \\  ╩")}

while True:
    print("Welcome to Bumblebee's hangman! Press [I] for instructions and to view the wordlist, [C] to input a custom wordlist, or [ENTER] to play with the default list.")
    init_prompt = input("> ")
    if init_prompt.upper() == "I":
        print("""1) Type in one letter at a time
        
        
        """)
        time.sleep(0.5)
        for i in range(len(words) - 1):
            print(words[i] + ' ', end="")
        print(words[-1])
    elif init_prompt.upper() == "C":
        while True:
            print('Please input your list of words, separated by spaces, or press [M] to enter them one at a time. Press [X] to return to the menu.')
            input_words = input("> ")
            if input_words.upper() == "M":
                words = []
                print("Enter each word, then press [ENTER]. Enter [X] when done.")
                while True:
                    input_word = input("> ")
                    if input_word.upper() == "X":
                        if len(words) < 5:
                            print("Not enough words! Please input more.")
                        else:
                            break
                    else:
                        if len(input_word) < 3:
                            print("Word not long enough! Please input a longer word!")
                        elif input_word in words:
                            print("This word has already been added to the list!")
                        elif input_word.isalpha() == 'False':
                            print("Please do not input spaces, numbers, or special characters!")
                        else:
                            words.append(input_word.upper())
            elif input_words.upper() == "X":
                pass
            else:
                words = input_words.upper().split()
                if len(words) < 5:
                    print("Not enough words! Please input more.")
                else:
                    break
    else:
        while True:
            hangman_word_selector = random.randint(0, len(words) - 1)
            word = words[hangman_word_selector]
            mistakes = 0
            attempt = []
            for space in range(len(word)):
                attempt.append("_")


            # Turn Sequence
            while True:
                print("════════════════════")
                for line in symbols[mistakes]:
                    print(line)
                for char in range(len(attempt)):
                    print(attempt[char], end=" ")
                while True:
                    guess = input("\nGuess a letter: ").upper()
                    if guess.isalpha() and guess not in attempt and len(guess) == 1:
                        break
                    else:
                        if guess.isalpha():
                            print('You have guessed this letter already.')
                        else:
                            print('Please enter a singular letter.')
                if guess in word:
                    if word.count(guess) > 1:
                        for letter in range(len(word)):
                            if guess == word[letter]:
                                attempt[letter] = word[letter]
                        print('The letter ' + guess + ' appeared ' + str(word.count(guess)) + ' times.')
                    else:
                        position = word.find(guess)
                        attempt[position] = word[position]
                        print('The letter ' + guess + ' was in the word.')
                else:
                    print('The letter was not in the word.')
                    mistakes += 1
                if "_" not in attempt:
                    print("════════════════════")
                    for line in symbols[mistakes]:
                        print(line)
                    print("You win! You got " + str(mistakes) + " guesses wrong.")
                    if input('Play again?\n> ') == 'Y':
                        break
                    else:
                        print('Thanks for playing!')
                        sys.exit(0)
                if mistakes == 6:
                    print("════════════════════")
                    for line in symbols[mistakes]:
                        print(line)
                    print("You lost! The word was " + word)
                    if input('Play again?\n> ') == 'Y':
                        break
                    else:
                        print('Thanks for playing!')
                        sys.exit(0)

