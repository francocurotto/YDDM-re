import curses
from cmdcli.text_view import TextView
from cursescli.windows.inputwin    import InputWin
from cursescli.windows.headerwin   import HeaderWin
from cursescli.windows.poolwin     import PoolWin
from cursescli.windows.playerwin   import PlayerWin
from cursescli.windows.opponentwin import OpponentWin
from cursescli.windows.dungeonwin import DungeonWin

class CursesView(TextView):
    """
    Display for curses interface.
    """
    def __init__(self, engine, stringifier):
        super().__init__(engine, stringifier)
        self.stdscr = init_screen()
        (y, x) = self.stdscr.getmaxyx()

        # create view elements
        self.poolwin  = PoolWin(self.stdscr, 1, 0)
        self.dungeonwin = DungeonWin(self.stdscr, 1, 65)
        self.playerwin = PlayerWin(self.stdscr, 1, 102)
        self.opponentwin = OpponentWin(self.stdscr, 5, 102)
        self.headerwin = HeaderWin(self.stdscr, 18, 0)
        self.inputwin = InputWin(self.stdscr, 19, 0)
        self.windows = [self.poolwin, self.dungeonwin, 
            self.playerwin, self.opponentwin, self.headerwin,
            self.inputwin]

        # inital display
        self.update_windows()

    def update(self, reply):
        """
        Update view.
        """
        # update output window with reply
        self.show_reply(reply)
        # update all windows
        self.update_windows()

    def update_windows(self):
        """
        Updates the view windows.
        """
        for window in self.windows:
            window.update(self.engine, self.stringifier)

    def print_string(self, string, end="\n\n"):
        """
        Print a generic string.
        """
        pass

    def exit_game(self):
        """
        Finish game script. First must close curses window
        properly.
        """
        curses.echo()
        curses.endwin()
        super().exit_game()

def init_screen():
    """
    Initialize curses sceen.
    """
    stdscr = curses.initscr()
    curses.noecho()
    curses.start_color()
    return stdscr
