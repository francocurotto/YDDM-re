import yaml
from dice import Dice

class Engine():
    """
    Creates and controls a duel.
    """
    def __init__(self, poolfile1, poolfile2):
        self.library = create_library()
        # pools
        pool1 = Pool(poolfile1, self.library)
        pool2 = Pool(poolfile1, self.library)
        # players
        player1 = Player(pool1)
        player2 = Player(pool2)
        
        self.duel = Duel(player1, player2)

def create_library():
    """
    Create the dice library dict by reading LIBRARY.yaml.
    """
    yamldict = yaml.full_load(open(library_path))
    library = {}
    for key, item in yamldict.items():
        library[key] = Dice(key, item)
    return library
