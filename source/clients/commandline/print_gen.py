class PrintGen():
    """
    Generator for print command.
    """
    def __init__(self, stringifier):
        self.key = "p"
        self.desc = desc
        self.stringifier = stringifier

    def create_command(self, engine, split):
        """
        Print the desired info. Return None as command.
        """
        # sanitize split
        if not split:
            return None
        # print dice pool
        if split[0]=="p" and len(split)==1:
            self.print_pool(engine)
        # print dice
        elif split[0]=="p" and len(split)==2:
            self.print_pool_dice(engine, split[1])
        # print dungeon
        elif split[0]=="d" and len(split)==1:
            self.print_dungeon(engine)
        # print dungeon object
        elif split[0]=="d" and len(split)==2:
            self.print_dungobj(engine, split[1])
        # print crest pool
        elif split[0]=="c" and len(split)==1:
            self.print_crestpool(engine)
        # print opponent crest pool
        elif split[0]=="oc" and len(split)==1:
            self.print_opponent_crestpool(engine)
        # print summon candidates
        elif split[0]=="s" and len(split)==1:
            self.print_summons(engine)
        # print nets
        elif split[0]=="n" and len(split)==1:
            self.print_nets(engine)
        # print trans
        elif split[0]=="t" and len(split)==1:
            self.print_trans(engine)
        return None

    def print_pool(self, engine):
        """
        Print player pool.
        """
        pool = engine.dsm.state.player.dicepool
        print(self.stringifier.stringify_dicelist(pool))

    def print_pool_dice(self, engine, i):
        """
        Print player dice at i in dice pool.
        """
        # sanitize index i
        try:
            i = int(i)
        except ValueError:
            print("Cannot convert integer")
            return
        try:
            dice = engine.dsm.state.player.dicepool[i-1]
        except IndexError:
            print("Integer out of pool bound")
            return
        print(self.stringifier.stringify_dice(dice))

    def print_dungeon(self, engine):
        """
        Print dungeon.
        """
        duel = engine.duel
        print(self.stringifier.stringify_dungeon(duel))

    def print_dungobj(self, engine, coor):
        """
        Print object in dungeon at position coor.
        """
        # convert and sanitize coor
        try:
            # separate coordinates
            x = coor[0]; y = coor[1:]
            # convert coordinate to ints
            x = ord(x)-97; y = int(y)-1
        except (IndexError, ValueError):
            print("Cannot interpret coordinates " + coor)
            return
        try:
            tile = engine.duel.dungeon.array[y][x]
        except IndexError:
            print("Coordinates out of dungeon bound")
            return
        if not tile.is_dungeon() or not tile.is_occupied():
            print("Nothing to print there")
            return
        duel = engine.duel
        dungobj = tile.content
        print(self.stringifier.stringify_dungobj(duel, \
            dungobj))

    def print_crestpool(self, engine):
        """
        Print player crestpool.
        """
        cpool = engine.dsm.state.player.crestpool
        print(self.stringifier.stringify_crestpool(cpool))

    def print_opponent_crestpool(self, engine):
        """
        Print opponent crestpool.
        """
        cpool = engine.dsm.state.player.crestpool
        print(self.stringifier.stringify_crestpool(cpool))

    def print_summons(self, engine):
        """
        Print player's summoning options after roll.
        """
        # check for correct state
        if engine.dsm.state.name != "DIM":
            print("Can print summons in DIM state only")
            return
        dimdice = engine.dsm.state.dimdice
        print(self.stringifier.stringify_dicelist(dimdice))

    def print_nets(self, engine):
        """
        Print all possible nets for dimension.
        """
        print(self.stringifier.stringify_nets(engine))

    def print_trans(self, engine):
        """
        Print all possible transformations for dimension.
        """
        print(self.stringifier.stringify_trans(engine))

desc = "\
- PRINT COMMANDS: p ARG1 [ARG2]\n\
    - p p:     print dice pool\n\
    - p p INT: print dice at INT in dice pool\n\
    - p d:     print dungeon\n\
    - p d XY:  print object in dungeon at position XY\n\
    - p c:     print own crest pool\n\
    - p oc:    print opponent crest pool\n\
    - p s:     print summon candidates"
