
def make_move(board, direction, index):
    if direction == "D":
        board.lastmove = "D"
        swap_tiles(board, index, index + board.w)
    elif direction == "U":
        board.lastmove = "U"
        swap_tiles(board, index, index - board.w)
    elif direction == "L":
        board.lastmove = "L"
        swap_tiles(board, index, index - 1)
    elif direction == "R":
        board.lastmove = "R"
        swap_tiles(board, index, index + 1)

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
def swap_tiles(board, zero_index, other_index):
    temp = board.tab[zero_index]
    board.tab[zero_index] = board.tab[other_index]
    board.tab[other_index] = temp
