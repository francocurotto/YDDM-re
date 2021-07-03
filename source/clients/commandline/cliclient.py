import yaml
from engine import Engine
from human_player import HumanPlayer

class CliClient():
    """
    Command line interface client.
    """
    def __init__(self, args):
        self.engine = Engine(args.library, args.poolfile1,
            args.poolfile2)
        
        # icon items
        allicons = yaml.full_load(open("ICONS.yaml"))
        icons = allicons[args.icontype]
        
        # players 
        player1 = HumanPlayer(args.player1, icons)
        player2 = HumanPlayer(args.player2, icons)
        self.players = [player1, player2]
        self.currplayer = self.players[0] # current player
        
    def run(self):
        """
        Run game.
        """
        while True:
            print(self.get_header())
            cmd = self.currplayer.get_command(self.engine)

            # if commmand is generated, update engine
            if cmd:
                reply = self.engine.update(cmd)

                # if new turn, update current player
                if reply["newturn"]:
                    self.currplayer = self.get_next_player()

            # end command newline
            print("")

    def get_header(self):
        """
        Create string of information after every command.
        """
        string  = "<"
        string += self.currplayer.name
        string += "[p"
        string += str(self.engine.dsm.state.player.id)
        string += "] | state:"
        string += self.engine.dsm.state.name
        string += " | turn:"
        string += str(self.engine.dsm.turn)
        string += "> (l:list command)"
        return string

    def get_next_player(self):
        """
        Get the player that is not the current player.
        """
        index = not self.players.index(self.currplayer)
        return self.players[index]
