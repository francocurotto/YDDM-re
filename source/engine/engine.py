import yaml
from copy import deepcopy
from dice.dice import Dice
from player.player import Player
from duel.duel import Duel
from duel.dsm import DuelStateMachine
# constants
from dungeon.dicenets.netdict import netdict
from dungeon.dicenets.dicenet import trans

class Engine():
    """
    Creates and controls a duel.
    """
    # constants
    POOLSIZE = 15
    NETS     = netdict.keys()
    TRANS    = trans

    def __init__(self, libraryfile, poolfile1, poolfile2):
        self.library = create_library(libraryfile)
        # pools
        pool1 = create_dicepool(poolfile1, self.library)
        pool2 = create_dicepool(poolfile1, self.library)
        # players
        player1 = Player(1, pool1)
        player2 = Player(2, pool2)
        
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

def create_dicepool(poolfile, library):
    dice_ids = yaml.full_load(open(poolfile))
    return [deepcopy(library[id]) for id in dice_ids]
