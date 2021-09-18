from dungeon.dicenets.pos import Pos

class Replier():
    """
    Converts a reply from the engine into a text reply.
    """
    def __init__(self, engine, stringifier):
        self.engine = engine
        self.stringifier = stringifier
        self.cmddict = {
            "ROLL"    : self.gen_roll}
            "DIM"     : self.gen_dim,
            "SKIP"    : self.gen_skip,
            "MOVE"    : self.gen_move,
            "ATTACK"  : self.gen_attack,
            #"GUARD"   : self.gen_guard,
            #"WAIT"    : self.gen_wait,
            "ENDTURN" : self.gen_endturn}

    def gen_string(self, reply):
        """
        Generates the reply string using cmddict.
        """
        return self.cmddict[reply["cmd"]["command"]](reply)

    def gen_roll(self, reply):
       roll = self.engine.dsm.state.player.rolls[-1]
       roll_string = self.stringifier.stringify_roll(roll)
       return "Go Dice Roll! "  + roll_string

    def gen_dim(self, reply):
        return "Dimension The Dice!"

    def gen_skip(self, reply)
        return  "Dimension skipped"

    def gen_move(self, reply):
        origin = Pos(*reply["cmd"]["origin"])
        dest = Pos(*reply["cmd"]["dest"])
        monster = self.engine.duel.dungeon.get_content(dest)
        return monster.name + " moved " + "from " + \
            str(origin) + " to " + str(dest)

    def gen_attack(self, reply);
        # distinguish between monster and ml
        # distinguish between adv, disadv, and neutral
        # get attack power
        # distinguish between reply state and dungeon state

    def gen_endturn(self, reply):
        return "Turn finished!"




