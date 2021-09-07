from curses.textpad import Textbox
from cursescli.windows.window import Window

class InputWin(Window):
    """
    Window for user input.
    """
    def __init__(self, parwin, y ,x):
        super().__init__(parwin, 1, 21, y, x)

        # draw >> symbol
        self.win.addstr(0, 0, ">> ")
        self.win.noutrefresh()

        # add textbox
        self.boxwin = self.win.derwin(1, 18, 0, 3)
        self.textbox = Textbox(self.boxwin)

    def get_input(self):
        """
        Get text input from textbox.
        """
        self.textbox.edit()
        string = self.textbox.gather()
        self.boxwin.clear()
        self.boxwin.move(0,0)
        return string
