from engine import Engine

class CliClient():
    """
    Command line interface client.
    """
    def __init__(self, args):
        self.engine = Engine(args.library, args.poolfile1,
            args.poolfile2)
        player1 = HumanPlayer(args.player1)
        player2 = HumanPlayer(args.player2)
        self.players = [player1, player2]
        self.currplayer = self.players[0] # current player
        
    def run(self):
        """
        Run game.
        """
        while True:
            cmd = self.currplayer.get_command(self.engine)
            reply = self.engine.update(cmd)
            if reply["newturn"]:
                self.currplayer = self.get_next_player()

    def get_next_player(self):
        """
        Get the player that is not the current player.
        """
        index = not self.players.index(self.currplayer)
        return self.players[index]

