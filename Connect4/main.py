PLAYER1_SYMBOL = "X"
PLAYER2_SYMBOL = "O"

# Minimal grid size is 4x4
GRID_HEIGHT = 4
GRID_WIDTH = 15

game_grid = [[' ' for i in range(GRID_WIDTH)] for x in range(GRID_HEIGHT)]

game_finished: bool = False


# Prints game grid
def print_game_grid(grid):
    width = len(grid[0])
    height = len(grid)
    for i in range(height):
        print("____" * width)
        for a in range(width):
            print(f"| {grid[i][a]} ", end="")
        print("|")
    print("____" * width)
    for b in range(width):
        print(f"  {b + 1} ", end="")
    print("")


# Makes a move given position and player symbol
def make_move(pos, symbol):
    lowest_spot = len(game_grid) - 1

    # Case when the column is empty
    if game_grid[lowest_spot][pos] == " ":
        game_grid[lowest_spot][pos] = symbol

    # Case when someting is already placed in this column
    else:
        current_h = 0
        while game_grid[current_h + 1][pos] == " ":
            current_h += 1
        game_grid[current_h][pos] = symbol


# Checks if move is legal, is there space left in a column and does it fit in a grid
def check_move(pos):
    if pos > GRID_WIDTH:
        return False
    if game_grid[0][pos] != " ":
        return False
    return True


# Asks player for a move until it's legal and then executes it
def player_turn(symbol):
    player_move = int(input(f"Input player {symbol} move: ")) - 1
    while not check_move(player_move):
        player_move = int(input("This move is incorrect, please choose another: ")) - 1
    make_move(player_move, symbol)

    print_game_grid(game_grid)
    if check_for_win(symbol):
        print(f"Congrats {symbol}, you won the game!")


def check_for_win(symbol):
    global game_finished

    # check horizontally
    for row in game_grid:
        current_len = 0
        for box in row:
            if box == symbol:
                current_len += 1
                if current_len >= 4:
                    game_finished = True
                    return True
            else:
                current_len = 0

    # check vertically:
    for a in range(GRID_WIDTH):
        current_len = 0
        for b in range(GRID_HEIGHT):
            if game_grid[b][a] == symbol:
                current_len += 1
                if current_len >= 4:
                    game_finished = True
                    return True
            else:
                current_len = 0

    # check diagonally:
    for a in range(GRID_HEIGHT):
        for b in range(GRID_WIDTH):
            help_a = a
            help_b = b
            current_len = 0
            if game_grid[a][b] == symbol:
                # check right up:
                current_len += 1
                # check if you don't run out of game grid before checking for next box
                while help_a - 1 >= 0 and help_b + 1 < GRID_WIDTH:
                    help_a -= 1
                    help_b += 1
                    if game_grid[help_a][help_b] == symbol:
                        current_len += 1
                        if current_len >= 4:
                            game_finished = True
                            return True
                    else:
                        current_len = 0

                # check right down:
                help_a = a
                help_b = b
                current_len = 1
                # check if you don't run out of game grid before checking for next box
                while help_a + 1 < GRID_HEIGHT and help_b + 1 < GRID_WIDTH:
                    help_a += 1
                    help_b += 1
                    if game_grid[help_a][help_b] == symbol:
                        current_len += 1
                        if current_len >= 4:
                            game_finished = True
                            return True
                    else:
                        current_len = 0

    return False


while not game_finished:
    player_turn(PLAYER1_SYMBOL)
    if not game_finished:
        player_turn(PLAYER2_SYMBOL)
