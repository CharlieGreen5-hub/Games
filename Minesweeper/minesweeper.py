import random

alphabet_values = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5,"G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15,}
default_board_mines = {3:4, 4:5, 5:6, 6:8, 7:10, 8:12, 9:15, 10:20, 11:25, 12:30, 13:33, 14:38, 15:40}
column_alphabet = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F",6:"G", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P",}





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

def flood_fill(row, col):
    global squares_left
    flood_fill_cells = [(row, col)]
    checked = []

    while len(flood_fill_cells) >= 1:
        temp_flood_fill_cells = []
        if (flood_fill_cells[-1][-2], flood_fill_cells[-1][-1]) not in checked:
            checked.append((flood_fill_cells[-1][-2], flood_fill_cells[-1][-1]))
            # Top left
            if flood_fill_cells[-1][-2] - 1 >= 0 and flood_fill_cells[-1][-1] - 1 >= 0:
                if unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] - 1] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] - 1]= unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] - 1]
                    if unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] - 1] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2] - 1, flood_fill_cells[-1][-1] - 1))
                        squares_left -= 1

            # Left
            if flood_fill_cells[-1][-1] - 1 >= 0:
                if unseen_matrix[flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] - 1] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] - 1] = unseen_matrix [flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] - 1]
                    if unseen_matrix[flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] - 1] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2], flood_fill_cells[-1][-1] - 1))
                        squares_left -= 1
            # Bottom Left
            if flood_fill_cells[-1][-2] + 1 <= board_size and flood_fill_cells[-1][-1] - 1 >= 0:
                if unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] - 1] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] - 1] = unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] - 1]
                    if unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] - 1] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2] + 1, flood_fill_cells[-1][-1] - 1))
                        squares_left -= 1
            # Bottom
            if flood_fill_cells[-1][-2] + 1 <= board_size:
                if unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1]] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1]] = unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1]]
                    if unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1]] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2] + 1, flood_fill_cells[-1][-1]))
                        squares_left -= 1
            # Bottom right
            if flood_fill_cells[-1][-2] + 1 <= board_size and flood_fill_cells[-1][-1] + 1 <= board_size:
                if unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] + 1] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] + 1] = unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] + 1]
                    if unseen_matrix[flood_fill_cells[-1][-2] + 1][flood_fill_cells[-1][-1] + 1] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2] + 1, flood_fill_cells[-1][-1] + 1))
                        squares_left -= 1
            # Right
            if flood_fill_cells[-1][-1] + 1 <= board_size:
                if unseen_matrix[flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] + 1] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] + 1] = unseen_matrix[flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] + 1]
                    if unseen_matrix[flood_fill_cells[-1][-2]][flood_fill_cells[-1][-1] + 1] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2], flood_fill_cells[-1][-1] + 1))
                        squares_left -= 1
            # Top right
            if flood_fill_cells[-1][-2] - 1 >= 0 and flood_fill_cells[-1][-1] + 1 <= board_size:
                if unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] + 1] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] + 1] = unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] + 1]
                    if unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1] + 1] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2] - 1, flood_fill_cells[-1][-1] + 1))
                        squares_left -= 1
            # Top
            if flood_fill_cells[-1][-2] - 1 >= 0:
                if unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1]] != -2:
                    displayed_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1]] = unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1]]
                    if unseen_matrix[flood_fill_cells[-1][-2] - 1][flood_fill_cells[-1][-1]] == '0':
                        temp_flood_fill_cells.append((flood_fill_cells[-1][-2] - 1, flood_fill_cells[-1][-1]))
                        squares_left -= 1
            flood_fill_cells.pop(-1)
            flood_fill_cells.extend(temp_flood_fill_cells)
        else:
            flood_fill_cells.pop(-1)


