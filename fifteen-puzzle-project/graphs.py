import chardet as chardet
import matplotlib.pyplot as plt
import numpy as np

def summary_graph(data, nr_criterion, name_criterion, name_file, use_log_scale):
    plt.clf()   #czyszczenie poprzedniego wykresu
    # tworzenie list sum_astar, sum_bfs, sum_dfs
    sum_astar = []  # pierwsze dla ilości zliczonych obiektów, reszta to głębokość rozwiązania = index
    sum_bfs = []
    sum_dfs = []
    for i in range(0, 8):
        sum_astar.append(0.0)
        sum_bfs.append(0.0)
        sum_dfs.append(0.0)

    # tworzenie tabel avg_astar_table, avg_bfs_table, avg_dfs_table
    avg_astar_table = []
    avg_bfs_table = []
    avg_dfs_table = []

    astar = [0.0]*7
    bfs = [0.0]*7
    dfs = [0.0]*7

    # przetwarzanie danych
    for d in data:
        if d[2] == 'astr':
            sum_astar[int(d[0])] += float(d[nr_criterion + 3])
            sum_astar[0] = sum_astar[0] + 1.0
            astar[int(d[0])-1] += 1.0
        if d[2] == 'bfs':
            sum_bfs[int(d[0])] += float(d[nr_criterion + 3])
            sum_bfs[0] = sum_bfs[0] + 1.0
            bfs[int(d[0])-1] += 1.0
        if d[2] == 'dfs':
            sum_dfs[int(d[0])] += float(d[nr_criterion + 3])
            sum_dfs[0] = sum_dfs[0] + 1.0
            dfs[int(d[0])-1] += 1.0

    # obliczanie średnich dla każdego algorytmu
    for i in range(0, 7):
        avg_astar_table.append(sum_astar[i + 1] / astar[i])
        avg_bfs_table.append(sum_bfs[i + 1] / bfs[i])
        avg_dfs_table.append(sum_dfs[i + 1] / dfs[i])

    # tworzenie wykresu
    x = [1, 2, 3, 4, 5, 6, 7]
   # y = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
    plt.hist([x, x, x], weights=[avg_bfs_table,avg_dfs_table, avg_astar_table], label=['DFS','BFS', 'A*'],
             color=['#4169E1','#FF8C00', '#228B22'], bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])
    # dodanie podziałki dla osi Y
    plt.yticks(range(0, 21, 1))
    plt.title('Ogółem')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(name_criterion)
    if nr_criterion == 2 or nr_criterion == 3 or nr_criterion ==5:
        plt.legend(('BFS','DFS', 'A*'), loc='upper right',bbox_to_anchor=(0.96, 0.88), borderaxespad=0.,
           bbox_transform=plt.gcf().transFigure)
    else:
        plt.legend(('BFS','DFS','A*'), loc='upper left')

    # opcjonalne skalowanie logarytmiczne osi y
    if use_log_scale is True:
        plt.yscale("log")

    # zapisanie wykresu do pliku
    plt.savefig('./graphs/' + name_file)

def astar_graph(data, nr_criterion, name_criterion, name_file, use_log_scale):
    # Czyszczenie aktualnego wykresu
    plt.clf()

    # Inicjalizacja tabeli sum Manhattana i sum Hamminga
    sum_manh = [0.0] * 8
    sum_hamm = [0.0] * 8

    # Inicjalizacja tablic średnich wartości dla kryteriów
    avg_manh_table = []
    avg_hamm_table = []

    # Inicjalizacja tablic wartości dla kryteriów
    manh = [0.0] * 7
    hamm = [0.0] * 7

    # Iteracja po danych wejściowych i obliczanie sum i wartości dla Manhattana i Hamminga
    for d in data:
        if d[2] == 'astr':
            if d[3] == 'manh':
                sum_manh[int(d[0])] += float(d[nr_criterion + 3])
                sum_manh[0] += 1
                manh[int(d[0])-1] += 1.0
            elif d[3] == 'hamm':
                sum_hamm[int(d[0])] += float(d[nr_criterion + 3])
                sum_hamm[0] += 1
                hamm[int(d[0])-1] += 1.0

    # Obliczanie średnich wartości dla kryteriów
    for i in range(0, 7):
        avg_manh_table.append(sum_manh[i + 1] / manh[i])
        avg_hamm_table.append(sum_hamm[i + 1] / hamm[i])

    # Konfiguracja histogramu
    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist(
        [x, x],
        weights=[avg_hamm_table,avg_manh_table],
        label=['Hamming','Manhattan'],
        color=['#4169E1', '#FF8C00'],
        bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5]
    )

    # Dodanie tytułu i etykiet osi
    plt.title('A*')
    if nr_criterion == 2:
        plt.yticks(range(0, 24, 1))
    plt.xlabel('Głębokość rozwiązania')
    if nr_criterion == 3:
        plt.yticks(range(0, 11, 1))
    plt.ylabel(name_criterion)
    if nr_criterion == 5:
        y_ticks = np.arange(0, 1.1, 0.1)
        plt.yticks(y_ticks)
    plt.ylabel(name_criterion)

    # Dodanie legendy
    plt.legend(('Hamming','Manhattan'), loc='upper left')

    # Dodanie skali logarytmicznej jeśli parametr use_log_scale jest True
    if use_log_scale:
        plt.yscale("log")

    # Zapisanie wykresu do pliku
    plt.savefig('./graphs/' + name_file)

