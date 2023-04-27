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
        self.path = ""  # zmienna przechowująca ścieżkę do rozwiązania
        self.visited = {}  # słownik przechowujący odwiedzone stany, gdzie klucz to hash stanu, wartość to długość ścieżki
        self.max_depth = 20  # maksymalna dozwolona głębokość przeszukiwania
        self.visited_states = 1  # liczba odwiedzonych stanów
        self.processed_states = 0  # liczba przetworzonych stanów
        self.elapsed_time = 0  # czas wykonania algorytmu
        self.max_recursion_reached = 0  # maksymalna głębokość rekursji, osiągnięta podczas działania algorytmu

    def dfs_start(self, board):
        """
        Funkcja uruchamiająca algorytm DFS i zwracająca rozwiązanie.
        :param board: początkowy stan planszy
        :return: ścieżka do rozwiązania
        """
        start_time = time.time()  # mierzymy czas wykonania algorytmu
        result = self.dfs_solve(board)  # uruchamiamy funkcję rozwiązującą problem
        self.elapsed_time = time.time() - start_time  # obliczamy czas wykonania algorytmu
        return result

    def dfs_solve(self, board):
        # Zwiększ licznik przetworzonych stanów
        self.processed_states += 1

        # Sprawdź, czy aktualna głębokość przeszukiwania nie przekracza maksymalnej
        if board.depth > self.max_depth:
            return None

        # Sprawdź, czy aktualna głębokość przekroczyła maksymalną osiągniętą głębokość
        if board.depth >= self.max_recursion_reached:
            self.max_recursion_reached = board.depth

        # Sprawdź, czy plansza jest rozwiązana
        if board.is_solved():
            return self.path

        # Dodaj hasz planszy do odwiedzonych, z kluczem jako haszem i wartością jako długość ścieżki
        self.visited[board.__hash__()] = board.depth

        # Wykonaj ruch na planszy i znajdź jej sąsiadów
        board.move()
        for neighbor in board.get_neighbors():
            # Zwiększ licznik odwiedzonych stanów
            self.visited_states += 1

            # Jeśli sąsiad już był odwiedzony i ścieżka do niego jest krótsza, to pomijamy ten stan
            # W przeciwnym przypadku odwiedzamy ten stan
            if (neighbor.__hash__() in self.visited and neighbor.depth < self.visited[
                neighbor.__hash__()]) or neighbor.__hash__() not in self.visited:
                # Dodaj ostatni ruch planszy do ścieżki
                self.path += neighbor.last_move

                # Rekurencyjnie rozwiąż planszę z sąsiadem
                result = self.dfs_solve(neighbor)
                if result is not None:
                    return result

                # Usuń ostatni ruch z ścieżki
                self.path = self.path[:-1]

        # Zwróć wartość None, gdy nie znaleziono rozwiązania
        return None

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
