from dice.crests.crest import Crest
from dice.crests.summon_crest import SummonCrest
from dice.crests.movement_crest import MovementCrest
from dice.crests.attack_crest import AttackCrest
from dice.crests.defense_crest import DefenseCrest
from dice.crests.magic_crest import MagicCrest
from dice.crests.trap_crest import TrapCrest

class Side():
    """
    A side from a dice. Includes the crest and the 
    multiplier.
    """
    def __init__(self, side_string):
        crest_char = side_string[0]
        # create crest
        self.crest = crest_dict[crest_char]()
        # create multiplier
        if len(side_string) > 1:
            self.mult = int(side_string[1:])
        else:
            self.mult = 1

    def serialize(self):
        """
        Return a serialized version of side.
        """
        serialized = {"crest" : self.crest.name, 
            "mult" : self.mult}
        return serialized

crest_dict = {"S" : SummonCrest,
              "M" : MovementCrest,
              "A" : AttackCrest,
              "D" : DefenseCrest,
              "G" : MagicCrest,
              "T" : TrapCrest}
