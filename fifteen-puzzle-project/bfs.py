import time
from collections import deque

class bfs:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.visited = set()
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
        start_time = time.time_ns()                                     # Zapisz czas rozpoczęcia rozwiązywania problemu.
        queue = deque([(self.puzzle, "")])                              # Utwórz kolejkę, która będzie przechowywała pary (stan planszy, ścieżka do tego stanu).
        self.visited.add(self.puzzle.__hash__())                        # Oznacz bieżący stan planszy jako odwiedzony.
        while queue:                                                    # Wykonuj dopóki kolejka nie jest pusta.
            current, path = queue.popleft()                             # Pobierz pierwszy element z kolejki.
            if current.depth >= self.max_depth_reached:                 # Zapisz, jeśli osiągnięto nową maksymalną głębokość.
                self.max_depth_reached = current.depth                  # Zwiększ licznik przetworzonych stanów.
            self.processed_states += 1
            if current.is_solved():                                     # Sprawdź, czy bieżący stan planszy jest rozwiązaniem.
                self.time = (time.time_ns() - start_time) / (10 ** 6)   # Oblicz czas potrzebny do rozwiązania problemu.
                return path                                             # Zwróć ścieżkę do rozwiązania.
            current.move()                                              # Wykonaj ruch na planszy.
            for neighbour in current.get_neighbors():                   # Sprawdź sąsiadów bieżącego stanu planszy.
                self.visited_states += 1                                # Zwiększ licznik odwiedzonych stanów.
                if neighbour.__hash__() not in self.visited:            # Dodaj do kolejki, jeśli sąsiad nie był wcześniej odwiedzony.
                    self.visited.add(neighbour.__hash__())
                    queue.append((neighbour, path + neighbour.final_move))
        self.time = (time.time_ns() - start_time) / (10 ** 6)           # Oblicz czas potrzebny do rozwiązania problemu.
        return None                                                     # Zwróć wartość None, gdy problem nie może być rozwiązany.

