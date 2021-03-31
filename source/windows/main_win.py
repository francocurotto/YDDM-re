import urwid
from title_win import TitleWin
from pool_builder_win import PoolBuilderWin

class MainWin(urwid.Frame):
    """
    Main window that displays the entirety of the game.
    """
    def __init__(self):
        # create game window, that starts at title
        game_win = TitleWin()

        # create main window as a frame
        super().__init__(game_win)

    def switch_pool_builder(self):
        """
        Swtich window to pool builder.
        """
        self.contents["body"] = (PoolBuilderWin(), None)
