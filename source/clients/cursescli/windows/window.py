import curses
from cursescli.windows.ansi_translator import ANSITranslator

class Window():
    """
    Generic window for the curses interface.
    """
    def __init__(self, parwin, dy, dx, y, x):
        self.win = parwin.derwin(dy, dx, y, x)
        self.translator = ANSITranslator()

    def addstr(self, string):
        """
        Add string to window at position (0,0) and add colors
        by translating ANSI escape characters.
        Then update the screen.
        """
        ctuplelist = self.translator.get_ctuples(string)
        for ctuple in ctuplelist:
            self.win.addstr(ctuple[0], ctuple[1])
        self.win.noutrefresh()

    def update(self):
        """
        Update window content.
        """
        self.win.clear()
