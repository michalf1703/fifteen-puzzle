import time
from queue import PriorityQueue

class aStar:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.visited_states = 0                             # Liczba odwiedzonych stanów
        self.processed_states = 0                           # Liczba przetworzonych stanów
        self.time = 0                                       # Czas wykonania algorytmu w milisekundach
        self.max_depth = 0                                  # Największa osiągnięta głębokość

    # count_states --> Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
    def get_states(self):
        return self.visited_states, self.processed_states

    # get_time --> Zwraca czas wykonania algorytmu w sekundach, z dokładnością do 3 miejsc po przecinku.
    def get_time(self):
        return round(self.time, 3)

    # get_max_depth_reached --> Zwraca maksymalną rekursję, jaką osiągnął algorytm
    def get_max_depth(self):
        return self.max_depth

    def solve(self):
        start_time = time.time_ns()                         # Pobieramy czas rozpoczęcia wykonywania algorytmu w nanosekundach
        open_set = PriorityQueue()                          # Kolejka priorytetowa na węzły do odwiedzenia
        open_set.put((0, self.puzzle))                      # Wkładamy koszt i dany stan
        closed_set = dict()                                 # Słownik przechowujący już odwiedzone stany wraz z ich kosztami
        while not open_set.empty():
            current = open_set.get()[1]                     # Wyjmujemy węzeł z najniższym kosztem
            if current.depth >= self.max_depth:
                self.max_depth = current.depth              # Aktualizujemy wartość największej osiągniętej głębokości
            self.processed_states += 1                      # Zwiększamy liczbę przetworzonych stanów
            closed_set[current.__hash__()] = current.depth  # Dodajemy aktualny stan do słownika odwiedzonych
            if current.is_solved():
                path = ""
                while current.final_move != "":              # Przechodzimy po rodzicach w celu odnalezienia rozwiązania
                    path += current.final_move
                    current = current.parent
                reversed_path = path[::-1]                  # Odwracamy scieżkę, aby otrzymać poprawny wynik
                self.time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczamy czas wykonania algorytmu
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
        self.time = (time.time_ns() - start_time) / (10 ** 6)  # Obliczamy czas wykonania algorytmu
        return None

