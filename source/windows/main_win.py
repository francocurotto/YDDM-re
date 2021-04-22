import urwid
from title_win import TitleWin
from pool_builder_win import PoolBuilderWin
from options_win import OptionsWin

class MainWin(urwid.Frame):
    """
    Main window that displays the entirety of the game.
    """
    def __init__(self):
        # create game window, that starts at title
        #game_win = TitleWin()
        self.title_win = TitleWin()

        # create main window as a frame
        #super().__init__(game_win)
        super().__init__(self.title_win)

    def switch_title(self):
        """
        Switch window to title.
        """
        #self.contents["body"] = (TitleWin(), None)
        self.contents["body"] = (self.title_win, None)

    def switch_pool_builder(self):
        """
        Swtich window to pool builder.
        """
        self.contents["body"] = (PoolBuilderWin(), None)

    def switch_options(self):
        """
        Swtich window to options.
        """
        self.contents["body"] = (OptionsWin(), None)
