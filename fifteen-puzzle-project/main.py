import numpy as np
import sys



#długość znalezionego rozwiązania, liczba stanow odwiedzonych, liczba stanow przetworzonych, maksymalna osiagnieta głębokość rekursji, czas trwania procesu obliczeniowego


#argumenty startowe
if len(sys.argv) > 1:
    algorithm = sys.argv[1]
    parameter = sys.argv[2]
    startFile = sys.argv[3]
    endFile = sys.argv[4]
    additionalStats = sys.argv[5]
