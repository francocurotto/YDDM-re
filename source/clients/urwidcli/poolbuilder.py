import urwid
from engine import create_library, create_dicepool
from stringifier import Stringifier
from urwidcli.dice_widgets.library import Library

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
        #self.library = Library(library, stringifier)
        #self.pool = Pool(pool, stringifier)
        #self.diceinfo = DiceInfo(sringifier)
        # create container widgets
        self.columns = urwid.Columns([(78,self.library)])
        #self.columns = urwid.Columns([(66,self.library)])
        super().__init__(self.columns)
