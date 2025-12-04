class Board:
    def __init__(self):
        self.data = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def display(self):
        print("\n ___ ___ ___ | ___ ___ ___ | ___ ___ ___" \
        "      \n             |             |            ")

    def set_cell(self, x, y, marker):
        """ Updates the board with the marker specified, i.e. 'x' or 'o'.
        Returns True if successful. """
        self.data[x][y] = marker
        return True


board = Board()
board.display()
#board.set_cell(1, 2, 'x')
#board.display()