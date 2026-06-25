import random


column_alphabet = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F",6:"G", 7:"H"}
unseen_matrix = [[0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0]]
displayed_matrix = [[-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1],
                    [-1,-1,-1,-1,-1,-1,-1,-1]]

def print_board(board):
    print("      1     2     3     4     5     6     7     8")
    for i, row in enumerate(board):
        row_str = " " + column_alphabet[i] + " "
        if i == 0:
            print('   ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐')
            for column in row:
                if column == -1:
                    row_str += "│     "
                else:
                    row_str += "│  " + str(column) + "  "
            row_str += "│"
            print(row_str)
        else:
            print("   ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
            for column in row:
                if column == -1:
                    row_str += "│     "
                else:
                    row_str += "│  " + str(column) + "  "
            row_str += "│"
            print(row_str)
    print('   └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘')

mines = []

print("Welcome to Bumblebee's Minesweeper! Press [I] for instructions, or [ENTER] to play!.")
init_prompt = input("> ")
if init_prompt == "I":
    print("[INSTRUCTIONS WILL BE HERE]")
else:
    while True:
        number_of_mines = input("How many mines? Input nothing to use the default of TEN.\n> ")
        if number_of_mines.isdigit():
            number_of_mines = int(number_of_mines)
            break
        else:
            number_of_mines = 10
            break

    while len(mines) < number_of_mines:
        mine_x = random.randint(0,7)
        mine_y = random.randint(0,7)
        if str(mine_x) + str(mine_y) not in mines:
            mines.append(str(mine_x) + str(mine_x))
            unseen_matrix[mine_x][mine_y] = -1




print_board(displayed_matrix)


