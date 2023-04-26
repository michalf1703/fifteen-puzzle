import copy

class Board:
    def __init__(self, columns, rows, puzzle, priority):
        self.columns = columns
        self.rows = rows
        self.board = puzzle
        self.parent = None
        self.last_move = ''
        self.priority = priority
        self.metrics = None
        self.neighbors = []
        self.depth = 0

    def get_neighbors(self):
        return self.neighbors

    def __copy__(self):
        new_board = copy.deepcopy(self.board)
        new_instance = Board(self.columns, self.rows, new_board, self.priority)
        new_instance.last_move = self.last_move
        new_instance.parent = self
        new_instance.depth = self.depth + 1
        return new_instance

    def __hash__(self):
        return hash(tuple(self.board))

    def is_goal(self):
        size = self.w * self.h
        if int(self.tab[size - 1]) != 0:
            return False

        expected_nums = list(range(1, size))
        actual_nums = [int(self.tab[i]) for i in range(size - 1)]

        return expected_nums == actual_nums

    def is_solved(self):
        solution = list(range(1, self.rows * self.columns)) + [0]
        return tuple(self.board) == tuple(solution)

    def change_state(self, move, index):
        new_board = self.__copy__()
        new_board.last_move = move
        if move == "U" and index - self.columns >= 0:
            new_board.board[index - self.columns], new_board.board[index] = new_board.board[index], new_board.board[index - self.columns]
        elif move == "D" and index + self.columns < self.rows * self.columns:
            new_board.board[index + self.columns], new_board.board[index] = new_board.board[index], new_board.board[index + self.columns]
        elif move == "R" and (index + 1) % self.columns != 0:
            new_board.board[index + 1], new_board.board[index] = new_board.board[index], new_board.board[index + 1]
        elif move == "L" and index % self.columns != 0:
            new_board.board[index - 1], new_board.board[index] = new_board.board[index], new_board.board[index - 1]
        return new_board

    def move(self):
        index = self.board.index(0)
        for move in self.priority:
            if move == "U" and self.last_move != "D":
                self.neighbors.append(self.change_state(move, index))
            elif move == "L" and self.last_move != "R":
                self.neighbors.append(self.change_state(move, index))
            elif move == "D" and self.last_move != "U":
                self.neighbors.append(self.change_state(move, index))
            elif move == "R" and self.last_move != "L":
                self.neighbors.append(self.change_state(move, index))




    def get_heuristic_cost(self):
        if self.metrics == "hamm":
            return self.hamming_metric()
        elif self.metrics == "manh":
            return self.manhattan_metric()
        else:
            return 0

    def __lt__(self, other):
        return True

"""
metody do operacji na planszy puzzli
"""
####################################################################################################

def make_move(board, direction, index):
    if direction == "D":
        board.lastmove = "D"
        swap_fields(board, index, index + board.w)
    elif direction == "U":
        board.lastmove = "U"
        swap_fields(board, index, index - board.w)
    elif direction == "L":
        board.lastmove = "L"
        swap_fields(board, index, index - 1)
    elif direction == "R":
        board.lastmove = "R"
        swap_fields(board, index, index + 1)

def find_zero(board):
    for index, tile in enumerate(board.tab):
        if tile == "0":
            return index

def available_moves(board, last_move):
    index = find_zero(board)
    moves = []
    if (int(index / board.w) != 0) and (last_move != "D"):
        moves.append("U")
    if index % board.w != 0 and (last_move != "R"):
        moves.append("L")
    if int(index / board.w) != board.h - 1 and (last_move != "U"):
        moves.append("D")
    if index % board.w != board.w - 1 and (last_move != "L"):
        moves.append("R")
    return moves

def next_moves_in_order(order, board):
    available = available_moves(board, board.lastmove)
    next_moves = [move for move in order if move in available]
    return next_moves

"""
swap_fields -> funkcja zamieniająca miejscami dwa elementy w układance, gdzie jeden z elementow to zero
"""
def swap_fields(board, zero_index, other_index):
    temp = board.tab[zero_index]
    board.tab[zero_index] = board.tab[other_index]
    board.tab[other_index] = temp
