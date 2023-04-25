
SUCCESS = "SOLVED"
FAILURE = "UNSOLVABLE"

#na ta chwile jest to pseudokod z zajęć

def dfs(G, s):
    if G.isgoal(s):
        return SUCCESS
    S = []
    T = set()
    S.append(s)
    while len(S) > 0:
        v = S.pop()
        T.add(v)
        for n in reversed(G.neighbours(v)):
            if G.isgoal(n):
                return SUCCESS
            if n not in T and n not in S:
                S.append(n)
    return FAILURE


