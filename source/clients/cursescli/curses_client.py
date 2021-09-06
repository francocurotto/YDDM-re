from client import Client
from cursescli.curses_view import CursesView
from cursescli.curses_controller import CursesController

class CursesClient(Client):
    """
    Curses interface client.
    """
    def __init__(self, args):
        super().__init__(args)
        self.view = CursesView(self.engine, self.stringifier)
        self.ctrl = CursesController(self.view, self.engine,
            self.stringifier)
        self.init_players()
