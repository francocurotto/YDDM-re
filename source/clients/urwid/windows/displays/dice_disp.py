import urwid
from icon_functions import load_icons

class DiceDisp(urwid.AttrMap):
    """
    Displays dice information in a single line.
    """
    def __init__(self, dice, disp_id=False):
        self.dice = dice
        col_widgets = create_widget_list(self.dice, disp_id)
        columns = urwid.Columns(col_widgets, dividechars=1)
        super().__init__(columns, None, focus_map="focused")

def create_widget_list(dice, disp_id):
    """
    Create all the widgets for that display column. If 
    disp_id is true, add ID to widgets.
    """
    icons = load_icons()
    card = dice.card # for less typing
    
    # initialize list
    widget_list = []

    # id widget
    if disp_id:
        dice_id = str(dice.id).zfill(3)
        widget_list.append(("pack",urwid.Text(dice_id)))

    # name widget
    widget_list.append(DiceName(card.name, wrap="clip"))

    # type widget
    string = icons["TYPE_"+card.type]+str(card.level)
    widget_list.append(("pack",urwid.Text(string)))

    # monster specific widget
    if dice.card.is_monster():
        # attack widget
        string  = str(card.attack).rjust(2)
        string += icons["CREST_ATTACK"]
        widget_list.append(("pack",urwid.Text(string)))
        # defense widget
        string  = str(card.defense).rjust(2)
        string += icons["CREST_DEFENSE"]
        widget_list.append(("pack",urwid.Text(string)))
        # life widget
        string  = str(card.life).rjust(2)
        string += icons["MONSTER_HEART"]
        widget_list.append(("pack",urwid.Text(string)))
    
    # in case of item add a blank section for alignment
    elif dice.card.is_item():
        dummy_str = "AA" + icons["CREST_ATTACK"] + " " + \
                    "DD" + icons["CREST_DEFENSE"] + " " + \
                    "LL" + icons["MONSTER_HEART"]
        dummy_text = urwid.Text(dummy_str)
        width = dummy_text.pack()[0]
        string = width*" "
        widget_list.append(("pack",urwid.Text(string)))
            
    # dice widget
    dice_str_list = []
    for side in dice.sides:
        dice_str  = icons["CREST_"+side.crest.type]
        dice_str += str(side.multiplier)
        dice_str_list.append(dice_str)
    string = ",".join(dice_str_list)
    widget_list.append(("pack",urwid.Text(string)))

    return widget_list

class DiceName(urwid.Text):
    """
    Makes dice name selectable for proper scrolling in dice 
    list.
    """
    _selectable = True
    def keypress(self, size, key):
        return key
