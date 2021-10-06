import urwid
from engine import create_library, create_dicepool
from stringifier import Stringifier
from urwidcli.dice_widgets.library import Library

class PoolBuilder(urwid.Columns):
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
        #self.pool = Pool(pool, stringifier)
        #self.diceinfo = DiceInfo(sringifier)
        super().__init__([self.library])
