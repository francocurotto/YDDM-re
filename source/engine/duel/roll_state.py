from duel.duel_state import DuelState
from errors import DuplicatedDice, DiceAlreadyUsed

class RollState(DuelState):
    """
    State were the player roll the dice.
    """
    def __init__(self, duel, player, opponent):
        super().__init__(duel, player, opponent)
        self.name = "ROLL"
        self.cmddict = {"ROLL" : self.run_roll_command}
        self.errors = (DuplicatedDice, DiceAlreadyUsed)

    def run_roll_command(self, cmd):
        """
        Run roll command.
        """
        # get the dice list
        dicelist = self.get_dicelist(cmd["dice"])
        sides = self.roll_dice(dicelist)
        self.player.rolls.append(sides)
        nextstate = self.get_nextstate(dicelist, sides)

        # fill success reply
        self.reply["valid"] = True
        self.reply["message"] += "Go Dice Roll!"
        return self.reply, nextstate

    def get_dicelist(self, intlist):
        """
        Creates a dicelist from a list of ints from a 
        command.
        """
        # check for duplicates
        if len(intlist) != len(set(intlist)):
            raise DuplicatedDice

        # get dice from the intlist
        dicelist = []
        for i in intlist:
            dice = self.player.dicepool[i]
            if dice in self.player.dimdice:
                raise DiceAlreadyUsed
            dicelist.append(dice)
        return dicelist

    def roll_dice(self, dicelist):
        """
        Roll dice from dice list and add roll to player crest 
        pool.
        """
        # roll dice and get sides
        sides = []
        for dice in dicelist:
            sides.append(dice.roll())
        # add rolls into the the player crest pool
        for side in sides:
            self.player.crestpool.add_crests(side)
        return sides

    def get_nextstate(self, dicelist, sides):
        """
        Determines next state given the dice and the sides 
        rolled (in the same order), i.e., if player can 
        dimension or not.
        """
        # get dice available for dimension
        dimdice = get_dimdice(dicelist, sides)
        # define next state
        if self.can_dimension(dimdice):
            from duel.dim_state import DimState
            nextstate = DimState(self.duel, self.player,
                self.opponent, dimdice)
        else: # cannot dimension
            from duel.dungeon_state import DungeonState
            nextstate = DungeonState(self.duel, self.player,
                self.opponent)
        return nextstate

    def can_dimension(self, dimdice):
        """
        True if player can dimension, that is, there are 
        available to dimension and the player has not hit the
        dimension limit.
        """
        if self.player.hit_dim_limit():
            self.reply["message"] += "No more dice " + \
                "dimensions allowed\n"
            return False
        return dimdice
                    
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
