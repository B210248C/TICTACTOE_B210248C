class TicTacToe:
    def __init__(self):
        self.ttt = {
            'top-l': ' ', 'top-c': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-c': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-c': ' ', 'bot-r': ' '
        }

    # Print the TicTacToe Board
    def print_ttt_board(self):
        print()
        print(self.ttt['top-l'], '|', self.ttt['top-c'], '|', self.ttt['top-r'])
        print("--+---+---")
        print(self.ttt['mid-l'], '|', self.ttt['mid-c'], '|', self.ttt['mid-r'])
        print("--+---+---")
        print(self.ttt['bot-l'], '|', self.ttt['bot-c'], '|', self.ttt['bot-r'])
        print()
        
    # X turn to play the game
    def x_turn(self):
        while True:
            getPosition = input("Now it is X\'s turn to enter the position:")
            if not self.getRole("X", getPosition):
                if self.check_win_or_not("X"):
                    break
                else:
                    self.o_turn()
                    return

    # O turn to play the game
    def o_turn(self):
        while True:
            getPosition = input("Now it is O\'s turn to enter the position:")
            if not self.getRole("O", getPosition):
                if self.check_win_or_not("O"):
                    break
                else:
                    self.x_turn()
                    return

    # Get their roles, which is X or O. Check if it is filled,empty, or exist position and place them in the right position
    def getRole(self, roles_position, place_position):
        if place_position in self.ttt:
            if self.ttt[place_position] == " ":
                self.ttt[place_position] = roles_position
                self.print_ttt_board()
                return False
            else:
                print("This position is filled. Please re-enter.")
                print()
                return True
        else:
            if place_position != "":
                print("Please enter the correct position.")
                print()
                return True
            else:
                print("Cannot be empty. Please enter a position.")
                print()
                return True
        
    # Check who wins or draws
    def check_win_or_not(self, roles):
        if (self.ttt['top-l'] == self.ttt['top-c'] == self.ttt['top-r'] == roles) or \
           (self.ttt['mid-l'] == self.ttt['mid-c'] == self.ttt['mid-r'] == roles) or \
           (self.ttt['bot-l'] == self.ttt['bot-c'] == self.ttt['bot-r'] == roles) or \
           (self.ttt['top-l'] == self.ttt['mid-l'] == self.ttt['bot-l'] == roles) or \
           (self.ttt['top-c'] == self.ttt['mid-c'] == self.ttt['bot-c'] == roles) or \
           (self.ttt['top-r'] == self.ttt['mid-r'] == self.ttt['bot-r'] == roles) or \
           (self.ttt['top-l'] == self.ttt['mid-c'] == self.ttt['bot-r'] == roles) or \
           (self.ttt['top-r'] == self.ttt['mid-c'] == self.ttt['bot-l'] == roles):
            print('Congratulations to ' + roles + "! You win the game!")
            return True
        else:
            if all(value != ' ' for value in self.ttt.values()):
                print('No winners. It is a draw game!')
                return True
        return False