import random


print("Welcome to Bumblebee's hangman! Press [I] for instructions and to view the wordlist, [C] to input a custom wordlist, or [ENTER] to play with the default list.")


words = ["BICYCLE", "LUGGAGE", "SUBWAY", "UMBRELLA", "PASSPORT", "CALENDAR", "KEYHOLE", "BACKPACK", "HEADLIGHT", "MAGNIFYING", "BLIZZARD", "MAGNIFYING", "BLIZZARD", "VOLCANO", "WILDERNESS", "THUNDER","HURRICANE", "ECLIPSE", "GLACIER", "WATERFALL", "TORNADO", "AVALANCHE", "CHAMELEON", "PLATYPUS", "GORILLA", "FLAMINGO", "DOLPHIN", "SCORPION", "SQUIRREL", "OCTOPUS", "KANGAROO", "CHEETAH", "SPAGHETTI", "PINEAPPLE", "CHOCOLATE", "BARBECUE", "CINNAMON", "GUACAMOLE", "AVOCADO", "CROISSANT", "BROCOLLI", "SANDWICH", "WHISPER", "JOURNEY", "ADVENTURE", "MYSTERY", "LAUGHTER", "TREASURE", "CARNIVAL", "FESTIVAL", "GYMNASTICS", "ASTRONAUT"]

symbols = {0:("═╦═══╗",
              "     ║",
              "     ║",
              "     ╩"),
           1: ("═╦═══╗",
               " O   ║",
               "     ║",
               "     ╩"),
           2: ("═╦═══╗",
               " O   ║",
               " ┼   ║",
               "     ╩"),
           3: ("═╦═══╗",
               " O   ║",
               "┌┼   ║",
               "     ╩"),
           4: ("═╦═══╗",
               " O   ║",
               "┌┼┐  ║",
               "     ╩"),
           5: ("═╦═══╗",
               " O   ║",
               "┌┼┐  ║",
               "/    ╩"),
           6: ("═╦═══╗",
               " O   ║",
               "┌┼┐  ║",
               "/ \  ╩"),
           }
