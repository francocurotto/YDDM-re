import yaml
from dice.dice import Dice
from player.pool import Pool
from player.player import Player
from duel.duel import Duel
from duel.dsm import DuelStateMachine

class Engine():
    """
    Creates and controls a duel.
    """
    def __init__(self, libraryfile, poolfile1, poolfile2):
        self.library = create_library(libraryfile)
        # pools
        pool1 = Pool(poolfile1, self.library)
        pool2 = Pool(poolfile1, self.library)
        # players
        player1 = Player(pool1)
        player2 = Player(pool2)
        
        # duel
        self.duel = Duel(player1, player2)

        # duel state machine
        self.dsm = DuelStateMachine(self.duel)

def create_library(libraryfile):
    """
    Create the dice library dict by reading the libraryfile
    yaml file.
    """
    yamldict = yaml.full_load(open(libraryfile))
    library = {}
    for key, item in yamldict.items():
        library[key] = Dice(key, item)
    return library
