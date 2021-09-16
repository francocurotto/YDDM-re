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
        self.reply = init_reply(cmd)
        try:
            return self.cmddict[cmd["command"]](cmd)
        except KeyError:
            self.reply["error"] = "InvalidCommand"
            self.reply["args"] = (cmd["command"],)
            return self.reply, self
        except self.errors as e:
            self.reply["error"] = e.__class__.__name__
            self.reply["args"] = e.args
            return self.reply, self

def init_reply(cmd):
    """
    Initialize a reply dict with default values.
    """
    return {"cmd":cmd, "valid":False, "flags":[], 
        "message":""}
