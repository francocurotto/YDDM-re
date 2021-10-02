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
            "DIRECTATTACK" : self.gen_direct_attack,
            "REPLYATTACK"  : self.gen_reply_attack,
            "GUARD"        : self.gen_guard,
            "WAIT"         : self.gen_wait,
            "ENDTURN" : self.gen_endturn}

    def gen_string(self, reply):
        """
        Generates the reply string using cmddict.
        """
        return self.resultdict[reply["result"]](reply)

    def gen_roll(self, reply):
        roll = reply["roll"]
        string = ""
        if reply["dimlimit"]:
            string += "No more dice dimensions allowed\n"
        roll_string = self.stringifier.stringify_roll(roll)
        return string + "Go Dice Roll! " + roll_string

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
            " monster lord\n"
        # add monster lord
        string += self.stringifier.stringify_monster_lord(
            self.engine.duel, ml)
        # check for opponent loss
        if "ENDDUEL" in reply["flags"]:
            string += "\n" + opponent + " lost all " + \
                "their hearts.\n" + player + \
                " is the winner!"
        return string

    def gen_direct_attack(self, reply):
        opponent = self.engine.dsm.state.opponent.name
        # get attack preamble
        string = self.gen_attack_preamble(reply)
        # add nondefendig message
        string += "\n" + opponent + " cannot defend\n"
        # add damage message
        target = reply["target"]
        power = reply["power"]
        damage = reply["damage"]
        kill = reply["kill"]
        string += self.gen_damage(target, damage, kill, False)
        return string

    def gen_reply_attack(self, reply):
        return self.gen_attack_preamble(reply)

    def gen_guard(self, reply):
        monster = reply["monster"]
        target = reply["target"]
        defense = reply["defense"]
        retaliation = reply["retaliation"]
        damage = reply["damage"]
        kill = reply["kill"]
        # add defend message
        string = target + " defends " + "with " + \
            str(defense) + "\n"
        # add damage message
        if damage == 0:
           string += "No damage inflicted"
        elif retaliation:
            string += self.gen_damage(monster, damage, kill,
                True)
        else:
            string += self.gen_damage(target, damage, kill,
                False)
        return string

    def gen_wait(self, reply):
        target = reply["target"]
        damage = reply["damage"]
        kill = reply["kill"]
        return self.gen_damage(target, damage, kill, False)

    def gen_attack_preamble(self, reply):
        monster = reply["monster"]
        target = reply["target"]
        advantage = reply["advantage"]
        power = reply["power"]
        string = ""
        # distinguish between adv, disadv, and neutral
        if "ADV" in advantage:
             string += monster +  " has advantage over " + \
                target + "\n"
        if "DAV" in advantage:
             string += monster + " has disadvantage over " +\
                target + "\n"
        # get attack power
        string += monster + " attacks " + target + \
            " with " + str(power)
        return string
        
    def gen_damage(self, damaged, damage, kill, retaliation):
        # add damage message
        string = damaged + " received " + str(damage) + \
            " damage"
        if retaliation:
            string += " in retaliation"
        # add kill message
        if kill:
            string += "\n" + damaged + " is dead"
        return string

    def gen_endturn(self, reply):
        return "Turn finished!"
