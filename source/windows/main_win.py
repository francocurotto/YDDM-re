import urwid
from title_win import TitleWin

class MainWin(urwid.Frame):
    """
    Main window that displays the entirety of the game.
    """
    def __init__(self):
        # create game window, that starts at title
        game_win = TitleWin()

        # create main window as a frame
        super().__init__(game_win)

    def keypress(self, size, key):
        """
        Handles ctrl-c and ctrl-z as exit program.
        """
        return super().keypress(size, key)
