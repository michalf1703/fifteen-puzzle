import copy


class puzzleBoard:
    def __init__(self, width, height, puzzle, order):
        self.width = width
        self.height = height
        self.puzzle = puzzle
        self.parent = None                                                         # rodzic węzła
        self.last_move = ''                                                       # ostatni ruch, który doprowadził do tego węzła
        if order == "hamm" or order == "manh":                                     # jeśli używamy A* z heurystyką hamm lub manh
            self.order = "LURD"                                                   # to na sztywno wybieramy kolejność ruchów
            self.heuristic = order
        else:
            self.order = order                                                    # w innym przypadku wykorzystujemy zadaną metrykę
            self.heuristic = None
        self.neighbors = []                                                        # sąsiedzi węzła
        self.depth = 0                                                             # głębokość w drzewie rozwiązań


#funkcja do kopiowania stanu planszy tak, aby nie modyfikować oryginalnej planszy
    def __copy__(self):
        new_puzzle_board = copy.deepcopy(self.puzzle)                                        # tworzymy głęboką kopię planszy
        new = puzzleBoard(self.width, self.height, new_puzzle_board, self.order)             # tworzymy nowy węzeł
        new.last_move = self.last_move                                                       # kopiujemy ostatni ruch
        new.parent = self                                                                    # ustawiamy rodzica na obecny węzeł
        new.order = self.order                                                               # ustawiamy priorytet
        new.depth = self.depth + 1                                                           # ustawiamy głębokość na jeden większą niż węzeł rodzica
        new.heuristic = self.heuristic                                                       # kopiujemy heurystykę
        return new

#funkcja tworząca skrót planszy gry
    def __hash__(self):
        return hash(tuple(self.puzzle)) #przekonwertowanie listy wartości planszy na krotkę oraz stworzenie skrótu tej krotki

#is_goal -> funkcja sprawdzająca czy dana plansza jest rozwiązaniem gry
    def is_goal(self):
        solution = list(range(1, self.height * self.width)) + [0]                    # tworzenie listy z rozwiązaniem, wartości od 1 do 15 i na końcu 0
        return tuple(self.puzzle) == tuple(solution)                                 # porównanie planszy z rozwiązaniem i zwracanie True lub False


#move_state -> funkcja używana do wykonania ruchów, aby stworzyć nowy węzeł planszy w grze
    def move_state(self, move, index):                   #index -> index pustego pola
        new_puzzles = self.__copy__()                    #tworzenie kopi obecnej planszy, tak aby nie działać na oryginalnej planszy
        new_puzzles.last_move = move                     # Ustawiamy ruch, który doprowadził nas do tego stanu planszy
        # Obliczamy przesunięcie w zależności od kierunku ruchu
        offset = 0
        if move == "U":
            offset = -self.width
        elif move == "D":
            offset = self.width
        elif move == "R":
            offset = 1
        elif move == "L":
            offset = -1
        # Jeśli przesunięcie nie wynosi 0, to zamieniamy wartość pustego pola z wartością z sąsiedniego pola
        if offset != 0:
            temp = new_puzzles.puzzle[index + offset]
            new_puzzles.puzzle[index + offset] = 0
            new_puzzles.puzzle[index] = temp
            return new_puzzles  # Zwracamy nowy węzeł
        return None  # Jeśli przesunięcie wynosi 0, to ruch jest niepoprawny, więc zwracamy None

#move -> służy do wygenerowania listy sąsiadów, którzy są osiągalni przez wykonanie jednego ruchu (lewo, w górę, w prawo , w dół)
    def move(self):
        index = self.puzzle.index(0)  # znajdź indeks pustego pola
        # dla każdego ruchu w kolejności metryki (LURD):
        for move in self.order:
            # jeśli ruch w górę jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            if move == "U" and self.last_move != "D" and int(index / self.width) != 0:
                self.neighbors.append(self.move_state(move, index))
            # jeśli ruch w lewo jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            elif move == "L" and self.last_move != "R" and index % self.width != 0:
                self.neighbors.append(self.move_state(move, index))
            # jeśli ruch w dół jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            elif move == "D" and self.last_move != "U" and int(index / self.width) != self.height - 1:
                self.neighbors.append(self.move_state(move, index))
            # jeśli ruch w prawo jest możliwy i nie jest to cofnięcie ostatniego ruchu, dodaj nowy węzeł do listy sąsiadów
            elif move == "R" and self.last_move != "L" and index % self.width != self.width - 1:
                self.neighbors.append(self.move_state(move, index))

    def get_neighbors(self):
        return self.neighbors

    # Funkcja obliczająca odległość Manhattan- mierzy odległość między dwoma punktami na płaszczyźnie, sumując różnice ich współrzędnych poziomych i pionowych
    def manhattan_metric(self):
        distance = 0                                              #inicjalizacja początkowej odległości
        for x in range(0, self.height):                           #przejście przez każdą wewnętrzną komórkę planszy wewnętrznymi pętlami for zmiennych x i y
            for y in range(0, self.width):
                puzzles_value = self.puzzle[x * self.height + y]  #dla każdej komórki planszy, "puzzles_value" przechowuje jej wartość, a jeśli jest zerem to przechodzi do następnej komórki
                if puzzles_value != 0:
                    current_x = y
                    current_y = x                                 #jeśli puzzles_value nie ma wartości 0, następuje wartość zmiennej current_x i current_y, które przechowują aktualne współrzędne komórki planszy
                    correct_x = (puzzles_value - 1) % self.width
                    correct_y = (puzzles_value - 1) // self.height #obliczanie wartości correct_x o
                    distance += abs(correct_x - current_x) + abs(correct_y - current_y) #obliczanie odległosci między aktualną i oczekiwaną pozycją komórki planszy
        return distance

    def hamming_metric(self):
        distance = 0                                                                            # zmienna przechowująca wartość heurystyki
        for number in range(0, self.width * self.height):                                       # pętla iterująca po wszystkich polach planszy
            puzzles_value = self.puzzle[number]                                                 # aktualna wartość pola planszy
            if number != puzzles_value - 1 and puzzles_value != 0:                              # sprawdzenie, czy pole jest w złym miejscu
                distance += 1                                                                   # zwiększenie wartości heurystyki
        return distance                                                                         # zwrócenie wartości heurystyki, im mniejsza wartosc distance to lepiej


    def get_metric_cost(self):
        if self.heuristic == "hamm":                                                            # jeśli wybrana heurystyka to "hamm"
            return self.hamming_metric()                                                        # zwraca wynik hamming_heuristic()
        else:
            return self.manhattan_metric()                                                      # w przeciwnym wypadku zwraca wynik manhattan_heuristic()

    def __lt__(self, other):
        return True

