from dungeon.dicenets.dicenet import DiceNet
from dungeon.dicenets.pos import Pos

class NetZ1(DiceNet):
    """
    Dice net with a specific shape.
    """
    name = "Z1"
    def __init__(self):
        self.poslist = [Pos(-1,-1),Pos(-1,0),
                                   Pos(0,0),
                                   Pos(1,0),
                                   Pos(2,0),Pos(2,1)]
        super().__init__()
