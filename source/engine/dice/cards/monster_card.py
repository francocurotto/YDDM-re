from dice.cards.summon_card import SummonCard

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
