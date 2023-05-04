#tu bedzie a*
"""
Algorytm A* : algorytm działa na takiej zasadzie, że umieszcza on na liście stanów otwartych umieszcza stanów
 - jednak w takiej kolejności, że wartości metryki w kolejności malejącej są bliżej zdjęcia z tej kolejki priorytetowej.

Algorytm A* nie porządkuje stanów w kolejce tylko i wyłącznie za pomocą funkcji heurysytcznej
- tylko funkcji oceny -> bierze ona pod uwagę wartość funkcji heurystycznej oraz dotychczasowy koszt
 dotarcia do bieżącego wierzchołka od stanu początkowego.

czyli: f(n) = g(n) + h(n)
"""



#psuedokod

"""
function aStar(G, s):
	p = priorityQueue()
	T = set()
	p.insert(s, 0)
	while ~p.isEmpty():
		v = p.pull()
		if ~T.has(v):
			if G.isGoal(v):
				return SUCCESS
			T.add(v)
			for n in G.neighbours(v)
			if ~T.has(n)
				f = g(n) + h(n, G)
				p.insert(n , f)
	return FAILURE
"""


import time
from queue import PriorityQueue

class aStar:
    def __init__(self, board):
        self.board = board
        self.visited_states = 0                             # Liczba odwiedzonych stanów
        self.processed_states = 0                           # Liczba przetworzonych stanów
        self.elapsed_time = 0                               # Czas wykonania algorytmu w milisekundach
        self.max_depth_reached = 0                          # Największa osiągnięta głębokość

    def solve(self):
        start_time = time.time_ns()                         # Pobieramy czas rozpoczęcia wykonywania algorytmu w nanosekundach
        open_set = PriorityQueue()                          # Kolejka priorytetowa na węzły do odwiedzenia
        open_set.put((0, self.board))                       # Wkładamy koszt i dany stan
        closed_set = dict()                                 # Słownik przechowujący już odwiedzone stany wraz z ich kosztami
        while not open_set.empty():
            current = open_set.get()[1]                     # Wyjmujemy węzeł z najniższym kosztem
            if current.depth >= self.max_depth_reached:
                self.max_depth_reached = current.depth      # Aktualizujemy wartość największej osiągniętej głębokości
            self.processed_states += 1                      # Zwiększamy liczbę przetworzonych stanów
            closed_set[current.__hash__()] = current.depth  # Dodajemy aktualny stan do słownika odwiedzonych
            if current.is_solved():
                path = ""
                while current.last_move != "":              # Przechodzimy po rodzicach w celu odnalezienia rozwiązania
                    path += current.last_move
                    current = current.parent
                reversed_path = path[::-1]                  # Odwracamy scieżkę, aby otrzymać poprawny wynik
                self.elapsed_time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczamy czas wykonania algorytmu
                return reversed_path
            current.move()
            for neighbor in current.get_neighbors():
                self.visited_states += 1                     # Zwiększamy liczbę odwiedzonych stanów
                if (neighbor.__hash__() in closed_set and neighbor.depth < closed_set[neighbor.__hash__()]) or neighbor.__hash__() not in closed_set:
                    cost = neighbor.depth + neighbor.get_metric_cost()  # Obliczamy koszt danego stanu
                    board_and_cost = (cost, neighbor)
                    is_in_queue = False
                    for item in open_set.queue:
                        if item == board_and_cost:
                            is_in_queue = True
                            break
                    if not is_in_queue:
                        open_set.put((cost, neighbor))
        self.elapsed_time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczamy czas wykonania algorytmu
        return None

    def count_states(self):
        """
        Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
        :return: krotka z dwoma liczbami: (odwiedzone, przetworzone)
        """
        return self.visited_states, self.processed_states

    def count_time(self):
        """
        Zwraca czas wykonania algorytmu w sekundach.
        :return: czas wykonania algorytmu w sekundach
        """
        return round(self.elapsed_time, 3)

    def recursion_reached(self):
        """
        Zwraca maksymalną rekursję, jaką osiągnął algorytm.
        :return: maksymalna rekursja
        """
        return self.max_depth_reached
