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
        By default, the command is invalid.
        """
        reply = {"valid" : False,
            "message" : "Invalid command " + cmd["command"] +
                        " at state " + self.name}
        return reply, self
