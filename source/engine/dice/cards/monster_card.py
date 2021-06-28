from dice.cards.summon_card import SummonCard
from dungobj.dragon      import Dragon
from dungobj.spellcaster import Spellcaster
from dungobj.undead      import Undead
from dungobj.beast       import Beast
from dungobj.warrior     import Warrior

class MonsterCard(SummonCard):
    """
    Object that contains the information of a monster.
    """
    def __init__(self, info):
        super().__init__(info)
        self.attack = info["ATTACK"]
        self.defense = info["DEFENSE"]
        self.life = info["LIFE"]

    def is_monster(self):
        return True

    def summon(self):
        """
        Return a summon based on card.
        """
        return summon_dict[self.type](self)

summon_dict = {
    "DRAGON"      : Dragon,
    "SPELLCASTER" : Spellcaster,
    "UNDEAD"      : Undead,
    "BEAST"       : Beast,
    "WARRIOR"     : Warrior}
