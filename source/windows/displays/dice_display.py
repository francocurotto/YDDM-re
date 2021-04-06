import urwid
from icon_functions import load_icons

class DiceDisplay(urwid.AttrMap):
    """
    Displays dice information in a single line.
    """
    def __init__(self, dice):
        col_widgets = create_widget_list(dice)
        columns = urwid.Columns(col_widgets, dividechars=1)
        super().__init__(columns, None)

def create_widget_list(dice):
    """
    Create all the widgets for that display column.
    """
    icons = load_icons()
    card = dice.card # for less typing
    
    # initialize list
    widget_list = []

    # name widget
    widget_list.append(urwid.Text(card.name, wrap="clip"))

    # string for the next widget
    string = icons["TYPE_"+card.type]+str(card.level) + " "

    # monster specific string part
    if dice.card.is_monster():
        # attack part
        string += str(card.attack).rjust(2)
        string += icons["CREST_ATTACK"] + " "
        # defense widget
        string += str(card.defense).rjust(2)
        string += icons["CREST_DEFENSE"] + " "
        # life widget
        string += str(card.life).rjust(2)
        string += icons["MONSTER_HEART"]
    
    # in case of item add a blank section for alignment
    elif dice.card.is_item():
        string += " "*11

    # dice widget
    dice_str_list = []
    for side in dice.sides:
        dice_str  = icons["CREST_"+side.crest.type]
        dice_str += str(side.multiplier)
        dice_str_list.append(dice_str)
    string += " " + ",".join(dice_str_list)

    widget_list.append(("pack",urwid.Text(string)))

    return widget_list
