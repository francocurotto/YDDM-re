from dungeon.dicenets.pos import Pos

class Replier():
    """
    Converts a reply from the engine into a text reply.
    """
    def __init__(self, engine, stringifier):
        self.engine = engine
        self.stringifier = stringifier
        self.resultdict = {
            "ROLL"         : self.gen_roll,
            "DIM"          : self.gen_dim,
            "SKIP"         : self.gen_skip,
            "MOVE"         : self.gen_move,
            "MLATTACK"     : self.gen_ml_attack,
            "DIRCETATTACK" : self.gen_direct_attack,
            "REPLYATTACK"  : self.gen_reply_attack,
            #"GUARD"        : self.gen_guard,
            #"WAIT"         : self.gen_wait,
            "ENDTURN" : self.gen_endturn}

    def gen_string(self, reply):
        """
        Generates the reply string using cmddict.
        """
        return self.resultdict[reply["result"]](reply)

    def gen_roll(self, reply):
       roll = reply["roll"]
       string = self.stringifier.stringify_roll(roll)
       return "Go Dice Roll! "  + string

    def gen_dim(self, reply):
        return "Dimension The Dice!"

    def gen_skip(self, reply):
        return  "Dimension skipped"

    def gen_move(self, reply):
        monster = reply["monster"]
        origin = reply["origin"]
        dest = reply["dest"]
        ostr = self.stringifier.stringify_pos(origin)
        dstr = self.stringifier.stringify_pos(dest)
        return monster + " moved " + "from " + ostr + \
            " to " + dstr

    def gen_ml_attack(self, reply):
        monster = reply["monster"]
        player = self.engine.dsm.state.player.name
        opponent = self.engine.dsm.state.opponent.name
        ml = self.engine.dsm.state.opponent.ml
        # add attack message
        string = monster + " attacks " + opponent + \
            " monster lord"
        # add monster lord
        string += self.stringifier.stringify_monster_lord(
            self.engine.duel, ml)
        # check for opponent loss
        if "ENDDUEL" in reply["flags"]:
            string += "\n" + opponent + " lost all " + \
                "their hearts.\n" + player + \
                " is the winner!"
        return string

    def gen_direct_attack(selg, reply):
        string = ""
        monster = reply["monster"]
        target = reply["target"]
        power = reply["power"]
        opponent = self.engine.dsm.state.opponent.name
        # distinguish between adv, disadv, and neutral
        if "ADV" in reply["advantage"]:
             string += monster +  " has advantage over " + \
                target + "\n"
        if "DAV" in reply["advantage"]:
             string += monster + " has disadvantage over " +\
                target + "\n"
        # get attack power
        string += monster + " attacks " + target + \
            " with " + str(power)
        # add nondefendig message
        string += "\n" + opponent + " cannot defend\n"
        # add damage message
        string += target + " received " + str(power) + \
            " damage"
        # add kill message
        if reply["kill"]:
            string += "\n" + monster + " is dead"
        return string

    def gen_endturn(self, reply):
        return "Turn finished!"
