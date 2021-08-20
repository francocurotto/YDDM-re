class DuelState():
    """
    Generic duel state.
    """
    def __init__(self, duel, player, opponent):
        self.duel = duel
        self.player = player
        self.opponent = opponent

    def update(self, cmd):
        """
        try to run command. If invalid send appropriate 
        response.
        """
        # initialize reply dict before every command
        self.reply = init_reply()
        try:
            return self.cmddict[cmd["command"]](cmd)
        except KeyError:
            self.reply["message"] = "Invalid command " + \
                cmd["command"] + " at state " + self.name
            return self.reply, self

def init_reply():
    """
    Initialize a reply dict with default values.
    """
    return {"valid":False, "message":"", "flags":[]}
