import random
MIN_NUMBER = 1
MAX_NUMBER = 75
MIN_GRID = 3
MAX_GRID = 5
PLAYERS = 2

def draw_random_number(numbers):
    random_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    while random_num in numbers:
        random_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    return random_num

def cross_out_number(grid, number):
    find_index = grid.index(number)
    grid[find_index] = "X"
    return grid

def grid_completed(grid):
    for i in grid:
        if i != "X":
            return False
    return True

def print_grid(grid, grid_size, name):
    print("{}'s grid:".format(name))
    for i in range(0, len(grid), grid_size):
        for j in range(grid_size):
            if grid[i + j] == "X":
                print("{:>3s}".format(grid[i + j]), end="")
            else:
                print("{:3d}".format(grid[i + j]), end="")
        print()
    print()

def create_player(grid_size, name):
    number_list = []
    print("{}, choose different numbers between 1-75.".format(name))
    print("Enter a number:")
    while len(number_list) != grid_size * grid_size:
        num = int(input(""))
        if MIN_NUMBER <= num <= MAX_NUMBER and num not in number_list:
            number_list.append(num)
            if len(number_list) != grid_size * grid_size:
                print("Enter a number:")
            else:
                print("The numbers were added successfully.")
        elif num in number_list:
            print("The number is already in the grid. Choose a different number:")
        elif num < MIN_NUMBER or num > MAX_NUMBER:
            print("The number must be between 1 and 75. Choose another number:")
    print_grid(number_list, grid_size, name)
    return number_list

def play_game(player1, player2, seed_number, player1_name, player2_name, grid_size):
    old_num = []
    status1, status2 = False, False
    random.seed(seed_number)
    print("Game starts.")
    while True:
        input("Press enter to draw a number.")
        draw = draw_random_number(old_num)
        old_num.append(draw)
        print("")
        print("The drawn number is {}.".format(draw))

        if draw in player1:
            player1 = cross_out_number(player1, draw)
            print("{} crossed out a number {}.".format(player1_name, draw))
        if draw in player2:
            player2  = cross_out_number(player2, draw)
            print("{} crossed out a number {}.".format(player2_name, draw))
        print("")
        print_grid(player1, grid_size, player1_name)
        print_grid(player2, grid_size, player2_name)

        if grid_completed(player1):
            print("{} has crossed out all the numbers.".format(player1_name))
            print("{} won!".format(player1_name))
            status1 = True
        if grid_completed(player2):
            print()
            print("{} has crossed out all the numbers.".format(player2_name))
            print("{} won!".format(player2_name))
            status2 = True
        if status1 is True or status2 is True:
            print("Game ended.")
            break

def main():
    print("Welcome to play bingo!")
    ask_size = int(input("Enter the size of one side of the grid. The size must be between 3 and 5:\n"))
    while True:
        if MIN_GRID <= ask_size <= MAX_GRID:
            break
        else:
            print("The number must be between 3 and 5.")
            ask_size = int(input("Enter a size:\n"))
    ask_seed = int(input("Enter a seed:\n"))
    player1_name = input("Enter the name of the 1. player:\n")
    player_1 = create_player(ask_size, player1_name)
    player2_name = input("Enter the name of the 2. player:\n")
    player_2 = create_player(ask_size, player2_name)
    play_game(player_1, player_2, ask_seed, player1_name, player2_name, ask_size)


main()


