import random


class Player:
    def __init__(self, letter):
        #letter is X or O
        self.letter = letter

    # we want all players to get their move given a game
    def get_move(self, game):
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = int(input("Your turn. Input move (0-8):"))
            # below we're going to check that this is a correct value by trying to cost
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is unavailable on the board , we also say its invalid
            try:
                if square not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid spot or spot is occupied. Try Again\n")
        return square
