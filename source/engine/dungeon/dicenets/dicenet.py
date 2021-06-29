from dungeon.dicenets.pos import Pos

class DiceNet():
    """
    Positions of the tiles created when a dice is dimensioned
    (unfolded).
    """
    trans = ["TCW", "TCCW", "FUD", "FLR"]
    def __init__(self):
        self.center = self.get_center()
        self.trans_dict = {}
        self.transfunc = [self.turn_cw, self.turn_ccw,
            self.flip_lr, self.flip_ud]
        for name, func in zip(self.names, self.transfunc):
            self.trans_dict[name] = func

    def get_center(self):
        """
        Returns the center position of net given by Pos(0,0).
        """
        for pos in self.poslist:
            if pos == Pos(0,0):
                return pos

    def apply_trans(self, translist):
        """
        Apply a list of transformations, identified by 
        strings to the net.
        """
        for trans in translist:
            self.trans_dict[trans]()

    def offset(self, offset):
        """
        Move all positions on net an offset amount. 
        """
        for pos in self.poslist:
            pos.offset(offset)
        
    def turn_cw(self):
        """
        Turn all positions on net clock-wise 90 degrees.
        """
        for pos in self.poslist:
            pos.turn_cw()

    def turn_ccw(self):
        """
        Turn all positions on net counter clock-wise 90
        degrees.
        """
        for pos in self.poslist:
            pos.turn_ccw()

    def flip_lr(self):
        """
        Turn all positions on net left-right.
        """
        for pos in self.poslist:
            pos.flip_lr()

    def flip_ud(self):
        """
        Turn all positions on net up-down.
        """
        for pos in self.poslist:
            pos.flip_ud()

def create_net(string, log):
    #imports
    from .net_t1 import NetT1
    from .net_t2 import NetT2
    from .net_z1 import NetZ1
    from .net_z2 import NetZ2
    from .net_x1 import NetX1
    from .net_x2 import NetX2
    from .net_m1 import NetM1
    from .net_m2 import NetM2
    from .net_s1 import NetS1
    from .net_s2 import NetS2
    from .net_l1 import NetL1
    net_class_list = [NetT1, NetT2, NetZ1, NetZ2, NetX1, NetX2,
        NetM1, NetM2, NetS1, NetS2, NetL1]

    # if string coincides with name return net instance
    for net_class in net_class_list:
        if string == net_class.name:
            return net_class(log)
    # invalid net name
    return None
