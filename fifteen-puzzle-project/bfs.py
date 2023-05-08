import time
from collections import deque

class bfs:
    def __init__(self, board):
        self.board = board
        self.visited = set()                            # zbiór odwiedzonych stanów
        self.visited_states = 1                         # liczba odwiedzonych stanów
        self.processed_states = 0                       # liczba przetworzonych stanów
        self.time = 0                                   # czas wykonania algorytmu
        self.max_depth_reached = 0                      # maksymalna głębokość, na którą zszedł algorytm

    def bfs_solve(self):
        start_time = time.time_ns()                     # Pobranie czasu rozpoczęcia działania algorytmu
        queue = deque([(self.board, "")])               # Utworzenie kolejki stanów do odwiedzenia
        current, path = queue.popleft()                 # Pobranie pierwszego elementu z kolejki (ten wiersz jest potrzebny tylko w przypadku, gdy wczytamy poprawna tablice)
        if self.board.is_solved():                      # Sprawdzenie, czy stan początkowy jest już rozwiązaniem
            self.time = (time.time_ns() - start_time) / (10 ** 6)           # Obliczenie czasu wykonania
            return path                                 # Zwrócenie pustego ciągu, ponieważ już jesteśmy w stanie końcowym
        queue = deque()                                 # Zainicjowanie pustej kolejki
        visited = set()                                 # Zainicjowanie pustego zbioru odwiedzonych stanów
        queue.append((self.board, ""))                  # Dodanie stanu początkowego do kolejki z pustym ciągiem ruchów
        visited.add(self.board.__hash__())              # Dodanie stanu początkowego do zbioru odwiedzonych
        while queue:
            current, path = queue.popleft()             # Pobranie pierwszego elementu z kolejki
            self.processed_states += 1                  # Zwiększenie liczby przetworzonych stanów
            current.move()                              # Wygenerowanie możliwych ruchów dla danego stanu
            for neighbor in current.get_neighbors():    # Przejście po sąsiadach danego stanu
                self.visited_states += 1                # Zwiększenie liczby odwiedzonych stanów
                if neighbor.__hash__() not in visited:  # Sprawdzenie, czy dany sąsiad nie był jeszcze odwiedzony
                    if neighbor.is_solved():            # Sprawdzenie, czy dany sąsiad jest stanem końcowym
                        self.time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczenie czasu wykonania
                        return path + neighbor.last_move        # Zwrócenie ciągu ruchów prowadzących do rozwiązania
                    queue.append((neighbor,
                                  path + neighbor.last_move))   # Dodanie danego sąsiada do kolejki z aktualnym ciągiem ruchów
                    visited.add(neighbor.__hash__())            # Dodanie danego sąsiada do zbioru odwiedzonych
                    if neighbor.depth > self.max_depth_reached: # Aktualizacja maksymalnej głębokości przeszukiwania
                        self.max_depth_reached = neighbor.depth
        self.time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczenie czasu wykonania
        return None                                             # Zwrócenie None, ponieważ nie udało się znaleźć rozwiązania

    # get_states_count --> Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
    def get_states_count(self):
        return self.visited_states, self.processed_states

    #get_time -->Zwraca czas wykonania algorytmu w sekundach, z dokładnością do 3 miejsc po przecinku
    def get_time(self):
        return round(self.time, 3)

    #get_max_depth_reached --> Zwraca maksymalną rekursję, jaką osiągnął algorytm
    def get_max_depth_reached(self):
        return self.max_depth_reached
