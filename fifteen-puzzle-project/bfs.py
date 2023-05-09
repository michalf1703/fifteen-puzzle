import time
from collections import deque

class bfs:
    def __init__(self, board):
        self.board = board
        self.visited = set()
        self.visited_states = 1
        self.processed_states = 0
        self.elapsed_time = 0
        self.max_recursion_reached = 0

    def bfs_solve(self):
        star_time = time.time_ns()
        q = deque([(self.board, "")])
        self.visited.add(self.board.__hash__())
        while q:
            current, path = q.popleft()
            if current.depth >= self.max_recursion_reached:
                self.max_recursion_reached = current.depth
            self.processed_states += 1
            if current.is_solved():
                self.elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
                return path
            current.move()
            for neighbour in current.get_neighbors():
                self.visited_states += 1
                if neighbour.__hash__() not in self.visited:
                    self.visited.add(neighbour.__hash__())
                    q.append((neighbour, path + neighbour.last_move))
        self.elapsed_time = (time.time_ns() - star_time) / (10 ** 6)
        return None

    # get_states_count --> Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
    def get_states_count(self):
        return self.visited_states, self.processed_states

    #get_time -->Zwraca czas wykonania algorytmu w sekundach, z dokładnością do 3 miejsc po przecinku
    def get_time(self):
        return round(self.elapsed_time, 3)

    #get_max_depth_reached --> Zwraca maksymalną rekursję, jaką osiągnął algorytm
    def get_max_depth_reached(self):
        return self.max_recursion_reached
