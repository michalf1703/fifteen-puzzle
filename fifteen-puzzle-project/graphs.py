from _csv import reader
import csv as csv
import chardet as chardet
import matplotlib.pyplot as plt

def summaryGraph(data, nr_criterion, name_criterion, name_file, other_numbers):
    plt.clf()

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
    plt.hist([x, x, x], weights=[avg_astar_table, avg_bfs_table, avg_dfs_table], label=['A*', 'BFS', 'DFS'],
             color=['blue', 'purple', 'green'], bins=[0.5, 1.5, 2.5, 3.6, 4.5, 5.5, 6.5, 7.5])
    plt.title('Ogólne')
    plt.xlabel('Głębokość rozwiazania')
    plt.ylabel(name_criterion)
    plt.legend(('A*', 'BFS', 'DFS'), loc='upper left')

    # opcjonalne skalowanie logarytmiczne osi y
    if other_numbers is True:
        plt.yscale("log")

    # zapisanie wykresu do pliku
    plt.savefig('./graphs/' + name_file)


with open('wszystkie_dane.csv', 'rb') as f:
    enc = chardet.detect(f.read())

with open("wszystkie_dane.csv", 'r', encoding=enc['encoding']) as csvfile:
    # Stwórz czytnik csv
    dataFrame = list()
    i=0
    for line in csvfile.readlines():
        array = line.split()
        dataFrame.append(array)

        i += 1
        #list.append(array)

    #print(dataFrame)

# Wyświetl tablicę_dwuwymiarową
for i in range(0,int(dataFrame.__sizeof__()/9)):
    print(dataFrame[i], '\n')


summaryGraph(dataFrame, 1, "Długość rozwiązania", "ogolne_dlugosc_rozwiazania", False)