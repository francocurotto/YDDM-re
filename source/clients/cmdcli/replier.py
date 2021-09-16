class Replier():
    """
    Converts a reply from the engine into a text reply.
    """
    def __init__(self, engine, stringifier):
        self.engine = engine
        self.stringifier = stringifier
        self.cmddict ={
            "ROLL"    : self.gen_roll}
            #"DIM"     : self.gen_dim,
            #"SKIP"    : self.gen_skip,
            #"MOVE"    : self.gen_move,
            #"ATTACK"  : self.gen_attack,
            #"GUARD"   : self.gen_guard,
            #"WAIT"    : self.gen_wait,
            #"ENDTURN" : self.gen_endturn}



    def gen_string(self, reply):
        """
        Generates the reply string using cmddict.
        """
        return self.cmddict[reply["cmd"]["command"]](reply)

    def gen_roll(self, reply):
       roll = self.engine.dsm.state.player.rolls[-1]
       roll_string = self.stringifier.stringify_roll(roll)
       return "Go Dice Roll! "  + roll_string
