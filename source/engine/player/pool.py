import yaml
from copy import deepcopy

class Pool():
    """
    The pool of dice of a player.
    """
    def __init__(self, poolfile, library):
        self.contents = create_contents(poolfile, library)

def create_contents(poolfile, library):
    dice_ids = yaml.full_load(open(poolfile))
    return [deepcopy(library[id]) for id in dice_ids]
        
        
