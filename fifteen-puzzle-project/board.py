import copy

class Board:
    def __init__(self, width, height, fields, last_move=None, solution="", metric="hamm", depth=0, cost=0):
        self.width = width
        self.height = height
        self.fields = fields
        self.last_move = last_move
        self.solution = solution
        self.metric = metric
        self.depth = depth
        self.cost = cost

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}
        copied_tab = [row[:] for row in self.fields]
        new_board = Board(self.width, self.height, copied_tab)
        new_board.solution = copy.deepcopy(self.solution)
        new_board.depth = copy.deepcopy(self.depth)
        new_board.metric = copy.deepcopy(self.metric)
        return new_board

    def __hash__(self):
        return hash(tuple(map(tuple, self.fields)))

    def is_goal(self):
        size = self.width * self.height
        if int(self.fields[size - 1]) != 0:
            return False

        expected_nums = list(range(1, size))
        actual_nums = [int(self.fields[i]) for i in range(size - 1)]

        return expected_nums == actual_nums

#################################################################################
    """
    metryka hamminga - jest to metryka, która sprawdza czy dany element jest na swoim miejscu - jeżeli nie jest to zwraca jeden,
     a jak jest zero, to zwraca zero - wówczas koszty można zsmuować - im wyższa wartość tym gorzej(bo oznacza to,
     że dużo kafelków nie jest na swojej pozycji
    """

    def get_xy_position(self, index):
        x = int(index % self.width)
        y = int(index / self.width)
        return [x, y]

    def hamming_metric(self):
        """
        Oblicza metrykę odległości Hamminga, czyli liczbę kafelków w niewłaściwej pozycji.
        """
        distance = sum(1 for i, tile in enumerate(self.fields) if tile != str(i + 1) and tile != "0")
        distance += self.depth
        self.cost = distance
        return distance

    """
    Metryka Manhatan - odległość jest liczona wzdłóż określonych współrzędnych, które są dalej sumowane - 
    w wyniku uzyskuje się odległość - wówczas dla każdego bloczka sumuje się te odległości - i im wyższa jest wartość tej metryki
     - to jest gorzej - jeżeli odległość jest niewielka to znaczy, że układ jest blisko stanu docelowego.
    """

    def manhattan_metric(self):
        """
        Oblicza metrykę odległości Manhattanu, która jest sumą odległości każdego pola od jego idealna pozycja.
        """
        distance = 0
        for i, tile in enumerate(self.fields):
            if tile != "0":
                current_row, current_col = self.get_xy_position(i)
                target_row, target_col = self.get_xy_position(int(tile) - 1)
                distance += abs(current_row - target_row) + abs(current_col - target_col)
        distance += self.depth
        self.cost = distance
        return distance


    def get_heuristic_cost(self):
        if self.metric == "hamm":
            return self.hamming_metric()
        elif self.metric == "manh":
            return self.manhattan_metric()
        else:
            return 0

    def __lt__(self, other):
        if self.metric == "hamm":
            return self.hamming_metric() < other.hammingsMetric()
        return self.manhattan_metric() < other.manhattansMetric()


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
