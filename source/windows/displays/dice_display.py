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

    # type widget
    string = icons["TYPE_"+card.type]+str(card.level)
    widget_list.append(("pack",urwid.Text(string)))

    # monster specific widgets
    # TODO: fix alignment for attack=0
    if dice.card.is_monster():
        # attack widget
        string = str(card.attack)+icons["CREST_ATTACK"]
        widget_list.append(("pack",urwid.Text(string)))
        # defense widget
        string = str(card.defense)+icons["CREST_DEFENSE"]
        widget_list.append(("pack",urwid.Text(string)))
        # life widget
        string = str(card.life)+icons["MONSTER_HEART"]
        widget_list.append(("pack",urwid.Text(string)))

    # dice widget
    str_list = []
    for side in dice.sides:
        string  = icons["CREST_"+side.crest.type]
        string += str(side.multiplier)
        str_list.append(string)
    string = ",".join(str_list)
    widget_list.append(("pack",urwid.Text(string)))

    return widget_list
