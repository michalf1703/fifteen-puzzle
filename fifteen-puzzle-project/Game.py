class Game:
    def __init__(self, board):
        self.board = board

    def isgoal(self, board):
        return self.board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

    def neighbours(self, board):
        neighbours = []
        row, col = self.find_empty_cell(board)
        if row > 0:
            new_board = self.copy_board(board)
            new_board[row][col], new_board[row - 1][col] = new_board[row - 1][col], new_board[row][col]
            neighbours.append(new_board)
        if row < 3:
            new_board = self.copy_board(board)
            new_board[row][col], new_board[row + 1][col] = new_board[row + 1][col], new_board[row][col]
            neighbours.append(new_board)
        if col > 0:
            new_board = self.copy_board(board)
            new_board[row][col], new_board[row][col - 1] = new_board[row][col - 1], new_board[row][col]
            neighbours.append(new_board)
        if col < 3:
            new_board = self.copy_board(board)
            new_board[row][col], new_board[row][col + 1] = new_board[row][col + 1], new_board[row][col]
            neighbours.append(new_board)
        return neighbours

    def find_empty_cell(self, board):
        for row in range(4):
            for col in range(4):
                if board[row][col] == 0:
                    return row, col

    def copy_board(self, board):
        return [row[:] for row in board]
