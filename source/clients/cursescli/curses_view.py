import curses
from cmdcli.text_view import TextView
from cursescli.windows.inputwin import InputWin

class CursesView(TextView):
    """
    Display for curses interface.
    """
    def __init__(self, engine, stringifier):
        super().__init__(engine, stringifier)
        self.stdscr = init_screen()

        # create view elements
        self.inputwin = InputWin(self.stdscr, 20, 0)

    def print_string(self, string, end="\n\n"):
        """
        Print a generic string.
        """
        pass

def init_screen():
    """
    Initialize curses sceen.
    """
    stdscr = curses.initscr()
    curses.noecho()
    curses.start_color()
    return stdscr