while True:
    unseen_matrix = []
    displayed_matrix = []
    flag_number = 0
    mines = []
    print("Welcome to Bumblebee's Minesweeper! Press [ENTER] to play!.")
    init_prompt = input("> ")
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
            if int(number_of_mines) > default_board_mines[board_size] * 2:
                print('Too many mines!')
            elif int(number_of_mines) < default_board_mines[board_size] / 2:
                print('Too few mines!')
            else:
                number_of_mines = int(number_of_mines)
                break
        else:
            number_of_mines = default_board_mines[board_size]
            break
    squares_left = board_size ** 2 - number_of_mines

    print_board(displayed_matrix)
    while True:
        init_guess = input("Which square will you dig first? (e.g. B3)\n> ")
        if len(init_guess) != 2:
            print('Please type the co-ordinate!')
        else:
            first_coordinates = list(init_guess.upper())
            if first_coordinates[1].isdigit():
                if first_coordinates[0] not in alphabet_values or int(first_coordinates[1]) - 1 not in column_alphabet:
                        print('Please type a valid coordinate!')
                else:
                    mine_first_coordinates = []
                    mine_first_coordinates.append(alphabet_values[first_coordinates[0]])
                    mine_first_coordinates.append(int(first_coordinates[1]) - 1)
                    squares_left -= 1
                    break
            else:
                print("Please type a valid coordinate!")

    # Mine randomising
    while len(mines) < number_of_mines:
        mine_x = random.randint(0,board_size)
        mine_y = random.randint(0,board_size)
        mine_iterator = [mine_x, mine_y]
        if mine_iterator not in mines and mine_iterator != mine_first_coordinates:
            mines.append([mine_x, mine_y])
            unseen_matrix[mine_x][mine_y] = -2

    # Number of mines around each square.
    for i, row in enumerate(unseen_matrix):
        for j, column in enumerate(row):
            if column != -2:
                mine_counter = 0
                # Top left
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
    displayed_matrix[mine_first_coordinates[0]][mine_first_coordinates[1]] = unseen_matrix[mine_first_coordinates[0]][mine_first_coordinates[1]]
    # if unseen_matrix[mine_first_coordinates[0]][mine_first_coordinates[1]] == '0':
    flood_fill(mine_first_coordinates[0], mine_first_coordinates[1])
    while True:
        print_board(displayed_matrix)
        if squares_left == 0:
            print('\nYou win!')
            break
        print("Type out which square you want to dig. If you want to flag a square, add 'F'. (e.g. B3 F). To remove a flag, add 'R'")
        input_square = input("> ")
        input_square_split = input_square.split()
        if len(input_square.split()) == 1 and len(input_square) == 2 or len(input_square) == 3:
            if input_square[1:].isdigit():
                if input_square[0].upper() not in alphabet_values or int(input_square[1:]) - 1 not in column_alphabet:
                    print('Please type a valid coordinate!')
                else:
                    input_coordinates = (alphabet_values[input_square[0].upper()], int(input_square[1:]) - 1)
                    # Must make sure you can't excavate flags
                    if displayed_matrix[input_coordinates[0]][input_coordinates[1]] == -1:
                        if unseen_matrix[input_coordinates[0]][input_coordinates[1]] == -2:
                            print('BOOOOMMM!!! You dug a mine! Game over.')
                            break
                        else:
                            displayed_matrix[input_coordinates[0]][input_coordinates[1]] = unseen_matrix[input_coordinates[0]][input_coordinates[1]]
                            if unseen_matrix[input_coordinates[0]][input_coordinates[1]] == "0":
                                flood_fill(input_coordinates[0], input_coordinates[1])
                            squares_left -= 1
                    elif displayed_matrix[input_coordinates[0]][input_coordinates[1]] == 'F':
                        print("There's a flag here! Remove it first!")
                    else:
                        print("You've already dug here!")
            else:
                print('Please type a valid coordinate!')
        elif len(input_square.split()) == 2 and input_square[-1].upper() == 'F' and input_square[0].upper() in alphabet_values and input_square_split[0][1:].isdigit():
            if int(input_square_split[0][1:]) in column_alphabet:
                if flag_number < number_of_mines:
                    input_coordinates = (alphabet_values[input_square[0]], int(input_square_split[0][1:]) - 1)
                    if displayed_matrix[input_coordinates[0]][input_coordinates[1]] == -1:
                        displayed_matrix[input_coordinates[0]][input_coordinates[1]] = 'F'
                        flag_number += 1
                    else:
                        print("You've already dug here!")
                else:
                    print('Too many flags!')
        elif len(input_square.split()) == 2 and input_square[-1].upper() == 'R' and input_square[0].upper() in alphabet_values and input_square_split[0][1:].isdigit():
            if int(input_square_split[0][1:]) in column_alphabet:
                input_coordinates = (alphabet_values[input_square[0].upper()], int(input_square_split[0][1:]) - 1)
                if displayed_matrix[input_coordinates[0]][input_coordinates[1]] == 'F':
                    displayed_matrix[input_coordinates[0]][input_coordinates[1]] = -1
                else:
                    print('There is no flag here!')
        else:
            print('Please type a valid command!')

    print_board(unseen_matrix)

