import urwid
from engine import create_library, create_dicepool
from stringifier import Stringifier
from urwidcli.dice_widgets.library import Library
from urwidcli.dice_widgets.pool import Pool
from urwidcli.dice_widgets.diceinfo import DiceInfo
from urwidcli.dice_widgets.dice import Dice

class BuilderWidget(urwid.Frame):
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
        self.library = Library(library, stringifier)
        self.boxlibrary = urwid.LineBox(self.library , 
            "Library", "left")
        self.pool = Pool(pool, stringifier)
        self.boxpool = urwid.LineBox(self.pool, "Dice Pool",
            "left")
        self.diceinfo = DiceInfo(library[1], stringifier)
        self.boxdiceinfo = urwid.LineBox(urwid.Filler(
            self.diceinfo, "top"), "Dice Info", "left")
        
        # create container widgets
        self.rightcol = urwid.Pile([(17,self.boxpool), 
            self.boxdiceinfo])
        self.columns = urwid.Columns([self.boxlibrary, 
            self.rightcol])

        # create footer widget
        self.footer = urwid.Text(
            "↑,↓:Select dice | ←,→:Change list | " +
            "SPACE:Remove,add dice | q:quit")

        super().__init__(self.columns, footer=self.footer)

    def keypress(self, size, key):
        # handle space (dice movement)
        if key == " ":
            if self.boxlibrary in self.get_focus_widgets():
                self.add_dice_to_pool()
            if self.boxpool in self.get_focus_widgets():
                self.remove_dice_from_pool()

        super().keypress(size, key)
        self.update_diceinfo(size)

    def mouse_event(self, size, event, button, col, row, 
        focus):
        if button == 4: # button 4 = scroll up
            self.keypress(size, "up")
        if button == 5: # button 4 = scroll down
            self.keypress(size, "down")
        super().mouse_event(size, event, button, col, row,
            focus)
        self.update_diceinfo(size)

    def update_diceinfo(self, size):
        """
        Update dice info widget with current dice in focus.
        """
        dicewid = self.get_focused_dicewid()
        # if no dicewid is focused, move focus to library
        if not dicewid:
            super().keypress(size, "left")
            dicewid = self.get_focused_dicewid()
        self.diceinfo.update(dicewid.dice)

    def get_focused_dicewid(self):
        """
        Get the dice that is currently selected, either in
        library or in pool.
        """
        for widget in self.get_focus_widgets():
            if isinstance(widget, Dice):
                return widget
        # if not dice widget found, return None
        return None

    def add_dice_to_pool(self):
        """
        Add dice focused in library to pool.
        """
        dicewid = self.get_focused_dicewid()
        self.pool.add_dice(dicewid.dice)

    def remove_dice_from_pool(self):
        """
        Remove dice focused in pool.
        """
        dicewid = self.get_focused_dicewid()
        self.pool.remove_dice(dicewid)
