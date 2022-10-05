from models.KeyTriple import KeyTriple

class TripleSet:
    def __init__(self, *triples):
        self.triple_set = [KeyTriple(*triple) for triple in triples]

    def check_win(self) -> str:
        empty_cells_counter = 0

        win = None

        for triple in self.triple_set:
            win = triple.check_row()
            
            if win:
                return win 
            
            empty_cells_counter += triple.get_empty_cells()

        if empty_cells_counter == 0:
            return 'draw'
        else:
            return 'play'
