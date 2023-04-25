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

    """
    metryka hamminga - jest to metryka, która sprawdza czy dany element jest na swoim miejscu - jeżeli nie jest to zwraca jeden,
     a jak jest zero, to zwraca zero - wówczas koszty można zsmuować - im wyższa wartość tym gorzej(bo oznacza to,
     że dużo kafelków nie jest na swojej pozycji
    """

    def get_xy_position(self,index):
        x = int(index % self.columns)
        y = int(index / self.columns)
        return [x,y]


    def hamming_metric(self):
        """
        Oblicza metrykę odległości Hamminga, czyli liczbę kafelków w niewłaściwej pozycji.
        """
        distance = sum(1 for i, tile in enumerate(self.board) if tile != str(i + 1) and tile != "0")
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
        for i, tile in enumerate(self.board):
            if tile != "0":
                current_row, current_col = self.get_xy_position(i)
                target_row, target_col = self.get_xy_position(int(tile) - 1)
                distance += abs(current_row - target_row) + abs(current_col - target_col)
        distance += self.depth
        self.cost = distance
        return distance

    def get_heuristic_cost(self):
        if self.metrics == "hamm":
            return self.hamming_metric()
        elif self.metrics == "manh":
            return self.manhattan_metric()
        else:
            return 0

    def __lt__(self, other):
        return True
