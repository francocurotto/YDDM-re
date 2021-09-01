from client import Client
from human_player import HumanPlayer
from commandline.cli_view import CliView
from commandline.cli_controller import CliController

class CliClient(Client):
    """
    Command line client.
    """
    def __init__(self, args):
        super().__init__(args)
        self.view = CliView(self.engine, self.stringifier)
        self.ctrl = CliController(self.view, 
            self.engine, self.stringifier)
        self.init_players()

    def init_player(self, playerid):
        """
        Initialize player.
        """
        return HumanPlayer(playerid, self.engine, self.ctrl)
