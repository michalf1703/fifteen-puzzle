import numpy as np
import sys
import board
import dfs
import fileOperations as read
import fileOperations as save
import time




#argumenty startowe
if len(sys.argv) > 1:
    algorithm = sys.argv[1]
    parameter = sys.argv[2]
    startFile = sys.argv[3]
    endFile = sys.argv[4]
    additionalStats = sys.argv[5]

board_tab = read.read_file(startFile)
board_width = read.get_width(startFile)
board_height = read.get_height(startFile)
board = board.Board(board_width,board_height,board_tab)

if algorithm == "dfs":
    solver = dfs.dfs()
    solvingStartTime = time.time_ns()
    solutionSequence = solver.solve(board,21,"","", parameter)
    solvingTime = time.time_ns() - solvingStartTime
    solvingTime = solvingTime / 1000000
    save.save_to_file(solver.found, endFile, additionalStats, solver.solution, solver.visitedStates, solver.processedStates.__len__(), solver.reachedDepth, solvingTime)
