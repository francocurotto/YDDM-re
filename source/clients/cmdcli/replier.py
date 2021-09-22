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
        tgpos = Pos(*reply["cmd"]["dest"])
        target = self.engine.duel.dungeon.get_content(tgpos)
        # distinguish between monster and ml
        if target.is_monster_lord():
            return self.gen_ml_attack(reply)
        else: # monster attack
            return self.gen_monster_attack(reply)

    def gen_ml_attack(self, reply):
        mnpos = Pos(*reply["cmd"]["origin"])
        monster = self.engine.duel.dungeon.get_content(mnpos)
        player = self.engine.dsm.state.player
        opponent = self.engine.dsm.state.opponent
        string = monster.name + " attacks " + \
            opponent.name + " monster lord"
        # check for opponent loss
        if self.opponent.ml.hearts <= 0:
            string += ".\n" + opponent.name + " lost all " +\
                "their hearts.\n" + player.name + \
                " is the winner!"
        return string

        # distinguish between adv, disadv, and neutral
        # get attack power
        # distinguish between reply state and dungeon state

    def gen_endturn(self, reply):
        return "Turn finished!"
