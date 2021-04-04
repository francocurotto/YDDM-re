from summon_crest import SummonCrest
from movement_crest import MovementCrest
from attack_crest import AttackCrest
from defense_crest import DefenseCrest
from magic_crest import MagicCrest
from trap_crest import TrapCrest

class Side():
    """
    A side from a dice. Includes the crest and the 
    multiplier.
    """
    def __init__(side_string):
        self.crest = crest_dict[side_string[0]]()
        if len(side_string) > 1:
            self.multiplier = int(side_string[1:])
        else:
            self.multiplier = 1

crest_dict = {"S" : SummonCrest,
              "M" : MovementCrest,
              "A" : AttackCrest,
              "D" : DefenseCrest,
              "G" : MagicCrest,
              "T" : TrapCrest}
