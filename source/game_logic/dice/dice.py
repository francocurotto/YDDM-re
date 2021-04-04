from globvars import monster_types

class Dice():
    """
    The dice players use to play the game.
    """
    def __init__(self, dice_dict):
        self.level = dice_dict["LEVEL"]
        self.card = create_card(dice_dict)
        self.sides = create_sides(dice_dict["CRESTS"], 
            self.level)

def create_card(card_info):
    """
    Create the appropiate card from the card_info dictionary.
    """
    if card_info["TYPE"] in monster_types:
        return MonsterCard(card_info)
    elif card_info["TYPE"] == "ITEM":
        return ItemCard(card_info)

from side import crest_dict
def create_sides(string, level):
    """
    Create a list of dice sides given a string of crests as 
    used in the dice library file.
    """
    # get crest characters from crest dict
    crest_chars = list(crest_dict.keys())

    # first  break the string into  a list of side strings
    side_strings = []
    for char in string:
        if char is in crest_chars:
            side_strings.append(char)
            if char == "S": # add level as multiplier
                side_string[-1] += str(level)
        else: # expected to be a digit
            side_string[-1] += char

    # then convert the side strings into side objects
    side_list = []
    for side_string in side_strings:
        side_list.append(Side(side_string))

    return side_list
