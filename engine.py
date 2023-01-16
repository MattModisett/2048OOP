from board import *
from ui import *

class Engine:

    def __init__(self):
        self.ui = UI()
        self.board = Board()
        self.play_game = True

    def runtime(self):

        for i in range(2):
            self.board.add_random_number()

        while (play_game):
            self.ui.print_board(self.board)
            user_input = self.ui.player_move_input_wasdq(self.board)
            self.board.det_shift_direction_do(user_input)

            if user_input.lower() == 'q':
                play_game = False
            else:
                self.board.det_shift_direction_do(user_input)
                play_game = self.board.check_end_of_game(play_game)

                if play_game:
                    self.board.add_random_number()
