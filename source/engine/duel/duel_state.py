class DuelState():
    """
    Generic duel state.
    """
    def __init__(self, duel, player, opponent):
        self.duel = duel
        self.player = player
        self.opponent = opponent
        self.reply = {
            "valid"   : True,
            "newturn" : False,
            "endduel" : False,
            "message" : ""}

    def update(self, cmd):
        """
        By default, the command is invalid.
        """
        self.reply["valid"] = False
        self.reply["message"] = "Invalid command " + \
            cmd["command"] + " at state " + self.name
        return self.reply, self
