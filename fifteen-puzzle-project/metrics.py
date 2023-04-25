
"""
metryka hamminga - jest to metryka, która sprawdza czy dany element jest na swoim miejscu - jeżeli nie jest to zwraca jeden,
 a jak jest zero, to zwraca zero - wówczas koszty można zsmuować - im wyższa wartość tym gorzej(bo oznacza to,
 że dużo kafelków nie jest na swojej pozycji
"""
def hamming_metric(self):
    """
    Oblicza metrykę odległości Hamminga, czyli liczbę kafelków w niewłaściwej pozycji.
    """
    distance = sum(1 for i, tile in enumerate(self.tab) if tile != str(i + 1) and tile != "0")
    distance += self.depth
    self.cost = distance
    return distance

"""
Metryka Manhatan - odległość jest liczona wzdłóż określonych współrzędnych, które są dalej sumowane - 
w wyniku uzyskuje się odległość - wówczas dla każdego bloczka sumuje się te odległości - i im wyższa jest wartość tej metryki
 - to jest gorzej - jeżeli odległość jest niewielka to znaczy, że układ jest blisko stanu docelowego.
"""
def manhattan_metric(self):
    """
    Oblicza metrykę odległości Manhattanu, która jest sumą odległości każdego pola od jego idealna pozycja.
    """
    distance = 0
    for i, tile in enumerate(self.tab):
        if tile != "0":
            current_row, current_col = self.get_xy_position(i)
            target_row, target_col = self.get_xy_position(int(tile) - 1)
            distance += abs(current_row - target_row) + abs(current_col - target_col)
    distance += self.depth
    self.cost = distance
    return distance




