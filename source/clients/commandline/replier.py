class Replier():
    """
    Print the information of a reply of the engine.
    """
    def __init__(self, engine, stringifier):
        self.engine = engine
        self.stringifier = stringifier

    def print_reply(self, reply):
        message = reply["message"]
        
        # reply has roll result
        if "ROLL" in reply["flags"]:
            message = self.add_roll(message)

        # reply indicates an attack to a monster lord
        if "MLATTACK" in reply["flags"]:
            message = self.add_ml_attack(message)

        # print only if there is a message
        if message:
            print(message)

    def add_roll(self, message):
        """
        Add roll to roll message
        """
        roll = self.engine.dsm.state.player.rolls[-1]
        string = " " + self.stringifier.stringify_roll(roll)
        return message + string

    def add_ml_attack(self, message):
        """
        Add the ml print to ml attack message.
        """
        duel = self.engine.duel
        ml = self.engine.dsm.state.opponent.ml
        string = self.stringifier.stringify_monster_lord(
            duel, ml)
        string = "\n" + string
        if "\n" in message: # case third heart
            message = message.replace("\n", string+"\n", 1)
        else: # first or second heart
            message += string
        return message
