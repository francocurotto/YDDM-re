from cmdcli.generators.generator import Generator
from cmdcli.generators.generator import infodict, descdict
from cmdcli.generators.sanitize_functs import *

class PrintGenerator(Generator):
    """
    Generator for print command.
    """
    def __init__(self, engine, stringifier):
        self.key = "p"
        self.engine = engine
        self.stringifier = stringifier
        self.descdict = descdict
        super().__init__()

    def get_string(self, split):
        """
        Get the desired info string.
        """
        # get basic help
        if not split:
            return self.get_help()
        # get command list
        elif split[0]=="cmd" and len(split)==1:
            return self.get_cmd_list()
        # get command description
        elif split[0]=="cmd" and len(split)==2:
            return self.get_cmd_desc(split[1])
        # get dice pool
        elif split[0]=="p" and len(split)==1:
            return self.get_pool()
        # get dice
        elif split[0]=="p" and len(split)==2:
            return self.get_dice(split[1])
        # get opponent dice pool
        elif split[0]=="op" and len(split)==1:
            return self.get_opponent_pool()
        # get opponent dice
        elif split[0]=="op" and len(split)==2:
            return self.get_opponent_dice(split[1])
        # get dungeon
        elif split[0]=="d" and len(split)==1:
            return self.get_dungeon()
        # get dungeon object
        elif split[0]=="d" and len(split)==2:
            return self.get_dungobj(split[1])
        # get crest pool
        elif split[0]=="c" and len(split)==1:
            return self.get_crestpool()
        # get opponent crest pool
        elif split[0]=="oc" and len(split)==1:
            return self.get_opponent_crestpool()
        # get summon candidates
        elif split[0]=="s" and len(split)==1:
            return self.get_summons()
        # get nets
        elif split[0]=="n" and len(split)==1:
            return self.get_nets()
        # get trans
        elif split[0]=="t" and len(split)==1:
            return self.get_trans()
        else:
            return "Invalid print command"

    def get_help(self):
        """
        Get basic help.
        """
        return self.descdict["p"]

    def get_cmd_list(self):
        """
        Get command list.
        """
        return "\n".join(infodict.values())
    
    def get_cmd_desc(self, cmd):
        """
        Get command cmd description.
        """
        try:
            return self.descdict[cmd]
        except KeyError: 
            return "Unknown command"

    def get_pool(self):
        """
        get player pool.
        """
        player = self.engine.dsm.state.player
        return self.stringifier.stringify_dicepool(player)

    def get_dice(self, string):
        """
        get player dice at index string in dice pool.
        """
        # convert string to index
        i = str2index(string, 0, 14)
        dice = self.engine.dsm.state.player.dicepool[i]
        return self.stringifier.stringify_dice(dice)

    def get_opponent_pool(self):
        """
        get opponent pool.
        """
        # check if duel had ended
        if self.engine.dsm.state.name != "ENDDUEL":
            return "Can only see opponent's pool at the " + \
            "end of duel"
        opponent = self.engine.dsm.state.opponent
        return self.stringifier.stringify_dicepool(opponent)

    def get_opponent_dice(self, string):
        """
        get opponent dice at index string in dice pool.
        """
        # check if duel had ended
        if self.engine.dsm.state.name != "ENDDUEL":
            return "Can only see opponent's pool at the " + \
            "end of duel"
            return
        i = str2index(string, 0, 14)
        dice = self.engine.dsm.state.opponent.dicepool[i]
        return self.stringifier.stringify_dicepool(opponent)

    def get_dungeon(self):
        """
        get dungeon.
        """
        duel = self.engine.duel
        return self.stringifier.stringify_dungeon(duel)

    def get_dungobj(self, string):
        """
        get object in dungeon at position string.
        """
        coor = str2coor(string)
        y = coor[0]; x = coor[1]
        tile = self.engine.duel.dungeon.array[y][x]
        # reachable = no content
        if not tile.is_dungeon() or tile.is_reachable():
            return "Nothing to print there"
        duel = self.engine.duel
        cont = tile.content
        return self.stringifier.stringify_dungobj(duel, cont)

    def get_crestpool(self):
        """
        get player crestpool.
        """
        cpool = self.engine.dsm.state.player.crestpool
        return self.stringifier.stringify_crestpool(cpool)

    def get_opponent_crestpool(self):
        """
        get opponent crestpool.
        """
        cpool = self.engine.dsm.state.opponent.crestpool
        return self.stringifier.stringify_crestpool(cpool)

    def get_summons(self):
        """
        get player's summoning options after roll.
        """
        # check for correct state
        if self.engine.dsm.state.name != "DIM":
            return "Can print summons in DIM state only"
        dimdice = self.engine.dsm.state.dimdice
        return self.stringifier.stringify_dicelist(dimdice)

    def get_nets(self):
        """
        get all possible nets for dimension.
        """
        player = self.engine.dsm.state.player
        return self.stringifier.stringify_nets(player)

    def get_trans(self):
        """
        get all possible transformations for dimension.
        """
        return self.stringifier.stringify_trans()
