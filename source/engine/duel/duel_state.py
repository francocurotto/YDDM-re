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
        By default, the command is invalid.
        """
        reply["message"] = "Invalid command " + \
            cmd["command"] + " at state " + self.name
        return reply, self
