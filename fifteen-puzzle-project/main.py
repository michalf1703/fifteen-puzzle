import numpy as np
import sys



#długość znalezionego rozwiązania, liczba stanow odwiedzonych, liczba stanow przetworzonych, maksymalna osiagnieta głębokość rekursji, czas trwania procesu obliczeniowego

lenght_of_the_solution = None
visited_states = None
processed_states = None
max_recursion_depth = None
time_of_algorithm = None

#argumenty startowe
if len(sys.argv) > 1:
    algorithm = sys.argv[1]
    parameter = sys.argv[2]
    startFile = sys.argv[3]
    endFile = sys.argv[4]
    additionalStats = sys.argv[5]