def dfs_graph(data, nr_criterion, name_criterion, name_file, use_log_scale):

    plt.clf()
    # Inicjalizacja list z wynikami sum i średnich dla poszczególnych wzorców
    sum_RDUL = [0.0] * 8
    sum_RDLU = [0.0] * 8
    sum_DRUL = [0.0] * 8
    sum_DRLU = [0.0] * 8
    sum_LUDR = [0.0] * 8
    sum_LURD = [0.0] * 8
    sum_ULDR = [0.0] * 8
    sum_ULRD = [0.0] * 8
    avg_RDUL_table = []
    avg_RDLU_table = []
    avg_DRUL_table = []
    avg_DRLU_table = []
    avg_LUDR_table = []
    avg_LURD_table = []
    avg_ULDR_table = []
    avg_ULRD_table = []

    rdul = [0.0] * 7
    rdlu = [0.0] * 7
    drul = [0.0] * 7
    drlu = [0.0] * 7
    ludr = [0.0] * 7
    lurd = [0.0] * 7
    uldr = [0.0] * 7
    ulrd = [0.0] * 7

    # Obliczanie sum i zliczanie wystąpień dla poszczególnych wzorców
    for d in data:
        index = int(d[0])
        value = float(d[nr_criterion + 3])

        if d[2] == 'dfs':
            if d[3] == 'rdul':
                sum_RDUL[index] += value
                sum_RDUL[0] += 1
                rdul[index - 1] += 1
            elif d[3] == 'rdlu':
                sum_RDLU[index] += value
                sum_RDLU[0] += 1
                rdlu[index - 1] += 1
            elif d[3] == 'drul':
                sum_DRUL[index] += value
                sum_DRUL[0] += 1
                drul[index - 1] += 1
            elif d[3] == 'drlu':
                sum_DRLU[index] += value
                sum_DRLU[0] += 1
                drlu[index - 1] += 1
            elif d[3] == 'ludr':
                sum_LUDR[index] += value
                sum_LUDR[0] += 1
                ludr[index - 1] += 1
            elif d[3] == 'lurd':
                sum_LURD[index] += value
                sum_LURD[0] += 1
                lurd[index - 1] += 1
            elif d[3] == 'uldr':
                sum_ULDR[index] += value
                sum_ULDR[0] += 1
                uldr[index - 1] += 1
            elif d[3] == 'ulrd':
                sum_ULRD[index] += value
                sum_ULRD[0] += 1
                ulrd[index - 1] += 1
    # Pętla iterująca po indeksach 0 do 6 (włącznie)
    for i in range(0, 7):
        # Obliczamy średnie wartości dla każdego ruchu
        avg_RDUL_table.append(sum_RDUL[i + 1] / rdul[i])
        avg_RDLU_table.append(sum_RDLU[i + 1] / rdlu[i])
        avg_DRUL_table.append(sum_DRUL[i + 1] / drul[i])
        avg_DRLU_table.append(sum_DRLU[i + 1] / drlu[i])
        avg_LUDR_table.append(sum_LUDR[i + 1] / ludr[i])
        avg_LURD_table.append(sum_LURD[i + 1] / lurd[i])
        avg_ULDR_table.append(sum_ULDR[i + 1] / uldr[i])
        avg_ULRD_table.append(sum_ULRD[i + 1] / ulrd[i])

    # Definiujemy listę x zawierającą wartości 1-7
    x = [1, 2, 3, 4, 5, 6, 7]

    # Tworzymy histogram
    plt.hist([x, x, x, x, x, x, x, x],
             # Wagi dla każdego ruchu
             weights=[avg_RDUL_table, avg_RDLU_table, avg_DRUL_table, avg_DRLU_table, avg_LUDR_table, avg_LURD_table,
                      avg_ULDR_table, avg_ULRD_table],
             # Etykiety dla każdego ruchu
             label=['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'],
             # Kolory dla każdego ruchu
             color=['#4169E1', '#FF8C00', '#228B22', '#A52A2A', '#9932CC', '#A0522D', '#FF69B4', '#808080'],
             # Zakresy przedziałów histogramu
             bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])

    # Dodajemy tytuł, opisy osi oraz legendę
    plt.title('DFS')
    if nr_criterion == 1:
        plt.yticks(range(0, 21, 1))
    elif nr_criterion == 2:
        y_ticks = np.arange(0, 1100000, 50000)
        plt.yticks(y_ticks)
    elif nr_criterion == 3:
        y_ticks = np.arange(0, 1100000, 50000)
        plt.yticks(y_ticks)
    elif nr_criterion == 4:
        y_ticks = np.arange(0, 21, 1)
        plt.yticks(y_ticks)
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(name_criterion)
    plt.legend(('RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'), loc='upper right',bbox_to_anchor=(1.005, 0.88), borderaxespad=0.,
           bbox_transform=plt.gcf().transFigure)


    # Jeśli strange_numbers ma wartość True, ustawiamy skalę osi
    if use_log_scale is True:
        plt.yscale("log")
    plt.savefig('./graphs/' + name_file)

