import urwid
from engine import create_library, create_dicepool
from stringifier import Stringifier
from urwidcli.dice_widgets.library import Library
from urwidcli.dice_widgets.pool import Pool
from urwidcli.dice_widgets.diceinfo import DiceInfo
from urwidcli.dice_widgets.dice import Dice

class PoolBuilder(urwid.Frame):
    """
    Main class of the pool builder implemented in urwid.
    """
    def __init__(self, args):
        # create dice lists
        library = create_library(args.library)
        pool = create_dicepool(args.pool, library)

        # create stringifier
        stringifier = Stringifier(args.icontype)
        
        # create main widgets
        self.library = urwid.LineBox(
            Library(library, stringifier), "Library", "left")
        self.pool = urwid.LineBox(
            Pool(pool, stringifier), "Dice Pool", "left")
        self.diceinfo = urwid.LineBox(urwid.Filler(
            DiceInfo(library[1], stringifier), "top"), 
            "Dice Info", "left")
        
        # create container widgets
        self.rightcol = urwid.Pile([(17,self.pool), 
            self.diceinfo])
        self.columns = urwid.Columns([self.library, 
            self.rightcol])
        super().__init__(self.columns)

    def keypress(self, size, key):
        super().keypress(size, key)
        self.update_diceinfo()

    def mouse_event(self, size, event, button, col, row, 
        focus):
        super().mouse_event(size, event, button, col, row,
            focus)
        self.update_diceinfo()

    def update_diceinfo(self):
        """
        Update dice info widget with current dice in focus.
        """
        dice = self.get_focused_dice()
        self.diceinfo.base_widget.update(dice)

    def get_focused_dice(self):
        """
        Get the dice that is currently selected, either in
        library or in pool.
        """
        for widget in self.get_focus_widgets():
            if isinstance(widget, Dice):
                return widget.dice
