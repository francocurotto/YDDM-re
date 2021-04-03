import yaml

class DiceList():
    """
    A generic list of dice.
    """
    def __init__(self, filename):
        self.contents = []
        dice_dict_list = yaml.full_load(open(filename))
        for dice_dict in dice_dict_list:
            dice = Dice(dice_dict)
            self.contents.append(dice)
            
