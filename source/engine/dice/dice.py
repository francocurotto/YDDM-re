import random
from dice.cards.monster_card import MonsterCard
from dice.cards.item_card import ItemCard
from dice.crests.side import Side, crest_dict

class Dice():
    """
    The dice players use to play the game.
    """
    def __init__(self, diceid, dicedict):
        self.id = diceid
        self.level = dicedict["LEVEL"]
        self.card = create_card(dicedict)
        self.sides = create_sides(dicedict["CRESTS"], 
            self.level)

    def roll(self):
        """
        Simulates a dice roll by selecting a random element
        from the dice sides list.
        """
        return random.choice(self.sides)

def create_card(card_info):
    """
    Create the appropiate card from the card_info dictionary.
    """
    if card_info["TYPE"] in monster_types:
        return MonsterCard(card_info)
    elif card_info["TYPE"] == "ITEM":
        return ItemCard(card_info)

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
        if char in crest_chars:
            side_strings.append(char)
            if char == "S": # add level as multiplier
                side_strings[-1] += str(level)
        else: # expected to be a digit
            side_strings[-1] += char

    # then convert the side strings into side objects
    side_list = []
    for side_string in side_strings:
        side_list.append(Side(side_string))

    return side_list

monster_types = ["DRAGON", 
                 "SPELLCASTER", 
                 "UNDEAD", 
                 "BEAST",
                 "WARRIOR"]
