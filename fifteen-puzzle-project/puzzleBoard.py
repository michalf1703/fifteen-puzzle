import copy


class puzzleBoard:
    def __init__(self, width, height, puzzle, metric):
        self.width = width
        self.height = height
        self.board = puzzle
        self.parent = None                                                          # rodzic węzła
        self.last_move = ''                                                         # ostatni ruch, który doprowadził do tego węzła
        if metric == "hamm" or metric == "manh":                                    # jeśli używamy A* z heurystyką hamm lub manh
            self.metric = "LURD"                                                    # to na sztywno wybieramy kolejność ruchów
            self.heuristic = metric
        else:
            self.metric = metric                                                    # w innym przypadku wykorzystujemy zadaną metrykę
            self.heuristic = None
        self.neighbors = []                                                         # sąsiedzi węzła
        self.depth = 0                                                              # głębokość w drzewie rozwiązań

    def get_neighbors(self):
        return self.neighbors

    def __copy__(self):
        new_board = copy.deepcopy(self.board)                                       # tworzymy głęboką kopię planszy
        new_instance = puzzleBoard(self.width, self.height, new_board, self.metric) # tworzymy nowy węzeł
        new_instance.last_move = self.last_move                                     # kopiujemy ostatni ruch
        new_instance.parent = self                                                  # ustawiamy rodzica na obecny węzeł
        new_instance.priority = self.metric                                         # ustawiamy priorytet heurystyki
        new_instance.depth = self.depth + 1                                         # ustawiamy głębokość na jeden większą niż węzeł rodzica
        new_instance.heuristic = self.heuristic                                     # kopiujemy heurystykę
        return new_instance

    def __hash__(self):                                                             #Oblicza hash planszy.
        return hash(tuple(self.board))

    def is_solved(self):
        """
        Sprawdza, czy plansza jest już rozwiązana.
        """
        solution = list(range(1, self.height * self.width)) + [0]                   # tworzymy listę z rozwiązaniem
        return tuple(self.board) == tuple(solution)                                 # porównujemy planszę z rozwiązaniem i zwracamy True lub False

    def change_state(self, move, index):
        """
        Tworzy nowy węzeł reprezentujący planszę po wykonaniu ruchu `move` na pozycji `index`.
        """
        new_board = self.__copy__()                                                 # tworzymy nowy węzeł na podstawie obecnej planszy
        new_board.last_move = move
        offset = 0
        if move == "U":
            offset = -self.width
        elif move == "D":
            offset = self.width
        elif move == "R":
            offset = 1
        elif move == "L":
            offset = -1

        if offset != 0:
            temp = new_board.board[index + offset]
            new_board.board[index + offset] = 0
            new_board.board[index] = temp
            return new_board

        return None

    def move(self):
        index = self.board.index(0)                                                 # znajdź indeks pustego pola
        # dla każdego ruchu w kolejności metryki (LURD):
        for move in self.metric:
            # jeśli ruch w górę jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            if move == "U" and self.last_move != "D" and int(index / self.width) != 0:
                self.neighbors.append(self.change_state(move, index))
            # jeśli ruch w lewo jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            elif move == "L" and self.last_move != "R" and index % self.width != 0:
                self.neighbors.append(self.change_state(move, index))
            # jeśli ruch w dół jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            elif move == "D" and self.last_move != "U" and int(index / self.width) != self.height - 1:
                self.neighbors.append(self.change_state(move, index))
            # jeśli ruch w prawo jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            elif move == "R" and self.last_move != "L" and index % self.width != self.width - 1:
                self.neighbors.append(self.change_state(move, index))

    def manhattan_metric(self):
        distance = 0
        target_positions = [
            [(i * self.width + j) % (self.width * self.height) % self.width, (i * self.width + j) // self.width] for i
            in range(self.height) for j in range(self.width)]
        for x in range(0, self.height):
            for y in range(0, self.width):
                board_value = self.board[x * self.height + y]
                if board_value != 0:
                    target_x, target_y = target_positions[board_value - 1]
                    distance += abs(target_x - y) + abs(target_y - x)
        return distance


    def hamming_metric(self):
        distance = 0                                                                            # zmienna przechowująca wartość heurystyki
        for number in range(0, self.width * self.height):                                       # pętla iterująca po wszystkich polach planszy
            board_value = self.board[number]                                                    # aktualna wartość pola planszy
            if number != board_value - 1 and board_value != 0:                                  # sprawdzenie, czy pole jest w złym miejscu
                distance += 1                                                                   # zwiększenie wartości heurystyki
        return distance                                                                         # zwrócenie wartości heurystyki


    def get_metric_cost(self):
        if self.heuristic == "hamm":                                                            # jeśli wybrana heurystyka to "hamm"
            return self.hamming_metric()                                                        # zwraca wynik hamming_heuristic()
        else:
            return self.manhattan_metric()                                                       # w przeciwnym wypadku zwraca wynik manhattan_heuristic()

    def __lt__(self, other):
        return True

