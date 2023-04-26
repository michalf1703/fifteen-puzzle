import numpy as np
import sys
import board
import dfs




#argumenty startowe
if len(sys.argv) > 1:
    algorithm = sys.argv[1]
    parameter = sys.argv[2]
    startFile = sys.argv[3]
    endFile = sys.argv[4]
    additionalStats = sys.argv[5]

