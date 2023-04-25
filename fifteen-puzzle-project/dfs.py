import time
SUCCESS = "SOLVED"
FAILURE = "UNSOLVABLE"

#tutaj pseudokod na ktorym bede sie opierac
def dfs(G, s):
    if G.isgoal(s):
        return True
    S = []
    T = set()
    S.append(s)
    while len(S) > 0:
        v = S.pop()
        T.add(v)
        for n in reversed(G.neighbours(v)):
            if G.isgoal(n):
                return True
            if n not in T and n not in S:
                S.append(n)
    return True

