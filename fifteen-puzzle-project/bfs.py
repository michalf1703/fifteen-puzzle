
"""
===> Omówienie BFS (ang. breadth-first-search):

* W przypadku tego algortymu potrzebna będzie struktura danych (ang. open list) - lista stanów otwartych - w przyapdku poznania sąsiadów dla danego elementu i będą wprowadzane do listy stanów otwartych.

* Jeżli algorytm operuje na liście stanów otwartych to nie działa taki algorytm najlepiej - bo niektóre stany będą odpytywane ponownie.

* Lista stanów zamkniętych (ang. closed - listed / explored) - przechowywana jest tam informacja o tym czy dany stan był już przepytywany (a do tego charakteryzuje się szybszym przeszukiwaniem)

"""


#pseudokod
"""
function dfs(G, s)
	if G.isgoal(s)
		return SUCCESS
	S = stack()
	T = set()
	S.push(s)
	while ~S.isempty()
		v = S.pop()
		T.add(v)
		for n in reverse(G.neighbours(n))
			if G.isgoal()
				return SUCCESS
			if ~T.has(n) and ~S.has(n)
				S.push(n)
	return FAILURE
"""

import time
from collections import deque


class bfs:
    def __init__(self, board):
        self.board = board
        self.visited = set()  # zbiór odwiedzonych stanów
        self.visited_states = 1  # liczba odwiedzonych stanów
        self.processed_states = 0  # liczba przetworzonych stanów
        self.elapsed_time = 0  # czas wykonania algorytmu
        self.max_depth_reached = 0  # maksymalna głębokość, na którą zszedł algorytm

    def bfs_solve(self):
        start_time = time.time_ns()  # czas rozpoczęcia działania algorytmu
        queue = deque([(self.board, "")])  # kolejka stanów do odwiedzenia
        self.visited.add(self.board.__hash__())  # dodanie stanu początkowego do odwiedzonych
        while queue:
            current, path = queue.popleft()  # pobranie stanu z kolejki
            self.processed_states += 1
            if current.is_solved():
                self.elapsed_time = (time.time_ns() - start_time) / (10 ** 6)  # obliczenie czasu wykonania
                return path
            current.move()  # generowanie ruchów dla danego stanu
            for neighbor in current.get_neighbors():
                self.visited_states += 1  # zwiększenie liczby odwiedzonych stanów
                if neighbor.__hash__() not in self.visited:
                    self.visited.add(neighbor.__hash__())  # dodanie stanu do zbioru odwiedzonych
                    queue.append((neighbor, path + neighbor.last_move))  # dodanie stanu do kolejki
                    if neighbor.depth > self.max_depth_reached:
                        self.max_depth_reached = neighbor.depth  # aktualizacja maksymalnej głębokości
        self.elapsed_time = (time.time_ns() - start_time) / (10 ** 6)
        return None

    def get_states_count(self):
        return self.visited_states, self.processed_states

    def get_elapsed_time(self):
        return round(self.elapsed_time, 3)

    def get_max_depth_reached(self):
        return self.max_depth_reached
