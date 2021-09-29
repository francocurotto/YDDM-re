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
            #"MLATTACK"     : self.gen_ml_attack,
            #"DIRCETATTACK" : self.gen_direct_attack,
            #"REPLYATTACK"  : self.gen_reply_attack,
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

    def gen_attack(self, reply):
        mnpos = Pos(*reply["cmd"]["origin"])
        tgpos = Pos(*reply["cmd"]["dest"])
        monster = self.engine.duel.dungeon.get_content(mnpos)
        target = self.engine.duel.dungeon.get_content(tgpos)
        # distinguish between monster and ml
        if target.is_monster_lord():
            return self.gen_ml_attack(reply, monster)
        else: # monster attack
            return self.gen_monster_attack(reply, monster,
                target)

    def gen_ml_attack(self, reply, monster):
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

    def gen_monster_attack(selg, reply, monster, target):
        string = ""
        # distinguish between adv, disadv, and neutral
        if "ADVANTAGE" in reply["flags"]:
             sring += monster.name +  " has advantage " + \
                "over " + target.name + "\n"
        if "DISADVANTAGE" in reply["flags"]:
             string += monster.name + " has disadvantage " +\
                "over " + target.name+"\n"
        # get attack power
        string += monster.name + " attacks " + \
            target.name + " with " + reply["power"]
        # distinguish between reply state and dungeon state

    def gen_endturn(self, reply):
        return "Turn finished!"
