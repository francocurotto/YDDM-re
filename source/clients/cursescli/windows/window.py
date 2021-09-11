import curses
from cursescli.windows.ansi_translator import ANSITranslator

class Window():
    """
    Generic window for the curses interface.
    """
    def __init__(self, parwin, dy, dx, y, x):
        self.win = create_derwin(parwin, dy, dx, y, x)
        self.translator = ANSITranslator()

    def addstr(self, string):
        """
        Add string to window at position (0,0) and add colors
        by translating ANSI escape characters.
        Wrap addstr into try/except to avoid stupid curses
        error while writing at the bottom right corner.
        At the end, update the screen.
        """
        strlist = string.split("\n")
        for i, line in enumerate(strlist):
            # move cursor to the start of the line
            self.win.move(i,0)
            ctuplelist = self.translator.get_ctuples(line)
            for ctuple in ctuplelist:
                # avoid stupid curses error
                try:
                    self.win.addstr(ctuple[0], ctuple[1])
                except curses.error:
                    pass
        self.win.noutrefresh()

    def update(self):
        """
        Update window content.
        """
        self.win.clear()

def create_derwin(parwin, dy, dx, y, x):
    """
    Creates a subwindow from parent window. If curses error
    (due to screen being too small), print message and exit.
    """
    try:
        return parwin.derwin(dy, dx, y, x)
    except curses.error:
        print("Curses error. Probably window is too small " +
            "to run the game. Try Maximizing the window, " +
            "or reducing the terminal font size.")
        curses.echo()
        curses.endwin()
        exit()

