from timeit import default_timer
from collections import deque

class bfs:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.visited = set()                #tworzy pustą zbiór, który będzie przechowywał wszystkie odwiedzone stany planszy.
        self.visited_states = 1
        self.processed_states = 0
        self.time = 0
        self.max_depth_reached = 0

    # get_states --> Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
    def get_states(self):
        return self.visited_states, self.processed_states

    #get_time -->Zwraca czas wykonania algorytmu w sekundach, z dokładnością do 3 miejsc po przecinku
    def get_time(self):
        return round(self.time, 3)

    #get_max_depth_reached --> Zwraca maksymalną rekursję, jaką osiągnął algorytm
    def get_max_depth(self):
        return self.max_depth_reached

    def solve(self):
        start_time = default_timer()                                    # zapisanie czasu rozpoczęcia rozwiązywania problemu.
        queue = deque([(self.puzzle, "")])                              # utworzenie kolejki, która będzie przechowywała pary (stan planszy, ścieżka do tego stanu).
        self.visited.add(self.puzzle.__hash__())                        # oznaczenie bieżącego stan planszy jako odwiedzony.
        while queue:                                                    # wykonywanie pętli dopóki kolejka nie jest pusta.
            current_board_state, path = queue.popleft()                 # pobranie pierwszy element z kolejki, który jest krotka dwoch wartosci
            if current_board_state.depth >= self.max_depth_reached:     # zapisanie, jeśli osiągnięto nową maksymalną głębokość.
                self.max_depth_reached = current_board_state.depth
            self.processed_states += 1                                  # zwiekszenie licznika przetworzonych stanów.
            if current_board_state.is_goal():                           # sprawdzenie, czy bieżący stan planszy jest rozwiązaniem.
                self.time = (default_timer() - start_time) *1000   # obliczenie czasu potrzebnego do rozwiązania problemu.
                return path                                             # zwrócenie ścieżki do rozwiązania.
            current_board_state.move()                                  # wykonanie ruchu na planszy.
            for neighbour in current_board_state.get_neighbors():       # sprawdzenie sąsiadów bieżącego stanu planszy.
                self.visited_states += 1                                # zwiekszenie licznika odwiedzonych stanów.
                if neighbour.__hash__() not in self.visited:            # dodanie do kolejki, jeśli sąsiad nie był wcześniej odwiedzony.
                    self.visited.add(neighbour.__hash__())              # dodanie do listy stanów odwiedzonych
                    queue.append((neighbour, path + neighbour.last_move)) #dodanie do kolejki queue krotke, składającą się na stan planszy sąsiada oraz path+neighbour.last_move
        self.time = (default_timer - start_time) *1000           # oblicznie czasu potrzebny do rozwiązania problemu.
        return None                                                     # zwrocenie wartość None, gdy problem nie może być rozwiązany.


#stan odwiedzony -> stan dodany do kolejki
#stan przetworzoyn -> stan, który został pobrany z kolejki (zdjęty ze struktury?, później jest sprawdzane czy jest naszym celem)
#l:42 ... path+neighbour.last_move -> nowa ścieżka, która prowadzi do danego sąsaida planszy. path to ścieżka, która prowadzi do bieżącego stanu planszy,
#natomiast neighbour.last_move jest ruchem, który z aktualnej ścieżki prowadzi do sąsiada
#ogólnie jest to łączone i daje nam to ścieżkę do sąsiada
#dzięki czemu z każdym nowym stanem planszy zapisywana jest aktualna ścieżka do tego stanu, a algorytm będzie miał możliwość odtworzenia ścieżki
#prowadzącej do rozwiązania po znalezieniu go