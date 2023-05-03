import subprocess, sys



tab = ["RDUL", "RDLU", "DRUL","DRLU","LUDR","LURD","ULDR","ULRD"]




for i in tab:

    p = subprocess.Popen(["powershell.exe", f"C:\\Users\\Hp\\Documents\\GitHub\\fifteen-puzzle\\fifteen-puzzle-project\\puzzles\\przeszukiwania.ps1 -strategy bfs -param {i}"], stdout=sys.stdout)
    p.communicate()

