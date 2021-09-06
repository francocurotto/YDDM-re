from curses.textpad import Textbox
from cursescli.windows.window import Window

class InputWin(Window):
    """
    Window for user input.
    """
    def __init__(self, parwin, y ,x):
        super().__init__(parwin, 1, 16, y, x)

        # draw >> symbol
        self.win.addstr(0, 0, ">> ")
        self.win.noutrefresh()

        # add textbox
        (y, x) = self.win.getmaxyx()
        self.inputwin = self.win.derwin(1, 13, 0, 3)
        self.inputbox = Textbox(self.inputwin)
