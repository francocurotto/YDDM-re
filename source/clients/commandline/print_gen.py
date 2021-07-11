from sanitize_functs import *

class PrintGen():
    """
    Generator for print command.
    """
    def __init__(self, engine, stringifier):
        self.key = "p"
        self.desc = desc
        self.engine = engine
        self.stringifier = stringifier

    def create_command(self, split):
        """
        Print the desired info. Return None as command.
        """
        # sanitize split
        if not split:
            return None
        # print dice pool
        if split[0]=="p" and len(split)==1:
            self.print_pool()
        # print dice
        elif split[0]=="p" and len(split)==2:
            self.print_pool_dice(split[1])
        # print dungeon
        elif split[0]=="d" and len(split)==1:
            self.print_dungeon()
        # print dungeon object
        elif split[0]=="d" and len(split)==2:
            self.print_dungobj(split[1])
        # print crest pool
        elif split[0]=="c" and len(split)==1:
            self.print_crestpool()
        # print opponent crest pool
        elif split[0]=="oc" and len(split)==1:
            self.print_opponent_crestpool()
        # print summon candidates
        elif split[0]=="s" and len(split)==1:
            self.print_summons()
        # print nets
        elif split[0]=="n" and len(split)==1:
            self.print_nets()
        # print trans
        elif split[0]=="t" and len(split)==1:
            self.print_trans()
        else:
            print("Invalid print command")
        return None

    def print_pool(self):
        """
        Print player pool.
        """
        player = self.engine.dsm.state.player
        print(self.stringifier.stringify_dicepool(player))

    def print_pool_dice(self, string):
        """
        Print player dice at index string in dice pool.
        """
        # convert string to index
        i = str2index(string, 0, 14)
        if i is not None:
            dicepool = self.engine.dsm.state.player.dicepool
            dice = dicepool[i]
            print(self.stringifier.stringify_dice(dice))

    def print_dungeon(self):
        """
        Print dungeon.
        """
        duel = self.engine.duel
        print(self.stringifier.stringify_dungeon(duel))

    def print_dungobj(self, string):
        """
        Print object in dungeon at position string.
        """
        coor = str2coor(string)
        if not coor:
            return
        y = coor[0]; x = coor[1]
        tile = self.engine.duel.dungeon.array[y][x]
        if not tile.is_dungeon() or not tile.is_occupied():
            print("Nothing to print there")
            return
        duel = self.engine.duel
        dungobj = tile.content
        print(self.stringifier.stringify_dungobj(duel, \
            dungobj))

    def print_crestpool(self):
        """
        Print player crestpool.
        """
        cpool = self.engine.dsm.state.player.crestpool
        print(self.stringifier.stringify_crestpool(cpool))

    def print_opponent_crestpool(self):
        """
        Print opponent crestpool.
        """
        cpool = self.engine.dsm.state.opponent.crestpool
        print(self.stringifier.stringify_crestpool(cpool))

    def print_summons(self):
        """
        Print player's summoning options after roll.
        """
        # check for correct state
        if self.engine.dsm.state.name != "DIM":
            print("Can print summons in DIM state only")
            return
        dimdice = self.engine.dsm.state.dimdice
        print(self.stringifier.stringify_dicelist(dimdice))

    def print_nets(self):
        """
        Print all possible nets for dimension.
        """
        player = self.engine.dsm.state.player
        print(self.stringifier.stringify_nets(player))

    def print_trans(self):
        """
        Print all possible transformations for dimension.
        """
        print(self.stringifier.stringify_trans())

desc = "\
- PRINT COMMANDS: p ARG1 [ARG2]\n\
    - p p:     print dice pool\n\
    - p p INT: print dice at INT in dice pool\n\
    - p d:     print dungeon\n\
    - p d XY:  print object in dungeon at position XY\n\
    - p c:     print own crest pool\n\
    - p oc:    print opponent crest pool\n\
    - p s:     print summon candidates"
