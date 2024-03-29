import yaml, copy
from dice.dice import Dice
from player.player import Player
from duel.duel import Duel
from duel.dsm import DuelStateMachine

class Engine():
    """
    Creates and controls a duel.
    """
    def __init__(self, libraryfile, name1, poolfile1, name2,
        poolfile2, dungeon):
        self.library = create_library(libraryfile)
        # pools
        pool1 = create_dicepool(poolfile1, self.library)
        pool2 = create_dicepool(poolfile2, self.library)
        # players
        player1 = Player(1, name1, pool1, dungeon)
        player2 = Player(2, name2, pool2, dungeon)
        
        # duel
        self.duel = Duel(player1, player2, dungeon)

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
    return [copy.deepcopy(library[id]) for id in dice_ids]
