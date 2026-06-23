import random
import time

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


