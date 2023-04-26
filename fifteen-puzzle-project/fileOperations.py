

#######################read#############

"""
Funkcja readFile wczytuje planszę z pliku, pomijając pierwszą linię zawierającą wymiary planszy. Funkcja zwraca listę z wartościami pól planszy.
"""
def read_file(file_name):
    # Otwórz plik o podanej nazwie w trybie odczytu
    f = open(file_name, "r")

    tab = []
    # Iteruj przez każdą linię pliku
    for i, line in enumerate(f.readlines()):
        # Pomijamy pierwszą linię (zawierającą tylko wymiary)
        if i > 0:
            # Usuwamy białe znaki z początku i końca linii i dzielimy ją na elementy
            row = line.strip().split(" ")
            for element in row:
                # Dodajemy każdy element do listy tablicy
                tab.append(element)

    # Zamykamy plik
    f.close()

    # Zwracamy tablicę
    return tab

"""
Funkcja getHeight odczytuje wysokość planszy z pliku, konwertuje ją na liczbę całkowitą i zwraca.
"""
def get_height(file_name):
    # Otwórz plik o podanej nazwie w trybie odczytu
    f = open(file_name, "r")

    # Odczytujemy pierwszą linię, dzielimy ją na elementy i zwracamy pierwszy element (wysokość)
    line = f.readline().strip().split(" ")
    height = line[0]

    # Zamykamy plik
    f.close()

    # Konwertujemy wysokość na liczbę całkowitą i zwracamy
    return int(height)

"""
Funkcja getWidth odczytuje szerokość planszy z pliku, konwertuje ją na liczbę całkowitą i zwraca.
"""
def get_width(file_name):
    # Otwórz plik o podanej nazwie w trybie odczytu
    f = open(file_name, "r")

    # Odczytujemy pierwszą linię, dzielimy ją na elementy i zwracamy drugi element (szerokość)
    line = f.readline().strip().split(" ")
    width = line[1]

    # Zamykamy plik
    f.close()

    # Konwertujemy szerokość na liczbę całkowitą i zwracamy
    return int(width)



################################## SAVE ##########################

def save_solution(solved, solution_filename, solution):
    # Otwieramy plik z rozwiązaniem w trybie 'w' (zapisu)
    with open("./solutions/" + solution_filename, 'w') as f:
        # Jeśli znaleziono rozwiązanie, zapisujemy długość rozwiązania i samo rozwiązanie w pliku
        if solved:
            f.write(str(len(solution)))
            f.write('\n' + solution)
        # W przeciwnym przypadku zapisujemy tylko "-1"
        else:
            f.write('-1')

def save_additional_info(solved, info_filename, solution, visited_states, processed_states, max_depth, exec_time):
    # Otwieramy plik z dodatkowymi informacjami w trybie 'w' (zapisu)
    with open("./solutions/" + info_filename, 'w') as f:
        # Jeśli znaleziono rozwiązanie, zapisujemy długość rozwiązania w pliku
        if solved:
            f.write(str(len(solution)))
        # W przeciwnym przypadku zapisujemy tylko "-1"
        else:
            f.write('-1')
        # Zapisujemy liczbę odwiedzonych stanów, liczbę przetworzonych stanów, maksymalną głębokość oraz czas wykonania w pliku
        f.write('\n' + str(visited_states))
        f.write('\n' + str(processed_states))
        f.write('\n' + str(max_depth))
        exec_time = round(exec_time, 3)
        f.write('\n' + str(exec_time))

def save_to_file(solved, solution_filename, info_filename, solution, visited_states, processed_states, max_depth, exec_time):
    # Zapisujemy rozwiązanie oraz dodatkowe informacje do dwóch różnych plików
    save_solution(solved, solution_filename, solution)
    save_additional_info(solved, info_filename, solution, visited_states, processed_states, max_depth, exec_time)

