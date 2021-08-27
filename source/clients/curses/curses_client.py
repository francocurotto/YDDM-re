import curses
from stringifier import Stringifier
from engine import Engine
from replier import Replier

class CursesClient():
    """
    Curses interface client.
    """
    def __init__(self, args):
        # initialize screen
        self.stdscr = init_screen()
        
        # engine
        self.engine = Engine(args.library, args.name1, 
            args.poolfile1, args.name2, args.poolfile2)

        # stringifier
        stringifier = Stringifier(args.icontype)

        # players 
        player1 = HumanPlayer(self.engine, 1, stringifier)
        player2 = HumanPlayer(self.engine, 2, stringifier)
        self.players = [player1, player2]
        self.currplayer = self.players[0] # current player

        # replier
        self.replier = Replier(self.engine, stringifier)

        # 

    def run(self):
        """
        Run game.
        """
        while True:
            

    def terminate(self):
        """
        Terminate the IO.
        """
        #self.stdscr.getkey()
        curses.echo()
        curses.endwin()

def init_screen():
    """
    Initialize curses screen.
    """
    stdscr = curses.initscr()
    curses.noecho()
    curses.start_color()
    return stdscr
