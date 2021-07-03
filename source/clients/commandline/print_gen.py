from stringifier import Stringifier

class PrintGen():
    """
    Generator for print command.
    """
    def __init__(self, icons):
        self.key = "p"
        self.desc = desc
        self.stringifier = Stringifier(icons)

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
        elif split[0]=="p" and len(split)==2:
            self.print_pool_dice(engine, split[1])
        elif split[0]=="d" and len(split)==1:
            self.print_dungeon(engine)
        elif split[0]=="d" and len(split)==2:
            self.print_dungobj(engine, split[1])
        elif split[0]=="c" and len(split)==1:
            self.print_crestpool(engine)
        elif split[0]=="oc" and len(split)==1:
            self.print_opponent_crestpool(engine)
        elif split[0]=="s" and len(split)==1:
            self.print_summons(engine)
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
        print(self.stringifier.stringify_dungeon(engine))

desc = "\
- PRINT COMMANDS: p ARGS\n\
    - p p:     print dice pool\n\
    - p p INT: print dice at INT in dice pool\n\
    - p d:     print dungeon\n\
    - p d XY:  print object in dungeon at position XY\n\
    - p c:     print own crest pool\n\
    - p oc:    print opponent crest pool\n\
    - p s:     print summon candidates"
