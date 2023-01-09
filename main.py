import os
import random

# This is a dummy comment.

class Cell:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        self.value += other.value
        other.value = 0


class Board:

    def __init__(self):
        self.matrix = self.init_board()

    def init_board(self):
        matrix = []
        for i in range(4):
            row = []
            for j in range(4):
                cell = Cell(0)
                row.append(cell)
            matrix.append(row)
        return matrix

    def add_random_number(self):
        new_numbers = [2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2]
        next_number = new_numbers[random.randint(0, 12)]
        random_x_coor = random.randint(0, 3)
        random_y_coor = random.randint(0, 3)
        while (self.matrix[random_x_coor][random_y_coor].value > 0):
            random_x_coor = random.randint(0, 3)
            random_y_coor = random.randint(0, 3)
        self.matrix[random_x_coor][random_y_coor].value = next_number

    def det_shift_direction_do(self, user_input_direction):
        is_up = user_input_direction.lower() == "w"
        is_down = user_input_direction.lower() == "s"
        is_left = user_input_direction.lower() == "a"
        is_right = user_input_direction.lower() == "d"
        board_hash = Board()
        for i in range(0, 3):
            if is_up:    self.shift_up(board_hash)
            if is_down:  self.shift_down(board_hash)
            if is_left:  self.shift_left(board_hash)
            if is_right: self.shift_right(board_hash)

    def shift_right(self, board_hash):
        for y in range(0, 4):
            for x in range(2, -1, -1):
                if (self.matrix[y][x + 1].value == self.matrix[y][x].value and self.matrix[y][x].value > 0 and
                        board_hash.matrix[y][x].value == 0):
                    self.matrix[y][x + 1] + self.matrix[y][x]
                    board_hash.matrix[y][x + 1].value = 1
                    board_hash.matrix[y][x].value = 0
                elif (self.matrix[y][x + 1].value == 0):
                    self.matrix[y][x + 1] + self.matrix[y][x]
                    board_hash.matrix[y][x + 1].value = board_hash.matrix[y][x].value
                    board_hash.matrix[y][x].value = 0

    def shift_left(self, board_hash):
        for x in range(1, 4):
            for y in range(0, 4):
                if (self.matrix[y][x - 1].value == self.matrix[y][x].value and self.matrix[y][x].value > 0 and
                        board_hash.matrix[y][x].value == 0):
                    self.matrix[y][x - 1] + self.matrix[y][x]
                    board_hash.matrix[y][x - 1].value = 1
                    board_hash.matrix[y][x].value = 0
                elif (self.matrix[y][x - 1].value == 0):
                    self.matrix[y][x - 1] + self.matrix[y][x]
                    board_hash.matrix[y][x - 1].value = board_hash.matrix[y][x].value
                    board_hash.matrix[y][x].value = 0

    def shift_down(self, board_hash):
        for y in range(2, -1, -1):
            for x in range(0, 4):
                if (self.matrix[y + 1][x].value == self.matrix[y][x].value and self.matrix[y][x].value > 0 and
                        board_hash.matrix[y][x].value == 0):
                    self.matrix[y + 1][x] + self.matrix[y][x]
                    board_hash.matrix[y + 1][x].value = 1
                    board_hash.matrix[y][x].value = 0
                elif (self.matrix[y + 1][x].value == 0):
                    self.matrix[y + 1][x] + self.matrix[y][x]
                    board_hash.matrix[y + 1][x].value = board_hash.matrix[y][x].value
                    board_hash.matrix[y][x].value = 0

    def shift_up(self, board_hash):
        for y in range(1, 4):
            for x in range(0, 4):
                if (self.matrix[y - 1][x].value == self.matrix[y][x].value and self.matrix[y][x].value > 0 and
                        board_hash.matrix[y][x].value == 0):
                    self.matrix[y - 1][x] + self.matrix[y][x]
                    board_hash.matrix[y - 1][x].value = 1
                    board_hash.matrix[y][x].value = 0
                elif (self.matrix[y - 1][x].value == 0):
                    self.matrix[y - 1][x] + self.matrix[y][x]
                    board_hash.matrix[y - 1][x].value = board_hash.matrix[y][x].value
                    board_hash.matrix[y][x].value = 0

    def check_end_of_game(self, play_game):
        #fill_board(board)           #Temp code for programming purposes
        #os.system('cls')
        #print_board(board)
        if self.is_game_lost():
            play_again = self.does_player_want_another_game()
            play_game = self.restart_game_or_exit(play_again, play_game)
        return play_game

    def restart_game_or_exit(self, play_again, play_game):
        if play_again == 'n':
            play_game = False
        if play_again == 'y':
            self.matrix.clear()
            self.init_board()
            self.add_random_number()
        return play_game

    def does_player_want_another_game(self):
        play_again = input("No more available moves. Game over. Play again? (y/n)")
        while not (play_again.lower() == "y" or play_again.lower() == "n"):
            play_again = input("Invalid input. Play again? (y/n)")
        return play_again

    def is_game_lost(self):
        game_lost = True
        for row in self.matrix:
            for cell in row:
                if cell.value == 0:
                    game_lost = False
                    return game_lost
        return game_lost



class UI:

    def print_board(self, board):
        os.system('cls')
        for row in board.matrix:
            for cell in row:
                if cell.value == 0:
                    print(f"[{' ': ^4}]", end="")
                else:
                    print(f"[{cell.value: ^4}]", end="")
            print()

    def player_move_input_wasdq(self, board):
        user_input = input("Use W, A, S, D to move (up, left, down, right): \n")
        while not (user_input.lower() == "w" or
                   user_input.lower() == "a" or
                   user_input.lower() == "s" or
                   user_input.lower() == "d" or
                   user_input.lower() == "q"):
            self.print_board()
            user_input = input("Invalid response.\nUse W, A, S, D to move (up, left, down, right): \n")
        return user_input



def runtime():
    ui = UI()
    board = Board()
    play_game = True
    for i in range(2):
        board.add_random_number()

    while (play_game):
        ui.print_board(board)
        user_input = ui.player_move_input_wasdq(board)
        board.det_shift_direction_do(user_input)

        if user_input.lower() == 'q':
            play_game = False
        else:
            board.det_shift_direction_do(user_input)
            play_game = board.check_end_of_game(play_game)

            if play_game:
                board.add_random_number()




def main():
    runtime()


if __name__ == '__main__':
    main()
