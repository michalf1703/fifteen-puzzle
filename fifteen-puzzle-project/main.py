import sys

import numpy as np
from puzzleNode import PuzzleNode
from dfs import dfs

algorithm = sys.argv[1]  # wybór algorytmu przeszukiwania podany jako pierwszy argument przy wywołaniu skryptu
metric = sys.argv[2]  # wybór metryki do heurystyki podany jako drugi argument przy wywołaniu skryptu
with open(f"puzzles/{sys.argv[3]}", "r") as f:  # otwarcie pliku z puzzlem do rozwiązania
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")  # odczytanie wymiarów planszy z pliku
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))  # odczytanie planszy z pliku i przekształcenie jej do postaci macierzy numpy

list_puzzle = data.flatten().tolist()  # przekształcenie planszy do postaci listy
puzzle = PuzzleNode(cols, rows, list_puzzle, metric)  # utworzenie instancji obiektu klasy PuzzleNode reprezentującego początkowe ułożenie puzzle'a

result = None
visited_states = None
processed_states = None
algorithm_time = None
max_recursion = None
if sys.argv[1] == "dfs":  # jeśli wybrany algorytm to DFS, to wykonujemy poniższy blok kodu
    dfs = dfs()  # utworzenie instancji obiektu klasy dfs (implementacja algorytmu DFS)
    result = dfs.dfs_start(puzzle)  # uruchomienie algorytmu DFS i zwrócenie znalezionego rozwiązania
    algorithm_time = dfs.algorithm_time()  # odczytanie czasu wykonania algorytmu DFS
    visited_states, processed_states = dfs.states_counter()  # odczytanie liczby odwiedzonych i przetworzonych stanów przez algorytm DFS
    max_recursion = dfs.recursion_reached()  # odczytanie maksymalnej głębokości rekursji osiągniętej przez algorytm DFS

with open(f"{sys.argv[4]}", "w") as output_file:  # otwarcie pliku wynikowego, do którego zapisane zostaną rozwiązania lub komunikaty o błędach
    if result is not None:  # jeśli udało się znaleźć rozwiązanie, to zapisujemy je do pliku
        output_file.write(f"{len(result)}\n{result}")  # zapis długości rozwiązania i samego rozwiązania
    else:  # jeśli nie udało się znaleźć rozwiązania, to zapisujemy informację o błędzie do pliku
        output_file.write("-1")

# Otwieramy plik wyjściowy, w którym zapiszemy wyniki.
# W zależności od wartości zmiennej "result" wypisujemy długość ścieżki lub "-1".
# Następnie zapisujemy ilość odwiedzonych i przetworzonych stanów, maksymalną rekursję oraz czas działania algorytmu.
with open(f"{sys.argv[5]}", "w") as output_file:
    if result is not None:
        output_file.write(f"{len(result)}\n")
    else:
        output_file.write("-1\n")
    output_file.write(f"{visited_states}\n")
    output_file.write(f"{processed_states}\n")
    output_file.write(f"{max_recursion}\n")
    output_file.write(f"{algorithm_time}")
