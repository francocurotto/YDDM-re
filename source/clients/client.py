from engine import Engine
from stringifier import Stringifier

class Client():
    """
    Generic client.
    """
    def __init__(self, args):
        self.engine = Engine(args.library, args.name1, 
            args.poolfile1, args.name2, args.poolfile2)
        self.stringifier = Stringifier(args.icontype)

    def run(self):
        """
        Run game.
        """
        while True:
            self.currplayer.init_turn()
            cmd = self.currplayer.get_command()
            reply = self.engine.update(cmd)
            self.currplayer.process_reply(reply)
            if "PLAYERSWITCH" in reply["flags"]:
                self.switch_player()

    def init_players(self):
        """
        Initialize players.
        """
        player1 = self.init_player(1)
        player2 = self.init_player(2)
        self.players = [player1, player2]
        self.currplayer = self.players[0] # current player

    def switch_player(self):
        """
        Switch current player.
        """
        index = not self.players.index(self.currplayer)
        self.currplayer = self.players[index]
