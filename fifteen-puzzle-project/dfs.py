import board as a_operations
class Dfs:
    def __init__(self):
        self.visited_states = 1  # liczba odwiedzonych stanów
        self.reached_depth = 0  # maksymalna osiągnięta głębokość przeszukiwania
        self.found = False  # flaga wskazująca, czy znaleziono rozwiązanie
        self.processed_states = {}  # słownik przechowujący informacje o przetworzonych stanach
        self.solution = ''  # znalezione rozwiązanie

    def solve(self, board, max_depth, last_move, solution, order):
        # Przerywamy przeszukiwanie, jeśli przekroczona zostanie maksymalna głębokość
        if board.depth > max_depth:
            return

        # Aktualizujemy maksymalną osiągniętą głębokość
        if self.reached_depth < board.depth:
            self.reached_depth = board.depth

        # Dodajemy ruch do rozwiązania
        solution += last_move

        # Sprawdzamy, czy osiągnęliśmy stan końcowy
        if board.check_board() is True:
            self.found = True
            self.solution = solution  # zapisujemy rozwiązanie
            return solution

        # Wykonujemy dostępne ruchy
        moves = a_operations.next_moves_in_order(order, board)
        self.visited_states += len(moves)  # aktualizujemy liczbę odwiedzonych stanów
        for move in moves:
            new_state = board.__deepcopy__()  # tworzymy kopię aktualnego stanu
            zero_index = a_operations.find_zero(new_state)  # znajdujemy indeks zera
            a_operations.make_move(new_state, move, zero_index)  # wykonujemy ruch
            new_state.depth += 1  # aktualizujemy głębokość
            if (new_state.__hash__() not in self.processed_states) or \
                    (self.processed_states[new_state.__hash__()] > new_state.depth):
                self.processed_states[new_state.__hash__()] = new_state.depth
                self.solve(new_state, max_depth, move, solution, order)
            if self.found:
                return
        return
