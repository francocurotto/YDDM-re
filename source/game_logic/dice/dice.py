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
    card_type = card_info["TYPE"]
    return card_dict[card_type](card_info)

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

from dragon_card import DragonCard
from spellcaster_card import SpellcasterCard
from undead_card import UndeadCard
from beast_card import BeastCard
from warrior_card import WarriorCard
from item_card import ItemCard
card_dict = {
    "DRAGON"      : DragonCard,
    "SPELLCASTER" : SpellcasterCard,
    "UNDEAD"      : UndeadCard,
    "BEAST"       : BeastCard,
    "WARRIOR"     : WarriorCard,
    "ITEM"        : ItemCard}

