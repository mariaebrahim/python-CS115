class Board:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.board = []
        for row in range(width):
            board += [' ']
            for colum in range(1, height):
                board += ['\n ']

    def __str__(self):
        for space in self.width:
            if space  == 0 or space == self.width:
                self.board.append('| |')
            else:
                self.baord.append(' |')

    def allowsMove(self, col):

