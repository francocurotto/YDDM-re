from cmdcli.generators.print_gen import PrintGenerator

class CursesPrintGen(PrintGenerator):
    """
    Curses specific print generator.
    """
    def __init__(self, engine, stringifier):
        super().__init__(engine, stringifier)
        self.descdict["p"] = printdesc

    # redefine get string
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
        # get dice
        elif split[0]=="p" and len(split)==2:
            return self.get_dice(split[1])
        # get opponent dice
        elif split[0]=="op" and len(split)==2:
            return self.get_opponent_dice(split[1])
        # get dungeon object
        elif split[0]=="d" and len(split)==2:
            return self.get_dungobj(split[1])
        # get summon candidates
        elif split[0]=="s" and len(split)==1:
            return self.get_summons()
        # get nets
        elif split[0]=="n" and len(split)==1:
            return self.get_nets()
        # get trans
        elif split[0]=="t" and len(split)==1:
            return self.get_trans()
        elif split[0]=="o" and len(split)==1:
            return self.get_opponent()
        else:
            return "Invalid print command"

    def get_opponent(self):
        """
        Hack to get opponent info by manually switching 
        players in engine.
        """
        if self.engine.dsm.state.name != "ENDDUEL":
            return "Can only see opponent info at the " + \
            "end of duel"
        self.engine.dsm.state.player, \
            self.engine.dsm.state.opponent = \
            self.engine.dsm.state.opponent, \
            self.engine.dsm.state.player
        return "Switching players"

printdesc = "\
- PRINT COMMANDS: p [ARG1 ARG2]\n\
    - p:        print this help\n\
    - p cmd     print command list\n\
    - p cmd CMD print command CMD description\n\
    - p p INT:  print dice at INT in own dice pool\n\
    - p op INT: print dice at INT in opponent dice pool\n\
    - p d XY:   print object in dungeon at position XY\n\
    - p s:      print summon candidates\n\
    - p n:      print nets\n\
    - p t:      print transformations\n\
    - p o:      print opponent info"
