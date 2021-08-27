from client import Client

class CliClient(Client):
    """
    Command line client.
    """
    def __init__(self, args):
        super().__init__(args)
        self.view = CliView()
        self.ctrl = CliController(self.view)

    def init_player(self):
        """
        Initialize player.
        """
        return HumanPlayer(1, self.engine, self.ctrl)
