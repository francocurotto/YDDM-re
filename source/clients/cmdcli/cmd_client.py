from client import Client
from cmdcli.cmd_view import CmdView
from cmdcli.cmd_controller import CmdController

class CmdClient(Client):
    """
    Command line client.
    """
    def __init__(self, args):
        super().__init__(args)
        self.view = CmdView(self.engine, self.stringifier)
        self.ctrl = CmdController(self.view, self.engine, 
            self.stringifier)
        self.init_players()
