import time

"""
=> Omówienie algorytmu przeszukiwania "w głąb" - (ang. depth-first-search).

Graf - musi być to graf skierowany, gdzie krawędzie są skierowane (do tego muszą być etykietowane operacjami - dokładnie operatorami) - jednak nie ma ich na wykresie, jako, że źle to wpływa na czytleność.

Bazowa reprezentacja metody / algorytmu DFS jest jako funkcja rekurencyjna - nie ma z tego potrzeby przechowywania listy stanów otwartych. Jendak wymagana jest lista stanów zamkniętych - jednak w tym przypadku musi być ona globalna (musi być dostępna dla każdego wywołania funkcji).
"""

#pseudokod:
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
class dfs:
    def __init__(self):
        # Inicjalizacja zmiennych używanych w algorytmie DFS
        self.path = ""                                      # zmienna przechowująca ścieżkę do rozwiązania
        self.visited = {}                                   # słownik przechowujący odwiedzone stany, gdzie klucz to hash stanu, wartość to długość ścieżki
        self.max_depth = 20                                 # maksymalna dozwolona głębokość przeszukiwania
        self.visited_states = 1                             # liczba odwiedzonych stanów
        self.processed_states = 0                           # liczba przetworzonych stanów
        self.elapsed_time = 0                               # czas wykonania algorytmu
        self.max_recursion_reached = 0                      # maksymalna głębokość rekursji, osiągnięta podczas działania algorytmu

    def dfs_start(self, board):
        """
        Funkcja uruchamiająca algorytm DFS i zwracająca rozwiązanie.
        :param board: początkowy stan planszy
        :return: ścieżka do rozwiązania
        """
        start_time = time.time()                            # mierzymy czas wykonania algorytmu
        result = self.dfs_solve(board)                      # uruchamiamy funkcję rozwiązującą problem
        self.elapsed_time = time.time() - start_time        # obliczamy czas wykonania algorytmu
        return result

    def dfs_solve(self, board):
        self.processed_states += 1                                  # Licznik odwiedzonych stanów planszy
        if self.max_depth is not None and board.depth > self.max_depth:
            return None                                             # Jeśli osiągnięto maksymalną głębokość i plansza przekracza ją, to zwróć None
        if board.depth >= self.max_recursion_reached:
            self.max_recursion_reached = board.depth                # Aktualizacja największej dotychczasowej głębokości rekursji
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
                self.path += neighbor.last_move                     # Dodaj ostatni ruch do ścieżki
                result = self.dfs_solve(neighbor)                   # Rekurencyjne wywołanie dfs_solve dla sąsiedniej planszy
                if result is not None:
                    return result                                   # Jeśli udało się znaleźć rozwiązanie, zwróć ścieżkę prowadzącą do rozwiązania
                self.path = self.path[:-1]  # Usuń ostatni ruch z ścieżki
        return None  # Jeśli nie udało się znaleźć rozwiązania, zwróć None


    def states_counter(self):
        """
        Zwraca liczbę odwiedzonych i przetworzonych stanów podczas działania algorytmu.
        :return: krotka z dwoma liczbami: (odwiedzone, przetworzone)
        """
        return self.visited_states, self.processed_states

    def get_algorithm_time(self):
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
        return self.max_recursion_reached
