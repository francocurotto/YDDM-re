import yaml
from dice.dice import Dice
from player.dice_pool import DicePool
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
        pool1 = DicePool(poolfile1, self.library)
        pool2 = DicePool(poolfile1, self.library)
        # players
        player1 = Player(pool1)
        player2 = Player(pool2)
        
        # duel
        self.duel = Duel(player1, player2)

        # duel state machine
        self.dsm = DuelStateMachine(self.duel)

    def update(self, cmd):
        """
        Update duel and duel state machine given external 
        command cmd.
        """
        return self.dsm.update(cmd)

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
