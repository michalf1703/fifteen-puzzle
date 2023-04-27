#tu bedzie a*
"""
Algorytm A* : algorytm działa na takiej zasadzie, że umieszcza on na liście stanów otwartych umieszcza stanów
 - jednak w takiej kolejności, że wartości metryki w kolejności malejącej są bliżej zdjęcia z tej kolejki priorytetowej.

Algorytm A* nie porządkuje stanów w kolejce tylko i wyłącznie za pomocą funkcji heurysytcznej
- tylko funkcji oceny -> bierze ona pod uwagę wartość funkcji heurystycznej oraz dotychczasowy koszt
 dotarcia do bieżącego wierzchołka od stanu początkowego.

czyli: f(n) = g(n) + h(n)
"""

from queue import PriorityQueue


#psuedokod

"""
def aStar(G, s, g, h):
    p = PriorityQueue()
    T = set()
    p.put((0, s))
    while not p.empty():
        _, v = p.get()
        if v not in T:
            if G.isGoal(v):
                return "SUCCESS"
            T.add(v)
            for n in G.neighbours(v):
                if n not in T:
                    f = g(n) + h(n, G)
                    p.put((f, n))
    return "FAILURE"
"""
