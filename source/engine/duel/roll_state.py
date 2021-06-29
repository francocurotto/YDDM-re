from duel.duel_state import DuelState

class RollState(DuelState):
    """
    State were the player roll the dice.
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
            dice = self.player.dicepool.contents[i]
            if dice in self.player.dimdice:
                self.reply["message"] = "Dice " + str(i) + \
                    " already dimensioned"
                return self.reply, self
            dicelist.append(dice)
        
        # roll the dice and get the rolled sides
        sides = []
        for dice in dicelist:
            sides.append(dice.roll())

        # add rolls into the the player crest pool
        for side in sides:
            self.player.crestpool.add_crests(side)
    
        # get dice available for dimension
        dimdice = get_dimdice(dicelist, sides)

        # define next state
        if self.can_dimension(dimdice):
            from duel.dim_state import DimState
            nextstate = DimState(self.duel, self.player,
                self.opponent, dimdice)
        else: # cannot dimension
            nextstate = self
            #from duel.dungeon_state import DungeonState
            #TODO: define dungeon state
            #nextstate = DungeonState(self.duel, self.player,
            #    self.opponent)

        # fill success reply
        self.reply["message"] = "Go Dice Roll!"
        if self.player.hit_dim_limit():
            self.reply["message"] += "\nNo more dice " + \
                "dimensions allowed"
        self.reply["roll"] = serialize_sides(sides)
        return self.reply, nextstate

    def can_dimension(self, dimdice):
        """
        True if player can dimension, that is, there are 
        available to dimension and  the player has not hit
        the dice limit.
        """
        return dimdice and not self.player.hit_dim_limit()
                    
def get_dimdice(dicelist, sides):
    """
    Given the dice and the sides rolled (in the same order),
    return a list of dice available to dimension, that is, if
    two or more dice of the same level rolled a summon crest.
    If no dice available, return an empty list.
    """
    # check for all levels
    for level in range(1,5):
        dimdice = []
        # check if dice rolled a specific level
        for dice, side in zip(dicelist, sides):
            if dice.level==level and side.crest.is_summon():
                dimdice.append(dice)
        # if two or more rolled summon, return filled list
        if len(dimdice) >= 2:
            return dimdice
    # no dice available for dimension found
    return []

def serialize_sides(sides):
    """
    Convert list of side objects into a list of serialized 
    dicts.
    """
    return [side.serialize() for side in sides]
