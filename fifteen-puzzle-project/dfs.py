import time
SUCCESS = "SOLVED"
FAILURE = "UNSOLVABLE"

#tutaj pseudokod na ktorym bede sie opierac



processed_states = None

time_of_algorithm = None
class dfs:

    def __int__(self):

        self.solution = ''                  #rozwiazanie
        self.visited_states = 1             #stany odwiedzone
        self.processed_states = {}          #stany przetworzone
        self.max_depth = 0                  #liczba stanów przetworzonych
        self.found = False
        self.time = None                    #nie wiem czy wykorzystam tutaj



    def dfs_solve(self, board, max_depth,lastmove,solution, order):

        #start algorytmu
        if board.is_goal() is True:
            self.found = True
            self.solution =

