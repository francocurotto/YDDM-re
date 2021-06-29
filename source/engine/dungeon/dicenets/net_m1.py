from dungeon.dicenets.dicenet import DiceNet
from dungeon.dicenets.pos import Pos

class NetM1(DiceNet):
    """
    Dice net with a specific shape.
    """
    name = "M1"
    def __init__(self):
        self.pos_list = [Pos(-1,-1),Pos(-1,0),
                                    Pos(0,0),
                                    Pos(1,0),Pos(1,1),
                                             Pos(2,1)]
        self.center_pos = self.get_center_pos()
