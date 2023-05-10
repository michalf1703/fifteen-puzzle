from timeit import default_timer
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
        start_time = default_timer()                                                 # pobranie czasu rozpoczęcia wykonywania algorytmu w nanosekundach
        open_set = PriorityQueue()                                                  # tworzenie listę , która jest kolejka priorytetowa na węzły do odwiedzenia
        open_set.put((0, self.puzzle))                                              # wkładanie do kolejki węzeła: koszt i dany stan, nie ma znaczenia czy koszt bedzie 0 czy inny, bo i tak zaraz zdejmujemy z kolejki
        processed_states_dictionary = dict()                                        # tworzenie słownika przechowującego już odwiedzone stany wraz z ich kosztami
        while not open_set.empty():                                                 #sprawdzenie czy lista przechowująca stany odwiedzone jest pusta
            current_board_state = open_set.get()[1]                                 # wyjmowanie węzła, który ma najniższy koszt
            if current_board_state.depth >= self.max_depth:                         # sprawdzenie czy aktualna głębokość węzła nie przekracza aktualnej maksymalnej głębokości
                self.max_depth = current_board_state.depth                          # aktualziacja wartości największej osiągniętej głębokości
            self.processed_states += 1                                              # zwiększenie liczby przetworzonych stanów
            processed_states_dictionary[current_board_state.__hash__()] = current_board_state.depth  # dodanie aktualny stan do słownika przetworzonych stanów, prównanie głębokości
            if current_board_state.is_goal():
                path = ""
                while current_board_state.last_move != "":              # Przechodzimy po rodzicach w celu odnalezienia rozwiązania
                    path += current_board_state.last_move
                    current_board_state = current_board_state.parent
                reversed_path = path[::-1]                  # Odwracamy scieżkę, aby otrzymać poprawny wynik
                self.time = (default_timer() - start_time) *1000
                return reversed_path
            current_board_state.move()
            for neighbor in current_board_state.get_neighbors():
                self.visited_states += 1                     # Zwiększamy liczbę odwiedzonych stanów
                if (neighbor.__hash__() in processed_states_dictionary and neighbor.depth < processed_states_dictionary[neighbor.__hash__()]) or neighbor.__hash__() not in processed_states_dictionary:
                    cost = neighbor.depth + neighbor.get_metric_cost()  # Obliczamy koszt danego stanu
                    board_and_cost = (cost, neighbor)
                    is_in_queue = False
                    for item in open_set.queue:
                        if item == board_and_cost:
                            is_in_queue = True
                            break
                    if not is_in_queue:
                        open_set.put((cost, neighbor))
        self.time = (default_timer() - start_time) *1000  # Obliczamy czas wykonania algorytmu
        return None

#koszt = koszt danego węzła + koszt heurystyczny
#licznik stanów przetworzonych zwiększa się w momencie, gdy algorytm pobiera nowy węzeł z najniższym kosztem ze zbioru otwartego
#słownik przetworzonych stanów służy do przechowywania informacji o już odwiedzonych stanach, co pozwala na uniknięcie powtarzania tych samych stanów.
#l:34 jeżeli algorytm natrafi na stan, który już został odwiedzony i jest przechowywany w słowniku stanów odwiedzonych to następuje porównanie
#głębokości aktualnego stanu z tą głębokością, którą przechowuje słownik przetworzonych dla danego stanu.
#jeżeli aktualna głębokość jest mniejsza niż
