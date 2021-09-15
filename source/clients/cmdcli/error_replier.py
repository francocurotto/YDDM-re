class ErrorReplier():
    """
    Converts an error reply from the engine into a text 
    reply.
    """
    def __init__(self, engine):
        self.engine = engine
        self.errordict = {
            "InvalidCommand"    : self.gen_invalidcommand,
            "DuplicatedDice"    : self.gen_duplicateddice,
            "DiceAlreadyUsed"   : self.gen_dicealreadyused,
            "OOBDinIndex"       : self.gen_oobdimindex,
            "NotPlayerMonster"  : self.gen_notplayermonster,
            "NotOpponentTarget" : self.gen_notopponenttarget,
            "AttackOutOfRange"  : self.gen_attackoutofrange,
            "MonsterInCooldown" : self.gen_monsterincooldown,
            "NotPathFound"      : self.gen_notpathfound}

    def gen_string(reply):
        """
        Generates reply string using the errordict.
        """
        self.errordict[reply["error"]](reply["args"])

    def gen_invalidcommand(self, args):
        return "Invalid command " + args[0] + " at state " +\
            self.engine.dsm.state.name

    def gen_duplicateddice(self, args):
        return "Duplicated dice in roll"

    def gen_dicealreadyused(self, args):
        return "Dice already dimensioned"

    def gen_oobdimindex(self, args):
        return "Invalid dimension index"
        
    def gen_notplayermonster(self, args):
        return "No player monster at " + str(args[0])

    def gen_notopponenttarget(self, args):
        return "No opponent target at " + str(args[0])

    def gen_attackoutofrange(self, args):
       return "Attack is out of range"

    def gen_monsterincooldown(self, args):
        return  args[0] + " already attacked this turn"

    def gen_notpathfound(self, args):
        return "No path found between " + str(args[0]) + \
            " and " + str(args[1])
