class HumanPlayer():
    """
    Player controled by human.
    """
    def __init__(self, playerid, engine, ctrl):
        self.name = engine.duel.players[playerid-1].name
        self.ctrl = ctrl
        self.view = self.ctrl.view

    def get_command(self):
        """
        Get a proper engine command from the controller.
        """
        return self.ctrl.get_command()

    def update_view(self, reply):
        """
        Update view given engine reply.
        """
        self.view.update(reply)
