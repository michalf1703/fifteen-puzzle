
"""
===> Omówienie BFS (ang. breadth-first-search):

* W przypadku tego algortymu potrzebna będzie struktura danych (ang. open list) - lista stanów otwartych - w przyapdku poznania sąsiadów dla danego elementu i będą wprowadzane do listy stanów otwartych.

* Jeżli algorytm operuje na liście stanów otwartych to nie działa taki algorytm najlepiej - bo niektóre stany będą odpytywane ponownie.

* Lista stanów zamkniętych (ang. closed - listed / explored) - przechowywana jest tam informacja o tym czy dany stan był już przepytywany (a do tego charakteryzuje się szybszym przeszukiwaniem)

"""


#pseudokod
"""
function dfs(G, s)
	if G.isgoal(s)
		return SUCCESS
	S = stack()
	T = set()
	S.push(s)
	while ~S.isempty()
		v = S.pop()
		T.add(v)
		for n in reverse(G.neighbours(n))
			if G.isgoal()
				return SUCCESS
			if ~T.has(n) and ~S.has(n)
				S.push(n)
	return FAILURE
"""