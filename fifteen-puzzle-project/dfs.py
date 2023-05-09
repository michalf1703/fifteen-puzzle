import time
class dfs:
    def __init__(self):
        # Inicjalizacja zmiennych używanych w algorytmie DFS
        self.path = ""                                      # zmienna przechowująca ścieżkę do rozwiązania
        self.visited = {}                                   # słownik przechowujący odwiedzone stany, gdzie klucz to hash stanu, wartość to długość ścieżki
        self.max_depth = 20                                 # maksymalna dozwolona głębokość przeszukiwania
        self.visited_states = 1                             # liczba odwiedzonych stanów
        self.processed_states = 0                           # liczba przetworzonych stanów
        self.time = 0                                       # czas wykonania algorytmu
        self.max_recursion = 0                              # maksymalna głębokość rekursji, osiągnięta podczas działania algorytmu

    #zaimplementowana została funkcja dfs_start(), w celu mierzenia czasu
    #nie mieliśmy jak zaimplementować licznika czasu wewnątrz funkcji dfs_solve, ponieważ została ona wykonana rekurencyjnie, więc licznik czasu resetowałby sie
    def dfs_start(self, puzzle):
        start_time = time.time()                            # mierzymy czas wykonania algorytmu
        result = self.solve(puzzle)                         # uruchamiamy funkcję rozwiązującą problem
        self.time = time.time() - start_time                # obliczamy czas wykonania algorytmu
        return result


    # get_states_count --> Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
    def get_states_count(self):
        return self.visited_states, self.processed_states

    # get_time --> Zwraca czas wykonania algorytmu w sekundach, z dokładnością do trzech miejsc po przecinku
    def get_time(self):
        return round(self.time, 3)

    # get_max_depth_reached --> Zwraca maksymalną rekursję, jaką osiągnął algorytm.
    def get_max_depth(self):
        return self.max_recursion

    def solve(self, board):
        self.processed_states += 1                                  # Licznik odwiedzonych stanów planszy
        if self.max_depth is not None and board.depth > self.max_depth:
            return None                                             # Jeśli osiągnięto maksymalną głębokość i plansza przekracza ją, to zwróć None
        if board.depth >= self.max_recursion:
            self.max_recursion = board.depth                        # Aktualizacja największej dotychczasowej głębokości rekursji
        if board.is_solved():
            return self.path                                        # Jeśli plansza jest rozwiązana, zwróć ścieżkę prowadzącą do rozwiązania
        self.visited[board.__hash__()] = board.depth                # Dodaj planszę do odwiedzonych stanów
        board.move()                                                # Przejście do następnego stanu planszy
        for neighbor in board.get_neighbors():
            self.visited_states += 1                                # Zwiększenie liczby odwiedzonych stanów planszy
                                                                    # Sprawdzenie, czy sąsiednia plansza już została odwiedzona i czy ma mniejszą głębokość,
                                                                    # jeśli tak, to nie wchodzimy do niej ponownie
            if (neighbor.__hash__() in self.visited and neighbor.depth < self.visited[
                neighbor.__hash__()]) or neighbor.__hash__() not in self.visited:
                self.path += neighbor.final_move                     # Dodaj ostatni ruch do ścieżki
                result = self.solve(neighbor)                   # Rekurencyjne wywołanie dfs_solve dla sąsiedniej planszy
                if result is not None:
                    return result                                   # Jeśli udało się znaleźć rozwiązanie, zwróć ścieżkę prowadzącą do rozwiązania
                self.path = self.path[:-1]                          # Usuń ostatni ruch z ścieżki
        return None                                                 # Jeśli nie udało się znaleźć rozwiązania, zwróć None


