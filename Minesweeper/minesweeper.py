import random

alphabet_values = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5,"G":6, "H":7}
default_board_mines = {3:4, 4:5, 5:6, 6:8, 7:10, 8:12, 9:15, 10:20, 11:25, 12:30, 13:33, 14:38, 15:40}
column_alphabet = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F",6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P",}
unseen_matrix = []
displayed_matrix = []




row_list1 = []
row_list2 = []

def print_board(board):
    # print("      1     2     3     4     5     6     7     8")
    print("   ", end="")
    for number in range(board_size + 1):
        print("   " + str(number + 1) + "  ", end="")
    print('\n', end='')
    for i, row in enumerate(board):
        row_str = " " + column_alphabet[i] + " "
        if i == 0:
            # print('   ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐')
            print("   ┌─────", end="")
            for line in range(board_size):
                print("┬─────", end="")
            print('┐')
            for j, column in enumerate(row):
                if column == -1:
                    row_str += "│     "
                elif column == -2:
                    row_str += "│  M  "
                else:
                    row_str += "│  " + str(column) + "  "
            row_str += "│"
            print(row_str)
        else:
            # print("   ├─────┼─────┼─────┼─────┼─────┼─────┼─────┼─────┤")
            print("   ├─────", end="")
            for line in range(board_size):
                print("┼─────", end="")
            print("┤")
            for j, column in enumerate(row):
                if column == -1:
                    row_str += "│     "
                elif column == -2:
                    row_str += "│  M  "
                else:
                    row_str += "│  " + str(column) + "  "
            row_str += "│"
            print(row_str)
    # print('   └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘')
    print("   └─────", end="")
    for line in range(board_size):
        print("┴─────", end="")
    print("┘")

mines = []

print("Welcome to Bumblebee's Minesweeper! Press [I] for instructions, or [ENTER] to play!.")
init_prompt = input("> ")
if init_prompt == "I":
    print("[INSTRUCTIONS WILL BE HERE]")
else:
    while True:
        board_size = input("How large should the board be? Input nothing for the default of 8x8. Please input one number (Board is square).\n> ")
        if board_size.isdigit():
            if int(board_size) > 16:
                print('Too large!')
            elif int(board_size) < 4:
                print('Too small!')
            else:
                board_size = int(board_size)-1
                break
        else:
            board_size = 7
            break

    for i in range(board_size + 1):
        row_list1 = []
        row_list2 = []
        for j in range(board_size + 1):
            row_list1.append(0)
            row_list2.append(-1)
        unseen_matrix.append(row_list1)
        displayed_matrix.append(row_list2)

    while True:
        number_of_mines = input("How many mines? Input nothing to use the default for this board size.\n> ")
        if number_of_mines.isdigit():
            if int(number_of_mines) > (board_size+1)*(board_size+1)/2:
                print('Too many mines!')
            elif int(number_of_mines) < (board_size+1)*(board_size+1)/10:
                print('Too few mines!')
            else:
                number_of_mines = int(number_of_mines)
                break
        else:
            number_of_mines = default_board_mines[board_size]
            break

    print_board(displayed_matrix)
    while True:
        init_guess = input("Which square will you dig first? (e.g. B3)\n> ")
        if len(init_guess) != 2:
            print('Please type the co-ordinate!')
        else:
            first_coordinates = list(init_guess.upper())
            if first_coordinates[0] not in alphabet_values or int(first_coordinates[1]) - 1 not in column_alphabet:
                print('Please type a valid coordinate!')
            else:
                mine_first_coordinates = []
                mine_first_coordinates.append(alphabet_values[first_coordinates[0]])
                mine_first_coordinates.append(int(first_coordinates[1]))
                break


    while len(mines) < number_of_mines:
        mine_x = random.randint(0,board_size)
        mine_y = random.randint(0,board_size)
        mine_iterator = [mine_x, mine_y]
        if mine_iterator not in mines and mine_iterator != mine_first_coordinates:
            mines.append([mine_x, mine_y])
            unseen_matrix[mine_x][mine_y] = -2

    for i, row in enumerate(unseen_matrix):
        for j, column in enumerate(row):
            if column != -2:
                mine_counter = 0
                if i - 1 >= 0 and j - 1 >= 0:
                    if unseen_matrix[i-1][j-1] == -2:
                        mine_counter += 1
                # Left
                if j - 1 >= 0:
                    if unseen_matrix[i][j-1] == -2:
                        mine_counter += 1
                # Bottom Left
                if i + 1 <= board_size and j - 1 >= 0:
                    if unseen_matrix[i+1][j-1] == -2:
                        mine_counter += 1
                # Bottom
                if i + 1 <= board_size:
                    if unseen_matrix[i+1][j] == -2:
                        mine_counter += 1
                # Bottom right
                if i + 1 <= board_size and j + 1 <= board_size:
                    if unseen_matrix[i+1][j+1] == -2:
                        mine_counter += 1
                # Right
                if j + 1 <= board_size:
                    if unseen_matrix[i][j+1] == -2:
                        mine_counter += 1
                # Top right
                if i - 1 >= 0 and j + 1 <= board_size:
                    if unseen_matrix[i-1][j+1] == -2:
                        mine_counter += 1
                # Top
                if i - 1 >= 0:
                    if unseen_matrix[i-1][j] == -2:
                        mine_counter += 1
                unseen_matrix[i][j] = str(mine_counter)



print_board(unseen_matrix)