def bfs_graph(data, nr_criterion, name_criterion, name_file, use_log_scale):
    plt.clf()
    # Tworzenie pustych list na sumy punktów dla każdego kierunku
    sum_RDUL = [0.0] * 8
    sum_RDLU = [0.0] * 8
    sum_DRUL = [0.0] * 8
    sum_DRLU = [0.0] * 8
    sum_LUDR = [0.0] * 8
    sum_LURD = [0.0] * 8
    sum_ULDR = [0.0] * 8
    sum_ULRD = [0.0] * 8

    # Inicjalizacja list na ilości wystąpień dla każdego kierunku
    rdul = [0.0] * 7
    rdlu = [0.0] * 7
    drul = [0.0] * 7
    drlu = [0.0] * 7
    ludr = [0.0] * 7
    lurd = [0.0] * 7
    uldr = [0.0] * 7
    ulrd = [0.0] * 7
    for d in data:
        index = int(d[0])
        value = float(d[nr_criterion + 3])
        if d[2] == 'bfs':
            if d[3] == 'rdul':
                sum_RDUL[index] += value
                sum_RDUL[0] += 1
                rdul[index - 1] += 1
            elif d[3] == 'rdlu':
                sum_RDLU[index] += value
                sum_RDLU[0] += 1
                rdlu[index - 1] += 1
            elif d[3] == 'drul':
                sum_DRUL[index] += value
                sum_DRUL[0] += 1
                drul[index - 1] += 1
            elif d[3] == 'drlu':
                sum_DRLU[index] += value
                sum_DRLU[0] += 1
                drlu[index - 1] += 1
            elif d[3] == 'ludr':
                sum_LUDR[index] += value
                sum_LUDR[0] += 1
                ludr[index - 1] += 1
            elif d[3] == 'lurd':
                sum_LURD[index] += value
                sum_LURD[0] += 1
                lurd[index - 1] += 1
            elif d[3] == 'uldr':
                sum_ULDR[index] += value
                sum_ULDR[0] += 1
                uldr[index - 1] += 1
            elif d[3] == 'ulrd':
                sum_ULRD[index] += value
                sum_ULRD[0] += 1
                ulrd[index - 1] += 1
    # Obliczanie średniej wartości kryterium dla każdego z ruchów RDLU, RULD, DRUL, DRLU, LUDR, LURD, ULDR, ULRD.
    avg_RDUL_table = [sum_RDUL[i + 1] / rdul[i] for i in range(0, 7)]
    avg_RDLU_table = [sum_RDLU[i + 1] / rdlu[i] for i in range(0, 7)]
    avg_DRUL_table = [sum_DRUL[i + 1] / drul[i] for i in range(0, 7)]
    avg_DRLU_table = [sum_DRLU[i + 1] / drlu[i] for i in range(0, 7)]
    avg_LUDR_table = [sum_LUDR[i + 1] / ludr[i] for i in range(0, 7)]
    avg_LURD_table = [sum_LURD[i + 1] / lurd[i] for i in range(0, 7)]
    avg_ULDR_table = [sum_ULDR[i + 1] / uldr[i] for i in range(0, 7)]
    avg_ULRD_table = [sum_ULRD[i + 1] / ulrd[i] for i in range(0, 7)]

    # Tworzenie histogramu, który przedstawia rozkład wartości kryterium dla każdego z ruchów.
    x = [1, 2, 3, 4, 5, 6, 7]
    plt.hist([x, x, x, x, x, x, x, x],
             # Wagi dla każdego ruchu
             weights=[avg_RDUL_table, avg_RDLU_table, avg_DRUL_table, avg_DRLU_table, avg_LUDR_table, avg_LURD_table,
                      avg_ULDR_table, avg_ULRD_table],
             # Etykiety dla każdego ruchu
             label=['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'],
             # Kolory dla każdego ruchu
             color=['#4169E1', '#FF8C00', '#228B22', '#A52A2A', '#9932CC', '#A0522D', '#FF69B4', '#808080'],
             # Zakresy przedziałów histogramu
             bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])

    # Ustawienie tytułu oraz etykiet osi na wykresie.
    plt.title('BFS')
    if nr_criterion == 2:
        plt.yticks(range(0, 1050, 50))
    if nr_criterion == 3:
        plt.yticks(range(0, 450, 25))
    if nr_criterion == 5:
        y_ticks = np.arange(0, 9.5, 0.5)
        plt.yticks(y_ticks)
    plt.xlabel('Głębokość rozwiązania')
    plt.ylabel(name_criterion)
    plt.legend(('RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD'), loc='upper left')

    # Opcjonalne ustawienie skali osi Y na logarytmiczną.
    if use_log_scale is True:
        plt.yscale("log")
    # Zapisanie wykresu do pliku.
    plt.savefig('./graphs/' + name_file)

