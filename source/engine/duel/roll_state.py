from duel.duel_state import DuelState

class RollState(DuelState):
    """
    State were the roll the dice.
    """
    def __init__(self, duel, player, opponent):
        super().__init__(duel, player, opponent)
        self.name = "ROLL"

    def update(self, cmd):
        """
        Update state given command cmd.
        """
        if cmd["command"] == "ROLL":
            return self.run_roll_command(cmd)
        return super().update(cmd)

    def run_roll_command(self, cmd):
        """
        Run roll command.
        """
        # get the dice from the command
        dicelist = []
        for i in cmd["dice"]:
            dice = self.player.dicepool.get_dice(i)
            if not dice:
                reply = {"valid" : False,
                "message" : "Invalid dice index " + str(i)}
                return reply
            if dice in self.player.useddice:
                reply = {"valid" : False,
                "message" : "Dice " + str(i) + " already \
                    dimensioned"}
                return reply
            dicelist.append(dice)
        
        # roll the dice and get the rolled sides
        sides = []
        for dice in dicelist:
            sides.append(dice.roll())

        # add rolls into the the player crest pool
        for side in sides:
            self.player.crestpool.add_crests(side)
    
        # check if can summon and create next state
        if can_summon(sides):
            summon_dice = []
            for dice, side in zip(dicelist, sides):
                if side.crest.is_summon():
                    summon_dice.append(dice)
            #TODO: define next state dimension

        else: # cannot summon
            pass
            #TODO: define next state dungeon

        reply = {"valid" : True, "message" : ""}
        return reply, self
                    
def can_summon(sides):
    """
    Check if a list of sides is a valid summon roll: 2 or
    more summon crests.
    """
    summon_crests = 0
    for side in sides:
        if side.crest.is_summon():
            summon_crests += 1
    return summon_crests >= 2
