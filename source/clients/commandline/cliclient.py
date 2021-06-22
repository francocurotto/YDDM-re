from engine import Engine

class CliClient():
    """
    Command line interface client.
    """
    def __init__(self, args):
        self.engine = Engine(args.library, args.poolfile1,
            args.poolfile2)
        
    def run(self):
        """
        Run game.
        """
        pass

