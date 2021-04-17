import os, yaml
from copy import deepcopy
from globvars import library_path
from globvars import starter_pool_path
from globvars import saved_pool_path
from dice import Dice
from pool import Pool

def create_dice_library():
    """
    Create a dictionary with all the dice from the game.
    """
    library = {}
    yaml_library = yaml.full_load(open(library_path))
    for key, item in yaml_library.items():
        library[key] = Dice(key, item)
    return library

def create_dice_list(filename):
    """
    Create dice list from IDs from a file.
    """
    from globvars import library
    dice_ids = yaml.full_load(open(filename))
    dice_list = []
    dice_list = [deepcopy(library[id]) for id in dice_ids]
    return dice_list

def create_player_pool():
    """
    Create player pool by looking at the pool.yaml file at
    the dicesets/pools/player folder. If yaml does not 
    exists, create pool from defaul starter.yaml file.
    """
    if os.path.isfile(saved_pool_path):
        return Pool(create_dice_list(saved_pool_path))
    else:
        return Pool(create_dice_list(starter_pool_path))
