import curses

class Window():
    """
    Generic window for the curses interface.
    """
    def __init__(self, parwin, dy, dx, y, x):
        self.win = parwin.derwin(dy, dx, y, x)

    def addstr(self, string):
        """
        Add string to window at position (0,0). It wraps
        curses addstr into a try/except statement to avoid 
        stupid curses error when addinga char at lower right 
        corner of window. 
        """
        try:
            self.win.addstr(string)
        except curses.error:
            pass
