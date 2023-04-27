import sys

import numpy as np
from puzzleNode import PuzzleNode
from dfs import dfs

algorithm = sys.argv[1]
metric = sys.argv[2]
with open(f"puzzles/{sys.argv[3]}", "r") as f:
    rows, cols = np.fromfile(f, dtype=int, count=2, sep=" ")
    data = np.fromfile(f, dtype=int, count=rows * cols, sep=" ").reshape((rows, cols))

list_puzzle = data.flatten().tolist()  # zamiana z numpy array na liste
puzzle = PuzzleNode(cols, rows, list_puzzle, metric)

result = None
visited_states = None
processed_states = None
algorithm_time = None
max_recursion = None
if sys.argv[1] == "dfs":
    dfs = dfs()
    result = dfs.dfs_start(puzzle)
    algorithm_time = dfs.algorithm_time()
    visited_states, processed_states = dfs.states_counter()
    max_recursion = dfs.recursion_reached()


with open(f"{sys.argv[4]}", "w") as output_file:
    if result is not None:
        output_file.write(f"{len(result)}\n{result}")
    else:
        output_file.write("-1")

with open(f"{sys.argv[5]}", "w") as output_file:
    if result is not None:
        output_file.write(f"{len(result)}\n")
    else:
        output_file.write("-1\n")
    output_file.write(f"{visited_states}\n")
    output_file.write(f"{processed_states}\n")
    output_file.write(f"{max_recursion}\n")
    output_file.write(f"{algorithm_time}")