with open('dane_do_sprawka.csv', 'rb') as f:
    enc = chardet.detect(f.read())

with open("dane_do_sprawka.csv", 'r', encoding=enc['encoding']) as csvfile:
    # Stwórz czytnik csv
    dataFrame = list()
    i=0
    for line in csvfile.readlines():
        array = line.split()
        dataFrame.append(array)

        i += 1

# Wyświetl tablicę_dwuwymiarową
for i in range(0,int(dataFrame.__sizeof__()/9)):
    print(dataFrame[i], '\n')

summary_graph(dataFrame, 1, "Długość rozwiązania", "ogolne_dlugosc_rozwiazania", False)
astar_graph(dataFrame, 1, "Długość rozwiązania", "astr_dlugosc_rozwiazania", False)
dfs_graph(dataFrame, 1, "Długość rozwiązania", "dfs_dlugosc_rozwiazania", False)
bfs_graph(dataFrame, 1, "Długość rozwiązania", "bfs_dlugosc_rozwiazania", False)

summary_graph(dataFrame, 2, "Liczba stanów odwiedzonych w skali logarytmicznej", "ogolne_odwiedzone", True)
astar_graph(dataFrame, 2, "Liczba stanów odwiedzonych", "astr_odwiedzone", False)
bfs_graph(dataFrame, 2, "Liczba stanów odwiedzonych w skali logarytmicznej", "bfs_odwiedzone", True)
dfs_graph(dataFrame, 2, "Liczba stanów odwiedzonych w skali logarytmicznej", "dfs_odwiedzone", True)

summary_graph(dataFrame, 3, "Liczba stanów przetworzonych w skali logarytmicznej", "ogolne_przetworzone", True)
astar_graph(dataFrame, 3, "Liczba stanów przetworzonych", "astr_przetworzone", False)
bfs_graph(dataFrame, 3, "Liczba stanów przetworzonych w skali logarytmicznej", "bfs_przetworzone", True)
dfs_graph(dataFrame, 3, "Liczba stanów przetworzonych w skali logarytmicznej", "dfs_przetworzone", True)

summary_graph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "ogolne_głębokość", False)
astar_graph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "astr_głębokość", False)
bfs_graph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "bfs_głębokość", False)
dfs_graph(dataFrame, 4, "Maksymalna osiągnięta głębokość rekursji", "dfs_głębokość", False)

summary_graph(dataFrame, 5, "Czas trwania procesu obliczeniowego[ms] w skali logarytmicznej", "ogolne_czas", True)
astar_graph(dataFrame, 5, "Czas trwania procesu obliczeniowego[ms]", "astr_czas", False)
bfs_graph(dataFrame, 5, "Czas trwania procesu obliczeniowego[ms] w skali logarytmicznej", "bfs_czas", True)
dfs_graph(dataFrame, 5, "Czas trwania procesu obliczeniowego[ms] w skali logarytmicznej", "dfs_czas", True)