import yaml
from globvars import library_path
from dice import Dice

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
    dice_list = [library[id] for id in dice_ids]
    return dice_list
