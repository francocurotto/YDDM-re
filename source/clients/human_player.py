class HumanPlayer():
    """
    Player controled by human.
    """
    def __init__(self, playerid, engine, ctrl):
        self.name = engine.duel.players[playerid-1].name
        self.ctrl = ctrl
        self.view = self.ctrl.view

    def init_turn(self):
        """
        Initialize turn.
        """
        pass

    def get_command(self):
        """
        Get a proper engine command from the controller.
        """
        return self.ctrl.get_command()

    def process_reply(self, reply):
        """
        Update view given engine reply.
        """
        self.view.process_reply(reply)
        
