import os

class UI:

    def __init__(self):
        self.input_prompt_message = "Use W, A, S, D to move (up, left, down, right) or Q to exit: \n"
        self.valid_inputs = ["w", "a", "s", "d", "q"]
        self.prompt_to_reinput = f"Invalid response.\n{self.input_prompt_message}"

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
        user_input = input(self.input_prompt_message)
        user_input = self.if_invalid_input_request_new_input(user_input, board)
        return user_input

    def if_invalid_input_request_new_input(self, user_input, board):
        while user_input not in self.valid_inputs:
            self.print_board(board)
            user_input = input(self.prompt_to_reinput)
        return user_input
