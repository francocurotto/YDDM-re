import yaml
from copy import deepcopy

class DicePool():
    """
    The pool of dice of a player.
    """
    def __init__(self, poolfile, library):
        self.contents = create_contents(poolfile, library)

    def get_dice(self, i):
        """
        Get dice at index i. If index is invalid return None.
        """
        try:
            return self.contents[i]
        except IndexError:
            return None

def create_contents(poolfile, library):
    dice_ids = yaml.full_load(open(poolfile))
    return [deepcopy(library[id]) for id in dice_ids]
        
        
