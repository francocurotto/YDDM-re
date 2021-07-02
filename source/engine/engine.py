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
        try:
            return self.dsm.update(cmd)
        except:
            return self.get_default_reply()

    def get_default_reply():
        """
        Returns the default reply when an exception is found
        while updating the engine.
        """
        reply = {
            "valid"   : False,
            "newturn" : False,
            "endduel" : False,
            "message" : "Exception at state: " + \
                dsm.state.name + "\n" + "Command:\n" + \
                str(cmd)}
        return reply

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
