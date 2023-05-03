
"""
===> Omówienie BFS (ang. breadth-first-search):

* W przypadku tego algortymu potrzebna będzie struktura danych (ang. open list) - lista stanów otwartych - w przyapdku poznania sąsiadów dla danego elementu i będą wprowadzane do listy stanów otwartych.

* Jeżli algorytm operuje na liście stanów otwartych to nie działa taki algorytm najlepiej - bo niektóre stany będą odpytywane ponownie.

* Lista stanów zamkniętych (ang. closed - listed / explored) - przechowywana jest tam informacja o tym czy dany stan był już przepytywany (a do tego charakteryzuje się szybszym przeszukiwaniem)

"""


#pseudokod
"""
function bfs(G, s):
    if G.isGoal(s):
        return SUCCESS
    queue = queue()
    visited = set()         # Zbiór odwiedzonych wierzchołków
    queue.enqueue(s)
    visited.add(s)
    while not queue.isEmpty():
        v = queue.dequeue()
        for n in G.neighbours(v):
            if n not in visited:
                if G.isGoal(n):
                    return SUCCESS
                queue.enqueue(n)
                visited.add(n)
    return FAILURE
"""

import time
from collections import deque


class bfs:
    def __init__(self, board):
        self.board = board
        self.visited = set()                            # zbiór odwiedzonych stanów
        self.visited_states = 1                         # liczba odwiedzonych stanów
        self.processed_states = 0                       # liczba przetworzonych stanów
        self.elapsed_time = 0                           # czas wykonania algorytmu
        self.max_depth_reached = 0                      # maksymalna głębokość, na którą zszedł algorytm

    def bfs_solve(self):
        start_time = time.time_ns()  # Pobranie czasu rozpoczęcia działania algorytmu
        queue = deque([(self.board, "")])  # Utworzenie kolejki stanów do odwiedzenia
        current, path = queue.popleft()  # Pobranie pierwszego elementu z kolejki (ten fragment kodu jest zbędny, możemy usunąć ten wiersz)
        if self.board.is_solved():  # Sprawdzenie, czy stan początkowy jest już rozwiązaniem
            self.elapsed_time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczenie czasu wykonania
            return path  # Zwrócenie pustego ciągu, ponieważ już jesteśmy w stanie końcowym
        queue = deque()  # Zainicjowanie pustej kolejki
        visited = set()  # Zainicjowanie pustego zbioru odwiedzonych stanów
        queue.append((self.board, ""))  # Dodanie stanu początkowego do kolejki z pustym ciągiem ruchów
        visited.add(self.board.__hash__())  # Dodanie stanu początkowego do zbioru odwiedzonych
        while queue:
            current, path = queue.popleft()  # Pobranie pierwszego elementu z kolejki
            self.processed_states += 1  # Zwiększenie liczby przetworzonych stanów
            current.move()  # Wygenerowanie możliwych ruchów dla danego stanu
            for neighbor in current.get_neighbors():  # Przejście po sąsiadach danego stanu
                self.visited_states += 1  # Zwiększenie liczby odwiedzonych stanów
                if neighbor.__hash__() not in visited:  # Sprawdzenie, czy dany sąsiad nie był jeszcze odwiedzony
                    if neighbor.is_solved():  # Sprawdzenie, czy dany sąsiad jest stanem końcowym
                        self.elapsed_time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczenie czasu wykonania
                        return path + neighbor.last_move  # Zwrócenie ciągu ruchów prowadzących do rozwiązania
                    queue.append((neighbor,
                                  path + neighbor.last_move))  # Dodanie danego sąsiada do kolejki z aktualnym ciągiem ruchów
                    visited.add(neighbor.__hash__())  # Dodanie danego sąsiada do zbioru odwiedzonych
                    if neighbor.depth > self.max_depth_reached:  # Aktualizacja maksymalnej głębokości przeszukiwania
                        self.max_depth_reached = neighbor.depth
        self.elapsed_time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczenie czasu wykonania
        return None  # Zwrócenie None, ponieważ nie udało się znaleźć rozwiązania

    def get_states_count(self):
        """
        Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
        :return: krotka z dwoma liczbami: (odwiedzone, przetworzone)
        """
        return self.visited_states, self.processed_states

    def get_elapsed_time(self):
        """
        Zwraca czas wykonania algorytmu w sekundach.
        :return: czas wykonania algorytmu w sekundach
        """
        return round(self.elapsed_time, 3)

    def get_max_depth_reached(self):
        """
        Zwraca maksymalną rekursję, jaką osiągnął algorytm.
        :return: maksymalna rekursja
        """
        return self.max_depth_reached
