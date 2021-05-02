import urwid
from title_win import TitleWin
from pool_builder_win import PoolBuilderWin
from options_win import OptionsWin

class MainWin(urwid.WidgetWrap):
    """
    Main window that displays the entirety of the game.
    """
    def __init__(self):
        # create game window, that starts at title
        self.title_win = TitleWin()

        # create main window as a frame
        #super().__init__(self.title_win, valign="top")
        super().__init__(self.title_win)

    def switch_title(self):
        """
        Switch window to title.
        """
        self._w = self.title_win

    def switch_pool_builder(self):
        """
        Swtich window to pool builder.
        """
        self._w = PoolBuilderWin()

    def switch_options(self):
        """
        Swtich window to options.
        """
        self._w = OptionsWin()
