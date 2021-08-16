class DuelState():
    """
    Generic duel state.
    """
    def __init__(self, duel, player, opponent):
        self.duel = duel
        self.player = player
        self.opponent = opponent
        self.reply = {
            "valid"   : False,
            "newturn" : False,
            "endduel" : False,
            "message" : ""}

    def update(self, cmd):
        """
        try to run command. If invalid send appropriate 
        response.
        """
        # reset message after every command
        self.reply["message"] = ""
        try:
            return self.cmddict[cmd["command"]](cmd)
        except KeyError:
            self.reply["message"] = "Invalid command " + \
                cmd["command"] + " at state " + self.name
            return self.reply, self
