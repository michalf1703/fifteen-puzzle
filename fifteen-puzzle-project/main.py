import sys
import numpy as np
from puzzleBoard import puzzleBoard
from dfs import dfs
from bfs import bfs
from aStar import aStar


algorithm = sys.argv[1]                                         # wybór algorytmu przeszukiwania podany jako pierwszy argument przy wywołaniu skryptu
metric = sys.argv[2]                                            # wybór metryki do heurystyki podany jako drugi argument przy wywołaniu skryptu
with open(f"{sys.argv[3]}", "r") as f:                  # otwarcie pliku z puzzlem do rozwiązania
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")    # odczytanie wymiarów planszy z pliku
    # odczytanie planszy z pliku i przekształcenie jej do postaci macierzy numpy
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))

list_puzzle = data.flatten().tolist()                           # przekształcenie planszy do postaci listy
puzzle = puzzleBoard(cols, rows, list_puzzle, metric)            # utworzenie instancji obiektu klasy PuzzleNode reprezentującego początkowe ułożenie puzzle'a

result = None
visited_states = None
processed_states = None
algorithm_time = None
max_recursion = None


if sys.argv[1] == "dfs":                                        # jeśli wybrany algorytm to DFS, to wykonujemy poniższy blok kodu
    dfs = dfs()                                                 # utworzenie instancji obiektu klasy dfs (implementacja algorytmu DFS)
    result = dfs.solve(puzzle)                              # uruchomienie algorytmu DFS i zwrócenie znalezionego rozwiązania
    algorithm_time = dfs.get_time()                             # odczytanie czasu wykonania algorytmu DFS
    visited_states, processed_states = dfs.get_states_count()   # odczytanie liczby odwiedzonych i przetworzonych stanów przez algorytm DFS
    max_recursion = dfs.get_max_depth()                 # odczytanie maksymalnej głębokości rekursji osiągniętej przez algorytm DFS

elif sys.argv[1] == "bfs":                                      # jeśli wybrany algorytm to bfs, to wykonujemy poniższy blok kodu
    bfs = bfs(puzzle)                                           # utworzenie instancji obiektu klasy bds (implementacja algorytmu bfs)
    result = bfs.solve()                                    # uruchomienie algorytmu bfs i zwrócenie znalezionego rozwiązania
    algorithm_time = bfs.get_time()                             # odczytanie czasu wykonania algorytmu bfs
    visited_states, processed_states = bfs.get_states()   # odczytanie liczby odwiedzonych i przetworzonych stanów przez algorytm bfs
    max_recursion = bfs.get_max_depth()                 # odczytanie maksymalnej głębokości rekursji osiągniętej przez algorytm bfs


elif sys.argv[1] == "astr":                                     # jeśli wybrany algorytm to A*, to wykonujemy poniższy blok kodu
    astr = aStar(puzzle)                                        # utworzenie instancji obiektu klasy A* (implementacja algorytmu A*)
    result = astr.solve()                                       # uruchomienie algorytmu A* i zwrócenie znalezionego rozwiązania
    algorithm_time = astr.get_time()                            # odczytanie czasu wykonania algorytmu A*
    visited_states, processed_states = astr.get_states()      # odczytanie liczby odwiedzonych i przetworzonych stanów przez algorytm A*
    max_recursion = astr.get_max_depth()                # odczytanie maksymalnej głębokości rekursji osiągniętej przez algorytm A*

with open(f"solutions/{sys.argv[4]}", "w") as output_file:      # otwarcie pliku wynikowego, do którego zapisane zostaną rozwiązania lub komunikaty o błędach
    if result is not None:                                      # jeśli udało się znaleźć rozwiązanie, to zapisujemy je do pliku
        output_file.write(f"{len(result)}\n{result}")           # zapis długości rozwiązania i samego rozwiązania
    else:                                                       # jeśli nie udało się znaleźć rozwiązania, to zapisujemy informację o błędzie do pliku
        output_file.write("-1")

with open(f"solutions/{sys.argv[5]}", "w") as output_file:      # Otwieramy plik wyjściowy, w którym zapiszemy wyniki.
    if result is not None:                                      # W zależności od wartości zmiennej "result" wypisujemy długość ścieżki lub "-1".
        output_file.write(f"{len(result)}\n")
    else:
        output_file.write("-1\n")                               # Następnie zapisujemy ilość odwiedzonych i przetworzonych stanów, maksymalną rekursję oraz czas działania algorytmu.
    output_file.write(f"{visited_states}\n")
    output_file.write(f"{processed_states}\n")
    output_file.write(f"{max_recursion}\n")
    output_file.write(f"{algorithm_time}")
